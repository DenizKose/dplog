import random
import sqlite3
from sqlite3 import Error
import os

import django

from homepage.views import get_quotes

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dplog.settings")
django.setup()
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from users.models import Profile, ProfileStatus
from application.models import Client, ClientAddress, ClientPerson

eng = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
       'w', 'x', 'y', 'z']
nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

db = '../db.db'


def connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


# def select(conn):
#     list_status = ['m', 'd', 'o', 'a']
#     cur = conn.cursor()
#     for i in range(2, 3):
#         num = random.randint(0, 3)
#         list_username = random.sample(eng, 4)
#         list_name = random.sample(eng, 6)
#         list_surname = random.sample(eng, 8)
#         name = ''.join(list_name).capitalize()
#         surname = ''.join(list_surname).capitalize()
#         username = ''.join(list_username).capitalize()
#         pswd = str(num)+name+surname
#         status = list_status[i]
#         print(name + ' ' + surname)
#         print(str(i) + ' ' + str(status))
#         cur.execute('INSERT INTO auth_user (username, first_name, last_name, password, is_superuser) VALUES (?,?,?,?,FALSE)',
#                     (username, name, surname,pswd))
#     rows = cur.fetchall()
#     for row in rows:
#         print(row)
#     cur.close()
# conn = connection(db)
# print(select(conn))


def create_user(qty):
    for i in range(3, qty):
        num = random.randint(0, 3)
        list_username = random.sample(eng, 4)
        list_name = random.sample(eng, 6)
        list_surname = random.sample(eng, 8)
        name = ''.join(list_name).capitalize()
        surname = ''.join(list_surname).capitalize()
        username = ''.join(list_username).capitalize()
        pswd = str(num) + name + surname
        #
        # print(name + ' ' + surname)
        # print(str(i) + ' ' + str(status))
        user = get_user_model().objects.create_user(username=username, first_name=name, last_name=surname,
                                                    password=pswd)
        print(user)
    print('Done!')


def create_profile(qty):
    users = User.objects.all()
    ids = users.values_list('id', flat=True)
    users = list(sorted(ids))
    for i in users[0:qty]:
        num = random.randint(2, 4)
        profile = Profile.objects.get(pk=i)
        print(profile.user.profile.status)
        status = ProfileStatus.objects.get(pk=num)

        print(profile)
        profile.status = status
        print(profile.status_id)
        print(str(profile.user.username)+" "+str(profile.status.profile_status_name))
        profile.save()
    print('Done!')


itn_1 = random.sample(nums, len(nums))
itn_2 = random.sample(nums, len(nums))
id1c = random.sample(eng + nums, len(eng + nums))

itn = itn_1 + itn_2


def create_client():
    for i in range(1, 101):
        itn_1 = random.sample(nums, len(nums))
        itn_2 = random.sample(nums, len(nums))
        id1c = random.sample(eng + nums, len(eng + nums))

        itn = itn_1 + itn_2
        name = 'Client '
        client = Client.objects.create(client_name=name+' '+str(i))
        client.client_itn = ''.join(itn)[:12]
        client.client_1c_id = ''.join(id1c)[:10]
        client.save()

        print(client)


def create_address():
    for i in range(0, 400):
        id = random.randint(1, 100)
        address = ClientAddress.objects.create(address='st.'+str(i), client_id=id)
        address.save()
        print(address)
        #name = ClientPerson.objects.create(client_person_name='Name ' + str(i), client_id=id)
        #name.save()
        #print(name)


def test():
    print(''.join(itn)[:12])
    print(''.join(id1c)[:10])

# create_user(99)
#create_profile(97)
#create_client()
#create_address()

#get_quotes()


def update_profile():
    users = User.objects.all()
    ids = users.values_list('id', flat=True)
    users = list(sorted(ids))
    users = len(users)
    print(users)
    for i in range(1, users+1):
        user = User.objects.get(pk=i)
        profile = Profile.objects.get(pk=i)
        user.first_name = 'Deniz '+str(i)
        user.last_name = 'Kose '+str(i)
        profile.father_name = 'Kadirovich '+str(i)
        user.save()
        profile.save()
        print(user.last_name+' '+user.first_name+' '+profile.father_name)


def update_client():
    clients = Client.objects.all()
    ids = clients.values_list('id', flat=True)
    clients = list(sorted(ids))
    clients = len(clients)
    print(clients)
    for i in range(1, clients+1):
        client = Client.objects.get(pk=i)
        client.client_name = 'Roga and Kopyta '+str(i)
        client.save()
        print(client.client_name)

def update_addresses():
    addresses = ClientAddress.objects.all()
    ids = addresses.values_list('id', flat=True)
    addresses = list(sorted(ids))
    addresses = len(addresses)
    print(addresses)
    for i in range(1, addresses+1):
        address = ClientAddress.objects.get(pk=i)
        address.address = 'st. Ivana Ivanova, '+str(i)
        address.save()
        print(address.address)


#update_profile()
#update_client()
update_addresses()