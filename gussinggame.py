#number gussing game
import random
x=int(input("enter xc value:"))
y=random.randint(1,10)
if(x>y):
  print("x is greaterthan y")
else:
  print("y is greaterthan x")