 import sys,string, math,itertools

 n,k = input().split()
 n,k = int(n),int(k)
 L = [ int(x) for x in input().split()]
 if k in L :
     print('Yes')
 else :
     print('No')
