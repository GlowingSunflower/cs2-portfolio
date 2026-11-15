for num in range (1,15) :
  if num % 3 == 0:
    continue
  print (num)

# 1st line: range(1, 15) gives numbers from 1 to 14.
# 2nd line: The code will check if num % 3 is equal to 0. If num % 3 is 1 and 1 is not equal to 0, then the if block is skipped and will proceed to continue.
# Line 1 and 2 will repeat. If a multiple of 3 appears, line 2 will then skip it and not print.
# The whole code repeats and continues until it reaches 14.
