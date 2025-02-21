def greet(**kwargs):
    print(f'Hello, {kwargs['name']},! You are {kwargs['age']} years old')


def create_dict(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')

def update_setting(**kwargs):
    default_settings = {"theme": "light", "notifications": True}


def filter_kwargs(**kwargs):
    for key, value in kwargs.items():
        if int(value) > 10:
            print(f'{key}: {value}')

def log_kwargs(a, b, **kwargs):
    for key, value in kwargs.items():
        if value is not None:
            print(f'{key}: {value}')

