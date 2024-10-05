def sum_of_digits(x):
    sum=0
    while(x>0):
        d1=x%10
        sum=sum+d1
        x=x//10
    return sum
dd=int(input("enter the day"))
mm=int(input("enter the month"))
yyyy=int(input("enter the year"))
d=sum_of_digits(dd)
m=sum_of_digits(mm)
y=sum_of_digits(yyyy)
lucky=d+m+y
while(lucky>9):
    lucky=sum_of_digits(lucky)
print(lucky)
