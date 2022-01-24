l=[]
l2=[]
a=int(input('Enter range of list:'))
for i in range (0,a):
    b=int(input('Enter number:'))
    l.append(b)
print('The list:',l)
for j in l:
    if j>=0:
        l2.append(j)
print("The list of positive integers is:",l2)        
