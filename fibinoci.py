#fibinoci series
i=1;a=0;b=1
n=int(input("enter a number..:"))
while(i<=n):
  print(a,end=" ")
  c=a+b
  a=b
  b=c
  i=i+1
