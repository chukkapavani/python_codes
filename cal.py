#calculator problem
class calculator:
  def getvals(self):
    self.a=int(input("enter a value"))
    self.b=int(input("enter b value"))
  def putvals(self):
    print("a=",self.a)
    print("b=",self.b)
  def add(self):
    return self.a+self.b
  def sub(self):
    return self.a-self.b
  def mul(self):
    return self.a*self.b
  def div(self):
    return self.a/self.b
  def mod(self):
    return self.a%self.b
  def exp(self):
    return self.a**self.b
  def floordiv(self):
    return self.a//self.b
o=calculator()
o.getvals()
o.putvals()
print("-----")
ch=int(input("enter choice"))
if(ch==1):
  print("addition of two numbers:",o.add())
elif(ch==2):
  print("subraction=",o.subb)
elif(ch==3):
  print("multiplication=",o.mul())
elif(ch==4):
  print("division=",o.div())
elif(ch==5):
  print("modulus=",o.mod())
elif(ch==6):
  print("expo=",o.exp())
elif(ch==7):
  print("floor division=",o.floordiv())
else:
  print("invalid choice")
