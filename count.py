def count():
    d=len(l)
    for c in l:
     if c not in l1:
      count=0
      for j in range(0,d):
        if c==l[j]:
            count+=1
            l1.append(l[j]) 
      print(c,'=',count)
a=input('Enter word:')
l=[]
l1=[]
for i in a.strip():
    l.append(i)
count()
