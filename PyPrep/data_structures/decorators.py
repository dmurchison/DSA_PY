# Decorators
# Decorators are functions that take another function as an argument and return a function.
# The returned function is called a wrapper function.
# The wrapper function is used to extend the behavior of the original function without permanently modifying it.
# Decorators are used to add functionality to an existing function without modifying the function itself.
# Decorators are usually called before the definition of a function you want to decorate.

def response_to_approacher(name, approaching=True):  # This is the decorator function (response_to_approacher)
    def inner_response(func):  # This is the function that will be returned by the decorator (response_to_approacher)
        def wrapper(*args, **kwargs):  # This is the function that will be called instead of the original function (func)
            if approaching:
                print(f"A {name} is coming")
            else:
                print(f"A {name} is leaving")
            response = func(*args, **kwargs)
            return response

        return wrapper  # This is the function that will be called instead of the original function (func)
    return inner_response  # This is the function that will be returned by the decorator (response_to_approacher)


def print_hello(func):
    def wrapper(*args, **kwargs):
        print("Hello")
        response = func(*args, **kwargs)
        return response
    return wrapper


@response_to_approacher("Milkman", False)  # This is the decorator (response_to_approacher)
@print_hello  # This is the decorator (print_hello)
def make_sound(sound):  # This is the function that will be decorated (make_sound)
    return sound * 2


return_val = make_sound("Woof")
print("return_val:", return_val)
print("make_sound.__name__:", make_sound.__name__)
