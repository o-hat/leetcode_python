from functools import wraps

def decorate(func):

    @wraps(func)
    def wrapper():
        print("=========before=========")
        func()
        print("=========before=========")
    return wrapper


@decorate
def hello():
    print("hello world!")


hello()
print(hello.__name__)
