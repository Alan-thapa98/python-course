

a = 54  # global variable


def func1():
    global a  # it mean all the globe of the a
    print(f" these is the local variable 1: {a}")
    a = 8  # lical variable
    print(f" these is the local variable 2: {a}")


func1()
print(f" these is the local variable 3: {a}")
