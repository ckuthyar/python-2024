list1=[]
qty=int(input("Enter quantity of numbers to be entered Eg. 5 "))
for i in range(0,qty,1):
    n1=int(input("Enter a number "))
    list1.append(n1)
print(list1)
sum1=sum(list1)
len1=len(list1)
avg1=sum1/len1
print(sum1,len1,avg1)
