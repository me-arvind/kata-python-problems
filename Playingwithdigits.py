def dig_pow(n, p):
  number = str(n)
  total = sum(int(number[i])**(p+i) for i in range(len(number)))
  if total%n == 0:
    return total/n
  else:
  return -1
  
  
  
