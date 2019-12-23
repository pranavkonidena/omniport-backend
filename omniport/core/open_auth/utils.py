from omniport.utils import switcher

AvatarSerializer = switcher.load_serializer('kernel', 'Person', 'Avatar')

def get_field_data(person, field_data_points, model_string):
    """
    Utility function to get requested model's data.
    :param person: Person object whose data is to be retreived.
    :param field_data_points: The specific fields of a model to be retreied.
    :param model_string: model name string to access the data
    """
    data = {}
    if eval(model_string) is None:
        return data
    for field_data_point in field_data_points:
        data[f'{field_data_point}'.replace('.', ' ')] = eval(f'{model_string}.{field_data_point}')
    return data

def get_roles(person):
    """
    Utility function to return the name and active status of person's roles.
    :param person: Person object whose roles are to be retreived.
    """
    all_roles = (AvatarSerializer(person).data['roles'])
    for role in all_roles:
        del role['data']
    return all_roles