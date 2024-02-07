
def even_odd(num):
    for n in range(1, num+1):
        if n % 2 == 0:
            print(f"The number {n} is even")
        else:
            print(f"The number {n} is odd")

name = input("Hello, what is your name? ")
print(f"Hi {name}, nice to meet you!")

number = int(input("Type in how many numbers to check for even or odd: "))
even_odd(number)