from django.contrib.auth.models import User
from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404

from application.models import Store
from dashboard.forms import StoreForm, AdminUserForm, AdminProfileForm
from users.models import Profile


def get_admin(request):
    return render(
        request,
        'dashboard/admin.html'
    )


def get_stores(request):
    stores = Store.objects.all()
    return render(
        request,
        'dashboard/stores.html',
        context={'stores': stores}
    )


def get_store(request, pk):
    store = get_object_or_404(Store, pk=pk)
    operators = store.store_operators.all()
    return render(
        request,
        'dashboard/store.html',
        context={'store': store, 'operators': operators}
    )


def get_profiles(request):
    profiles = Profile.objects.all()
    return render(
        request,
        'dashboard/profiles.html',
        context={'profiles': profiles}
    )


def create_store(request):
    if request.method == 'POST':
        store_form = StoreForm(request.POST)
        if store_form.is_valid():
            store_form.save(commit=False)
            store_form.save()
            store_form.save_m2m()
            return redirect('stores')
        else:
            print('Error')
    else:
        store_form = StoreForm()
    return render(
        request,
        'dashboard/create_store.html',
        context={'store_form': store_form}
    )


def update_store(request, pk):
    store = Store.objects.get(pk=pk)
    if request.method == 'POST':
        store_form = StoreForm(request.POST, instance=store)
        if store_form.is_valid():
            store_form.save(commit=False)
            store_form.save()
            store_form.save_m2m()
            return redirect('stores')
        else:
            print('Error')
    else:
        store_form = StoreForm(instance=store)
    return render(
        request,
        'dashboard/create_store.html',
        context={'store_form': store_form}
    )


@transaction.atomic
def update_profile(request, pk):
    user = User.objects.get(pk=pk)
    user_profile = Profile.objects.get(pk=pk)
    if request.method == 'POST':
        admin_user_form = AdminUserForm(request.POST, instance=user)
        admin_profile_form = AdminProfileForm(request.POST, instance=user_profile)
        if admin_user_form.is_valid() and admin_profile_form.is_valid():
            admin_user_form.save()
            admin_profile_form.save()
            return redirect('profile', user_profile)
        else:
            print('Please correct the error below.')
    else:
        admin_user_form = AdminUserForm(instance=user)
        admin_profile_form = AdminProfileForm(instance=user_profile)
    return render(request, 'dashboard/update_profile.html', {
        'admin_user_form': admin_user_form,
        'admin_profile_form': admin_profile_form
    })


@transaction.atomic
def create_profile(request):
    if request.method == 'POST':
        admin_user_form = AdminUserForm(request.POST)
        admin_profile_form = AdminProfileForm(request.POST)
        if admin_user_form.is_valid() and admin_profile_form.is_valid():
            admin_user_form.save()
            user_profile = admin_profile_form.save(commit=False)
            user = User.objects.last()
            user_profile.user = user
            print(user_profile.user)
            user_profile.save()
            print('OK')
            return redirect('profiles')
        else:
            print('Please correct the error below.')
    else:
        admin_user_form = AdminUserForm()
        admin_profile_form = AdminProfileForm()
    return render(request, 'dashboard/create_profile.html', {
        'admin_user_form': admin_user_form,
        'admin_profile_form': admin_profile_form
    })



