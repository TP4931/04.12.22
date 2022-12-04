x=int(input())
y=int(input())
if x<y:
 for x in range(x,y+1):
     print(x)
if y<x:
 for x in range(x,y-1,-1):
     print(x)