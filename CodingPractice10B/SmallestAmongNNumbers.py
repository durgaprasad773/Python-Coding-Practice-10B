n=int(input())
first_num = int(input())
small_num = first_num
for i in range(n-1):
    num = int(input())
    if num < small_num:
        small_num = num
print(small_num)