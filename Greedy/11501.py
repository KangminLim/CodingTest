def get_profit(n,price):
    profit = 0
    max_price = price[-1] 
    for i in range(n-2,-1,-1):
        if max_price < price[i]:
            max_price = price[i]
        else:
            profit += max_price - price[i]
    print(profit)
    
t = int(input())
for _ in range(t):
    n = int(input())
    price = list(map(int,input().split()))
    get_profit(n,price)