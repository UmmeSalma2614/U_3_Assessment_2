# Take 10 integers from keyboard using loop and print their average value on the screen

n=input("enter any numbers:")
num=n.split()
print("\n")
print("enter all numbers",num)
sum=0
for i in num:
	sum+=int(i)
print("sum of numbers",sum)
avg=sum/len(num)
print(avg)