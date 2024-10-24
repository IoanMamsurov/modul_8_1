def add_everything_up(a, b):
    try:
        a + b
    except TypeError:
        if type(a) is str:
            b = str(b)
        elif type(b) is str:
            a = str(a)
    return (a + b)


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
