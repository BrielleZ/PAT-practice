# B1008
n, mov = map(int, input().split())
mov = mov % n
num = input().split()
if mov == 0:
    num_new = num
else:
    num_new = num[-mov:] + num[:n - mov]
print(' '.join(num_new))