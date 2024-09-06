n=int(input())
term_num = "1"
sum_of = 0
for i in range(1,n+1):
    sum_of = sum_of + int(term_num * i)
print(sum_of)