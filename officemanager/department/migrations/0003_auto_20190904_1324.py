# Generated by Django 2.2.4 on 2019-09-04 11:06

from django.db import migrations
from random import randint, random

def add_employees(apps, schema_editor):
    
    Emp = apps.get_model('department','Employee')
    Dep = apps.get_model('department', 'Department')
    dep_list = Dep.objects.all()
    fname_list = [
        'Dmitri',
        'Alexandra',
        'Ivan',
        'Anastasia',
        'Lena',
        'Krisitna',
        'Nina',
        'Madina',
        'Yana',
        'Kostya',
        'Nikolay',
        'Valeriy',
        'Artem',
        'Kirill',
        'Daniil',
        'Olga',
        'Tamara'
    ]
    lname_list = [
        'Divanko',
        'Kaveruk',
        'Korzh',
        'Smit',
        'Snow',
        'Bolton',
        'McFly',
        'Alba',
        'Stepaniuk',
        'Kluni',
        'Kot',
        'Hyneman',
        'Savage',
        'Dronov',
        'Lutz',
        'Linus',
        'Meladze'
    ]
    
    Emp.objects.bulk_create(
        (Emp(
            department = dep_list[randint(0,len(dep_list)-1)],
            first_name = fname_list[randint(0,len(fname_list)-1)],
            last_name = lname_list[randint(0,len(lname_list)-1)],
            d_of_b = '{}-{}-{}'.format(randint(1950,2010),randint(1,12),randint(1,28)),
            salary = round(random()*20000,2)
        ) for i in range(100))
    )

def reverce_add(apps, schema_editor):
    Emp = apps.get_model('department','Employee')
    Emp.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('department', '0002_auto_20190904_1052'),
    ]

    operations = [
        migrations.RunPython(add_employees, reverce_add)
    ]
