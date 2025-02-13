def log_decorator(f):
    def wrapper(*args,**kwargs):
        print(f'Function Name : {f.__name__}')
        print(f'Function Arguments : {args}')
        print(f'Function Keyword Arguments : {kwargs}')
        result = f(*args,**kwargs)
        return result
    return wrapper


@log_decorator
def greet(name, greeting = "안녕하세요",**kwargs):
    return f"{greeting}, {name}"

print(greet("인하"))
print(greet("인하","곤방와"))
print(greet("James","Hello",age=29))
