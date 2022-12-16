a,b=map(int,input().split())
c=int(input())

#1차
#if((a==23)&(60<=(b+c)<120)):
#    print(f'0 {(b + c) % 60}')
#else:
#    print(f'{a+(int((b+c)/60))} {(b+c)%60}')

#2차
#if(((a==23)|(a+(int((b+c)/60))==0))&(60<=(b+c)<120)):
#    print(f'0 {(b + c) % 60}')
#else:
#    print(f'{a+(int((b+c)/60))} {(b+c)%60}')

if(((a==23)&(60<=(b+c)<120))|(a+(int((b+c)/60))==24)):
    print(f'0 {(b + c) % 60}')
elif(a+(int((b+c)/60))>24):
    print(f'{a+(int((b+c)/60))-24} {(b+c)%60}')
else:
    print(f'{a+(int((b+c)/60))} {(b+c)%60}')