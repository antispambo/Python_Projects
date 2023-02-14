digits = {0: 9471, 1: 10102, 2: 10103, 3: 10104, 4: 10105}

n = input(" Input: ")

new_n = ""

for i in n:
  i = int(i)
  i = chr(digits[i])
  new_n = new_n + i

print("Output: %s " % new_n)
