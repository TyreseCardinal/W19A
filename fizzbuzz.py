def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

if __name__ == "__main__":
    import random
    random_numbers = [7, 28, 99, 50, 69, 32, 77, 81, 11, 20, 2, 48, 92, 41, 70]
    for num in random_numbers:
        fizzbuzz(num)
