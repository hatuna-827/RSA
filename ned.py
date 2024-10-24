def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    if a!=1:
        print("Error")
        exit()
    return
def is_prime(a):
    b=3
    c=0
    if a!=2 and a%2==0:
        print(a,"is not prime number")
        exit()
    for i in range(len(str(a))//2,-1,-1):
        while a>=c**2:
            c+=10**i
        c-=10**i
    while True:
        if b>c:
            return
        if a%b==0:
            print(a,"is not prime number")
            exit()
        b+=2
p=int(input())
is_prime(p)
q=int(input())
is_prime(q)
n=p*q
l=(p-1)*(q-1)
e=int(input())
gcd(e,l)
d=0
while True:
    if (l*d+1)%e==0:
        d=(l*d+1)//e
        break
    d+=1
with open("./ned.txt",mode='w') as f:
    f.write(f"{str(n)}\n")
    f.write(f"{str(e)}\n")
    f.write(f"{str(d)}\n")
