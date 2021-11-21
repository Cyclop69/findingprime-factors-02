#finding the factors of a number
def factor(num):
  list=[]
  for i in range(1,num):
    if num%i==0:
      list.append(i)
  return list
    
#checking if the factors are prime:
def prime_factor(num):
  listt=[]
  a=factor(num)
  for b in a:
    for t in range(2,b):
      if b%t==0:
        pass
      else:
        listt.append(b)       
     #kicking out repeated numbers(if coded correctly then nt necessary,which as a abeginner Icant)   
  f=set(listt)
  g=list(f)       
  return g
  
  
  
y=int(input("enter the number:"))

print("the prime factors are:")
z=prime_factor(y)
for i in z:
  print(i)


    
  
  
    
  

