#cycloni number
i=1
n=int(input("enter a number..:"))
l=n%10
while(n!=0):
  f=n%10
  n=n//10
if(l==f):
  print("cyclonic")
else:
  print("not")