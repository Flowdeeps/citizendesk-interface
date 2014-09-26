entity = {
    'schema': {
        'first_name': {
            'type': 'string',
            'required': True
        },
        'last_name': {
            'type': 'string',
            'required': True
        },
        'email': {
            'type': 'string',
            'required': False
        },
        'location': {
            'type': 'string',
            'required': False
        }
    },
    'resource_methods': ['GET', 'POST'],
    'item_methods': ['GET', 'PUT', 'PATCH', 'DELETE'],
    'pagination': False
}
