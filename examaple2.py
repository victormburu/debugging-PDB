def multiply(x, y):
  total = x * y
  return total

a = int(input("enter first number : "))
b = int(input("enter second number: "))
import pdb; pdb.set_trace() # breakpoint
result = multiply(a, b)
print(f"the result is: {result}")