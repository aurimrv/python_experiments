# This class implements a single method, factorial, 
# which accepts an integer as parameter and calculates
# the factorial of any number greather or equals 1 and
# returns its factorial.
#
# For negative numbers the factorial methods returns None
# indicating factorial is not defined for negative numbers.
class Training:
    @staticmethod
    def factorial(n):
      if (n >= 0):
         fact = 1
         while (n > 1):
            fact = fact * n
            n = n - 1
      else:
         fact = None

      return fact

def main():
   print("Type an integer number: ", end="")
   n = int(input())

   fact = Training.factorial(n)

   if (fact is None):
      print("Error: there is no factorial for negative numbers")
   else:
      print("Factorial of %d is %d." % (n, fact))

if (__name__ == '__main__'):
   main()