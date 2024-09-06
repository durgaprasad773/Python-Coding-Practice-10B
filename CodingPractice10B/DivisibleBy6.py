m=int(input())
n = int(input())
res=""
for i in range(m,n+1):
    if i % 6 == 0:
        res = res + str(i)+" "
if len(res) > 0:
    print(res)
else:
    print("No Numbers Found")