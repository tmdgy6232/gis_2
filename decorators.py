class User:
    def __init__(self, is_authenticated):
        self.is_authenticated = is_authenticated

def decorator1(func):
    def decorator(*args, **kwargs):
        w = args[0]
        h = args[1]
        if w > 0 or h > 0:
            print('good')
            return func(*args)
        else:
            raise ValueError('음수다인마')

    return decorator

def login_required(func):
    def decorated(w, h, **kwargs):
        if kwargs.get('user').is_authenticated:
            return func(w, h, **kwargs)
        else: raise ValueError('is_authenticated Error')
    return decorated

@login_required
@decorator1
def triangle(w, h, **kwargs):
    val = w * h / 2
    return val

@decorator1
def box(w, h, **kwargs):
    val = w * h
    return val

print(box(2,3))
