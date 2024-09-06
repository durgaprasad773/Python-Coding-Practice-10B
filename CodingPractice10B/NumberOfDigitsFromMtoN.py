m=int(input())
n=int(input())
count = 0
for i in range(m,n+1):
    s = len(str(i))
    count = count + s
print(count)