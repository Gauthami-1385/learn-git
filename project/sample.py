# Print all prime number in intervel
# now this change is amend to older commit
x=int(input('Enter the lower limit = '))
y=int(input('Enter the upper limit = '))

prime=[True] * (y+1)

prime[0],prime[1]=False,False

for i in range(2,int(y**0.5)+1):
    if prime[i]:
        for j in range(i*i,y+1,i):
            prime[j]=False

res=[i for i in range(x,y+1)if prime[i]]

print(res if res else 'No')
        