def kwargs_to_dict(**kwargs):
    result = {}
    for key, value in kwargs.items():
        try:
            result[value] = key
        except:
            result[str(value)] = key
    return result

print(kwargs_to_dict(name='Даниил', Палавандзия='', weight=99.0,
                     months=['August', 'September', 'October'],
                     courses={'python'}))