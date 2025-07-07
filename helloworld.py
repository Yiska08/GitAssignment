import math

print("Hello, bubba world!")

#Assuming that the list is already in ascending order

def median(input):
  input = sorted(input)
  medianVal = 0
  if len(input) % 2 == 0:
    a = input[math.floor(len(input) / 2 - 1) ]
    b = input[math.floor(len(input) / 2)]
    medianVal = (a + b) / 2
  else:
    medianVal = input[math.floor(len(input) / 2)]
  return medianVal



print(median([0, 3, 5, 7, 10, 11, 32, 87, 100, 999]))

