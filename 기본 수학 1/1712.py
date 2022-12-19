import sys
cost_var, cost_fix, cost_sell = map(int, sys.stdin.readline().split())
if cost_fix >= cost_sell:
    print(-1)
else:
    print(int(cost_var / (cost_sell-cost_fix) + 1))