import pdb

def add(a, b):
  pdb.set_trace()
  sum = a + b
  return sum

x = 5
y = 7
total = add(x, y)
print(f"the sum is: {total}")