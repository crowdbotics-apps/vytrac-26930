from icecream import ic


def make_fields_permissions(Permission, ContentType, Model):

    modle_name = Model.__name__.lower()
    permissions = []
    for item in Model._meta.fields:
        permissions.append(('view_' + modle_name + '.' + item.name + '_field', 'Can view ' + modle_name + " " + item.name.replace('_', ' ')))
        permissions.append(('change_' + modle_name + '.' + item.name + '_field', 'Can change ' + modle_name + " " + item.name.replace('_', ' ')))


    for codename, permission_name in permissions:
        get, create =   Permission.objects.get_or_create(
            codename=codename,
            name=permission_name,
            content_type=ContentType.objects.get_for_model(Model),
        )

