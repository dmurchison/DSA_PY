import time

# Use an empty list characters and a += augmented assignment statement to convert the string 'Birthday' into a list of characters.
characters = []
characters += 'Birthday'
print(characters)


n = 501
def prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

start_time = time.time()  # start timing
print(prime(n))  # call your function
end_time = time.time()  # end timing
print("Execution time: ", end_time - start_time)  # print the execution time

# Commit Sauce

n = 501
def prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
