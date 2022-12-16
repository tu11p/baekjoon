daily_up, daily_down, height = map(int, input().split())

if (height - daily_up) % (daily_up - daily_down) == 0:
    print((height - daily_up) // (daily_up - daily_down) + 1)
else:
    print((height - daily_up) // (daily_up - daily_down) + 2)
