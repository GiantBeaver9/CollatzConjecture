#The Following is the Collatz Conjecture
#If the number is even, divide by 2
#If odd, we multiply by 3 then add 1
#This eventually goes to 1 in all known usages
#However, this is not proven, ergo this is a way to test numbers
#Once a number hits a number equal to 2^n, it will go to 0
#You can find this in any number that is calculable.
User_Input = int(input("Enter a number greater than 1: \n"))
count = 0;
while(User_Input > 1):
  if(User_Input % 2 == 0):
    User_Input /= 2
  else:
    User_Input *= 3
    User_Input += 1
  count += 1
  print(int(User_Input))
