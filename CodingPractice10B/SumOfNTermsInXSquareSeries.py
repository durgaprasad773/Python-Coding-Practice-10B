x=input()
n=int(input())
sum_of = 0
for i in range(1,n+1):
    sum_of = sum_of + (int(x*i) ** 2)
print(sum_of)