### FUNCTIONS ###

def my_function():
    print("Hello from a function")

def suum(*args):
    sum = 0
    for num in args:
        sum += num
    print(sum)

suum(1, 3, 2)