def decorator1(fucc):
    def decorator(*args):
        w = args[0]
        h = args[1]
        if w > 0 or h > 0:
            print('good')
            fucc(*args)
        else:
            raise ValueError('음수다인마')

    return decorator

@decorator1
def triangle(w, h):
    val = w * h / 2
    print(val)

@decorator1
def box(w, h):
    val = w * h
    print(val)

triangle(-22, -22)
box(3,3)