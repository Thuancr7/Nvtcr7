#Bai1
a = "Ngo Van Thuan K14"
count={}
for i in a:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
print(count)

#Bai2
def sapxep(list):
    list = [10,5,8,2,3,9,1,99]
    list.sort()
    return list
print(sapxep(list))

#Bai3
a = ['abc','123',2,3,5,6]
sosanh = a
a[0] = 0
if sosanh == a:
    print(' Khong bi thay doi')
else:
    print(' CO bi thay doi')

#Bai4
def xuat_mang(a):
    for i in range(len(a)):
        dem = 0
        for j in range(len(a)):
            if a[i] == a[j] and i != j:
                dem += 1
        if dem == 0:
                print(a[i])
    return a[i]
xuat_mang(a = [1,2,1,5,9,2,7,6,5])  
