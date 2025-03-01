#amstrong number
i=1;s=0
n=int(input("enter a number:"))
t=n
while(i<=n):
  r=n%10
  s=s+r*r*r
  n=n//10
if(t==s):
    print("amstrong number")
else:
    print("not an amstrong")

