from datetime import datetime, timedelta

from django.contrib.auth.models import User
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from application.forms import ApplicationForm, ChangeDriverForm, ChangeStatusForm
from application.models import Application, Client, ClientPerson, ClientAddress, Store, Status
from users.models import Profile


def get_json_client_data(request):
    clients = list(Client.objects.values())
    return JsonResponse({'data': clients})


def get_json_client_person_data(request, *args, **kwargs):
    selected_client = kwargs.get('client')
    client_persons = list(ClientPerson.objects.filter(client__client_name=selected_client).values())
    return JsonResponse({'data': client_persons})


def get_json_client_address_data(request, *args, **kwargs):
    selected_client = kwargs.get('client')
    client_address = list(ClientAddress.objects.filter(client__client_name=selected_client).values())
    return JsonResponse({'data': client_address})


def new_application(request):
    clients = Client.objects.all()
    if request.method == 'POST':
        application_form = ApplicationForm(request.POST, request.FILES, initial={'manager': request.user.pk})
        if application_form.is_valid():
            orders = request.POST.getlist('order_1c')
            orders_ids = []
            for order in orders:
                orders_ids.append(order)
            app_form = application_form.save(commit=False)
            app_form.created_by = request.user.profile
            app_form.created_at = timezone.now()
            app_form.order = app_form.created_at.strftime('%d%m%Y%H%M%S')
            app_form.order_1c = ', '.join(orders_ids)
            if '_save' in request.POST:
                app_form.status = Status.objects.get(pk=1)
            if '_send' in request.POST:
                app_form.status = Status.objects.get(pk=2)
            app_form.save()
            return redirect('get_all_applications')
        else:
            print(application_form.errors)
            print(application_form.cleaned_data)
            return HttpResponse(application_form.errors.values())
    else:
        application_form = ApplicationForm(initial={'manager': request.user.pk})

    return render(request, 'application/new_application.html', {
        'application_form': application_form,
        'clients': clients,
        'manager_profile': request.user
    })


def application(request, pk):
    application_id = get_object_or_404(Application, pk=pk)
    user = request.user
    post = request.POST
    manager = application_id.manager.user
    date = application_id.order_date.strftime('%Y-%m-%d')
    date_now = datetime.today().strftime('%Y-%m-%d')
    try:
        driver = application_id.driver.user
    except:
        driver = None

    status_id = application_id.status.pk
    cancel, delivered, delivering = False, False, False

    if user == manager and status_id != 7:
        cancel = True

    if user == driver and status_id == 5 and date == date_now:
        delivering = True

    if user == driver and status_id == 6 and date == date_now:
        delivered = True

    print(
        'Cancel: '+str(cancel),
        ' Delivered: '+str(delivered),
        ' Delivering: '+str(delivering)
    )

    if '_cancel' in post:
        application_id.status = Status.objects.get(pk=7)
        application_id.save()
        cancel = False

    if '_delivered' in post:
        application_id.status = Status.objects.get(pk=8)
        application_id.save()
        delivered = False

    if '_delivering' in post:
        application_id.status = Status.objects.get(pk=5)
        application_id.save()
        delivering = False

    return render(
        request,
        'application/application.html',
        context={'application': application_id, 'cancel_access': cancel, 'delivered_access': delivered,
                 'delivering_access': delivering}
    )


def get_all_applications(request, *args, **kwargs):
    applications = Application.objects.all().filter(status_id=5).order_by('-order_date')
    return render(
        request,
        'application/applications.html',
        context={'applications': applications}
    )


def get_my_applications(request, manager):
    applications = Application.objects.filter(manager__user__username=manager).order_by('order_date')
    return render(
        request,
        'application/my_applications.html',
        context={'my_applications': applications}
    )


def get_store(request, store_id):
    store = Store.objects.get(store_operators=store_id)
    applications = Application.objects.filter(store=store).order_by('order_date')
    applications_new = applications.filter(status_id=2)
    applications_collected = applications.filter(status_id=3)
    applications_collecting = applications.filter(status_id=4)
    applications_waiting = applications.filter(status_id=5)
    applications_delivered = applications.filter(status_id=8)
    return render(
        request,
        'application/store.html',
        context={
            'applications_new': applications_new,
            'applications_collected': applications_collected,
            'applications_collecting': applications_collecting,
            'applications_waiting': applications_waiting,
            'applications_delivered': applications_delivered,
            'store': store}
    )


def get_applications_without_drivers(request):
    current_date = datetime.now().strftime("%Y-%m-%d")
    next_date = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
    applications_without_drivers = Application.objects.filter(driver=None, status_id=4,
                                                              order_date=current_date).order_by('order_date')
    applications_without_drivers_tomorrow = Application.objects.filter(driver=None, status_id=4,
                                                                       order_date=next_date).order_by('order_date')
    applications = Application.objects.filter(order_date=current_date).exclude(driver=None).order_by('order_date')
    return render(
        request,
        'application/routes.html',
        context={'applications': applications, 'applications_wo_drs': applications_without_drivers,
                 'applications_wo_drs_tmrw': applications_without_drivers_tomorrow}
    )


def get_application_without_driver(request, pk):
    application_without_driver = Application.objects.get(pk=pk)
    if request.method == 'POST':
        driver_form = ChangeDriverForm(request.POST, instance=application_without_driver)
        if driver_form.is_valid():
            f = driver_form.save(commit=False)
            f.status = Status.objects.get(pk=5)
            f.save()
            return redirect('applications_wo_dr')
        else:
            return HttpResponse(driver_form.errors.values())
    else:
        driver_form = ChangeDriverForm(instance=application_without_driver)
    return render(
        request,
        'application/route.html',
        context={'driver_form': driver_form, 'application': application_without_driver}
    )


def get_application_for_change_status(request, store_id, pk_store):
    application_for_change_status = Application.objects.get(pk=pk_store)
    if request.method == 'POST':
        status_form = ChangeStatusForm(request.POST, instance=application_for_change_status)
        if status_form.is_valid():
            f = status_form.cleaned_data['status']
            print(f)
            status_form.save()
            return redirect('store', store_id)
        else:
            print(status_form.errors.as_data())
            return HttpResponse(status_form.errors.values())
    else:
        status_form = ChangeStatusForm(instance=application_for_change_status)
    return render(
        request,
        'application/operator_application.html',
        context={'status_form': status_form, 'application': application_for_change_status}
    )


def get_driver_applications(request, pk):
    current_date = datetime.now().strftime("%Y-%m-%d")
    next_date = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
    driver_applications = Application.objects.filter(driver=pk, order_date=current_date).order_by('order_date')
    driver_applications_tomorrow = Application.objects.filter(driver=pk, order_date=next_date).order_by('order_date')
    return render(
        request,
        'application/driver_applications.html',
        context={'applications': driver_applications, 'applications_tmrw': driver_applications_tomorrow, }
    )
