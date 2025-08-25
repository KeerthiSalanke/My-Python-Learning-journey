#repitition
message = "warning!"*6
print (message*2)

print(message.upper())
print(message.strip()*2)
print(message.replace("warning","Error"))

name= '''chandan said "hello"'
darshan said "hi"'''
print (name)

print(len(message))#lenghth
name = "keerthi"

#Slicing string- we can extract the portion.
print (name[5])#index =position-1, position is 1,2,3 including spaces, but indeex starts with 0,1,2
print(name[2:6])
print(name[:5])
print(name[0])
#[start:end:skip] --- name[::]
print(name[::2])

#escape sequence-- are special characters in string that starts with a backslash.(\)
s= "keerthi \nis good gril"
print (s)

#operators---1]  assignment operators, basically it assigns some values.
a=100
a+= 100 #a=a+100 shortform
print (a)

x = 5#assigning 5 to x
x +=3 #equivalent to x = x + 3, now x is 8
x -=3 #equivalent to x = x - 3
x *=3 #equivalent to x = x * 3
x /=3 #equivalent to x = x / 3
print(x)

#2]Comparision operators
a=10
b=20
print(a==b) #false
print(a !=b)
print(a>b)
print(a<b)
print(a>=10)
print(b<=25)
#3] logical operators
print(True and True)
print(not(True))
print(1>2 or 2>1)
print(1>2 and 2>1)
print(not(1>2))
 
#membership opertors---in, not in
my_string ="python"
print("p" in my_string)

s="rose"
s2="rosewood"
print(("e" in s) and ("w" in s2))

#bitwise operators: perform operation on binary represenation of integers, usefull for low-level programming tasks like working with bits and bytes
#8 bits = 1 bytes
a = 5
b = 3
print( a&b) #and  (binary:001)
print(a | b)#or (binary:111)
print(a^b)#XOR (binary:110)
print(~a) #Bitwise NOT, inverts all bits 
print(a<<1) #left shift (binary:1010)
print(a>>1)#right shift (binary:010)
