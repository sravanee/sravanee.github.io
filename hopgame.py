n=int(input())
a=list(map(int,input().split(',')))
dp=[[0,0,0] for _ in range(n+1)]
for i in range(1,n+1):
    dp[i][0]=max(dp[i][0],dp[i-1][-1]+a[i-1])
    dp[i][1]=max(dp[i][1],dp[i-1][1]+a[i-1])
    if i-2>=0:
        dp[i][0]=max(dp[i][0],dp[i-2][-1]+a[i-1]*2)
        dp[i][1]=max(dp[i][1],dp[i-2][1]+a[i-1]*2)
    if i>=3:
        dp[i][2]=max(dp[i][2],dp[i-3][1]+a[i-1]*3)
print(max(dp[-1]))
