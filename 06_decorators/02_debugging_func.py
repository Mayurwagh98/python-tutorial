def debug(func):
    def wrapper(*args, **kwargs):
        agrs_value = ", ".join(str(arg) for arg in args)
        agrs_value = ", ".join(f"{k}={v}" for k, v in kwargs.items())
        result = func(*args, **kwargs)
        print(f"calling {func.__name__} and args {agrs_value} and kwargs {agrs_value}")
        return result
    return wrapper


@debug
def hello():
    print("hello")

@debug
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}")

hello()
greet("mayur","namaste")
greet(name="User",greeting="good morning")