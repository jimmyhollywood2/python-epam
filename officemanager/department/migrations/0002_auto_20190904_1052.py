# Generated by Django 2.2.4 on 2019-09-04 10:39

from django.db import migrations

def add_titles_dep(apps, schema_editor):
    title_list = [
        'Business Intelligence',
        'IT Management',
        'Administration',
        'IT Procurement',
        'IT Security',
        'Network Adminstration',
        'Systems Analyst & Architecture',
        'User Support & Services'
    ]

    for line in title_list:
        Dep = apps.get_model('department', 'Departments')
        newdep = Dep(name = line)
        newdep.save()

class Migration(migrations.Migration):

    dependencies = [
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_titles_dep),
    ]



