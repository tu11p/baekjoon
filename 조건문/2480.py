first,second,third=map(int,input().split())
max=first
if((first==second)&(second==third)):
    print(f'{10000+first*1000}')
elif((first==second)&(third!=first)&(third!=second)):
    print(f'{1000+first*100}')
elif ((first == third) & (second != first)&(second!=third)):
    print(f'{1000 + first * 100}')
elif ((second == third) & (first != second)&(first!=third)):
    print(f'{1000 + second * 100}')
else:
    if(second>max):
        max=second
    if(third>max):
        max=third
    print(f'{max*100}')