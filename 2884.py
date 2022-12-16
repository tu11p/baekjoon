a,b=map(int,input().split())
if(b>=45):
    print(f'{a} {b-45}')
elif(a==0):
    print(f'23 {b+15}')
else:
    print(f'{a - 1} {b+15}')