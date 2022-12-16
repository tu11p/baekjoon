buy_all = int(input())
buy_type = int(input())
sum_price = 0

for i in range(0, buy_type):
    price,count = map(int, input().split())
    sum_price = sum_price + price * count

if(sum_price == buy_all):
    print("Yes")
else:
    print("No")