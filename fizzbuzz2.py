# This version will check entered number
# to meet condition of Fizz, Buzz or FizzBuzz

def num(i):
    if i % 3 == 0 and i % 5 ==0:
        i = "FizzBuzz"
    elif i % 3 == 0:
        i = "Fizz"
    elif i % 5 == 0:
        i = "Buzz"
    return i

print("\n"*5)
print("I'll check if your number divisible to 3 or 5 or both numbers")
print("you'll see Fizz, Buzz or FizzBuzz respectively if it's matches")
print("let's begin: \n")
try:
    x = input("Please input digital number(s): ")
    print(num(int((x))))
except ValueError:
    print("Please use number(s) (0-9)")
