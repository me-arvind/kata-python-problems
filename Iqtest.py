def iq_test(string):
  numbers = string.split()
  odd = 0
  even = 0
  pos = 0
  
  for i in range(0,len(numbers)):
    if (int(numbers[i])%2==0):
      even = even + 1
    else:
      odd = odd + 1
      
  if (odd>even):
    for i range(0,len(0,numbers)):
      if (int(numbers[i]%2) == 0):
        pos = i+1
  else:
    for i range(0, len(0,numbers)):
      if (int(numbers[i]%2 != 0)):
        pos = i+1
  return pos      
      
