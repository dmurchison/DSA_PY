from typing import Optional, Union

def test_function(x: int, y: int) -> Union[float, None]:
    if y != 0:
        return x / y
    return None



return_val = test_function(1, 2)
print(return_val)
return_val = test_function(1, 0)
print(return_val)

