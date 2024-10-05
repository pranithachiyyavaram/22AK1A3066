n=int(input("enter a number"))
original=n
arm=0
while(n>0):
    d=n%10
    arm=arm+(d*d*d)
    n=n//10
print(arm)
if(arm==original):
    print("armstrong")
else:
    print("not armstrong")
