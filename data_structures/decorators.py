# Decorators

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


@response_to_approacher("Milkman", False)  # This is the decorator (response_to_approacher)
def make_sound(sound):  # This is the function that will be decorated (make_sound)
    return sound * 2


return_val = make_sound("Woof")
print("return_val:", return_val)


