n=int(input())
re=[]
while(n>=3):
    re.append(int(n%3))
    n=n//3
re.append(n)
index=len(re)-1
result=0
for i in range(len(re)):
    result=result+((3**(index-i))*re[i])

print(result)