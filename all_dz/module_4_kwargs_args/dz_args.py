def add_numbers(*args):
    return sum(args)

def create_list(*args):
    c = []
    for i in args:
        c.append(i)
    return c

def pass_arguments(*args):
    for arg in args:
        print('print_args = ', arg)



def print_args(*args):
    pass_arguments(*args)

def find_max(*args):
    return max(args)

def join_strings(*args):
    return ' '.join(args)

