REQUEST_SCHEMA = {
    'type': 'object',
    'properties': {
        'name': {'type': 'string', 'minLength': 1},
        'dob': {'type': 'string', 'minLength': 1},
        'question': {'type': 'string', 'minLength': 1},
        'past-card': {
            'type': 'object',
            'properties': {
                'name': {'type': 'string', 'minLength': 1},
                'isUpRight': {'type': 'boolean'}
            },
            'required': ['name', 'isUpRight'],
            'additionalProperties': False
        },
        'present-card': {
            'type': 'object',
            'properties': {
                'name': {'type': 'string', 'minLength': 1},
                'isUpRight': {'type': 'boolean'}
            },
            'required': ['name', 'isUpRight'],
            'additionalProperties': False
        },
        'future-card': {
            'type': 'object',
            'properties': {
                'name': {'type': 'string', 'minLength': 1},
                'isUpRight': {'type': 'boolean'}
            },
            'required': ['name', 'isUpRight'],
            'additionalProperties': False
        }
    },
    'required': ['name', 'dob', 'question', 'past-card', 'present-card', 'future-card'],
    'additionalProperties': False
}