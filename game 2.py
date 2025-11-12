'''
import time
k = 1
while k < 10:
    if k == 6:
        break
    print(k)
    time.sleep(0.4)
    k += 1
'''
import time
l = 0
while l < 10:
    l += 1
    if l == 6 or l == 7:
        continue
    time.sleep(0.5)
    print(l)