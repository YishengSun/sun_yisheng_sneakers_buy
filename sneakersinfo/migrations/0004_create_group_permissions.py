from __future__ import unicode_literals
from itertools import chain

from django.db import migrations


def populate_permissions_lists(apps):
    permission_class = apps.get_model('auth', 'Permission')

    type_permissions = permission_class.objects.filter(content_type__app_label='sneakersinfo',
                                                             content_type__model='type')

    year_permissions = permission_class.objects.filter(content_type__app_label='sneakersinfo',
                                                          content_type__model='year')

    country_permissions = permission_class.objects.filter(content_type__app_label='sneakersinfo',
                                                                  content_type__model='country')

    company_permissions = permission_class.objects.filter(content_type__app_label='sneakersinfo',
                                                           content_type__model='company')
    
    agency_permissions = permission_class.objects.filter(content_type__app_label='sneakersinfo',
                                                           content_type__model='agency')

    sneakers_permissions = permission_class.objects.filter(content_type__app_label='sneakersinfo',
                                                         content_type__model='sneakers')

    order_permissions = permission_class.objects.filter(content_type__app_label='sneakersinfo',
                                                          content_type__model='order')

    perm_view_type = permission_class.objects.filter(content_type__app_label='sneakersinfo',
                                                           content_type__model='type',
                                                           codename='view_type')

    perm_view_year = permission_class.objects.filter(content_type__app_label='sneakersinfo',
                                                               content_type__model='year',
                                                               codename='view_year')

    perm_view_country = permission_class.objects.filter(content_type__app_label='sneakersinfo',
                                                               content_type__model='country',
                                                               codename='view_country')

    perm_view_company = permission_class.objects.filter(content_type__app_label='sneakersinfo',
                                                         content_type__model='company',
                                                         codename='view_company')
    
    perm_view_agency = permission_class.objects.filter(content_type__app_label='sneakersinfo',
                                                         content_type__model='agency',
                                                         codename='view_agency')
    
    perm_view_sneakers = permission_class.objects.filter(content_type__app_label='sneakersinfo',
                                                       content_type__model='sneakers',
                                                       codename='view_sneakers')

    perm_view_order = permission_class.objects.filter(content_type__app_label='sneakersinfo',
                                                        content_type__model='order',
                                                        codename='view_order')


    ci_user_permissions = chain(perm_view_type,
                                perm_view_year,
                                perm_view_country,
                                perm_view_agency,
                                perm_view_company,
                                perm_view_sneakers,
                                perm_view_order)

    ci_info_manager_permissions = chain(type_permissions,
                                 country_permissions,
                                 year_permissions,
                                 company_permissions,
                                 sneakers_permissions,
                                 agency_permissions,
                                 perm_view_order)

    ci_order_manager_permissions = chain(perm_view_type,
                                perm_view_year,
                                perm_view_country,
                                perm_view_agency,
                                perm_view_company,
                                perm_view_sneakers,
                                order_permissions)

    my_groups_initialization_list = [
        {
            "name": "ci_user",
            "permissions_list": ci_user_permissions,
        },
        {
            "name": "ci_info_manager",
            "permissions_list": ci_info_manager_permissions,
        },
        {
            "name": "ci_order_manager",
            "permissions_list": ci_order_manager_permissions,
        },
    ]
    return my_groups_initialization_list


def add_group_permissions_data(apps, schema_editor):
    groups_initialization_list = populate_permissions_lists(apps)

    Group = apps.get_model('auth', 'Group')
    for group in groups_initialization_list:
        if group['permissions_list'] is not None:
            group_object = Group.objects.get(
                name=group['name']
            )
            group_object.permissions.set(group['permissions_list'])
            group_object.save()


def remove_group_permissions_data(apps, schema_editor):
    groups_initialization_list = populate_permissions_lists(apps)

    Group = apps.get_model('auth', 'Group')
    for group in groups_initialization_list:
        if group['permissions_list'] is not None:
            group_object = Group.objects.get(
                name=group['name']
            )
            list_of_permissions = group['permissions_list']
            for permission in list_of_permissions:
                group_object.permissions.remove(permission)
                group_object.save()


class Migration(migrations.Migration):
    dependencies = [
        ('sneakersinfo', '0003_create_groups'),
    ]

    operations = [
        migrations.RunPython(
            add_group_permissions_data,
            remove_group_permissions_data
        )
    ]
