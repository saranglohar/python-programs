def fizz_buzz(number: int):
      if number % 3 == 0 and number % 5 == 0:
          return "FizzBuzz"
      if number % 3 == 0:
        return "Fizz"
      if number % 5 == 0:
          return "Buzz"
      return number


print(fizz_buzz(15))



