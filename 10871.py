import sys
seq_idx, stnd = map(int,sys.stdin.readline().split())
seq = list(map(int,sys.stdin.readline().split()))
for i in range(0, seq_idx):
    if(seq[i]<stnd):
        print(f'{seq[i]} ', end="")