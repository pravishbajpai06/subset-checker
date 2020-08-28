def check():
  a=int(input())
  s=set(map(int,input().split()))
  b=int(input())
  c=set(map(int,input().split()))
  l=list()
  for i in s:
    if i in c:
      l.append(i)
  l=set(l)
  if l==s:
    print("True")
  else:
    print("False")
d=int(input())
for  in range(d):
  check()
  
