n=int(input())
a=list(map(int,input().split()))
mod=1000000007

t=sum(a)
ans=0
for v in a:
    t-=v
    ans+=(v*t)%mod
    ans%=mod

print(ans)


