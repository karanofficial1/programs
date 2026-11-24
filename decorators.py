def decorator1(func):
    def wrapper():
        print("Start")
        func()
        print("End")
    return wrapper


def decorator2(func):
    def wrapper():
        print("Welcome")
        func()
    return wrapper

@decorator1
@decorator2
def hello():
    print("Hello, karan")


hello()