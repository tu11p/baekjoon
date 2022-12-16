import sys

fir_num, sec_num = sys.stdin.readline().split()
rev_fir_num = fir_num[::-1]
rev_sec_num = sec_num[::-1]
if rev_fir_num > rev_sec_num:
    print(rev_fir_num)
else:
    print(rev_sec_num)
