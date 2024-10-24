with open("./ned.txt") as f:
    n=int(f.readline())
    e=int(f.readline())
    d=int(f.readline())
m=input('encode or decode (e/d):')
x=int(input('x:'))
if m=='e':
    print(pow(x,e,n))
elif m=='d':
    print(pow(x,d,n))
