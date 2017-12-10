#!/usr/bin/python
# histogram_lines-minute.py
import sys
import pysrt
if (len(sys.argv) != 2):
    raise Exception("Incorrect input")
filename = sys.argv[1]

# In this first implementation, count based on starting times
print (filename)
subs = pysrt.open(filename)
sub_count = {}
last_minute = 0
for sub in subs:
    start_minute = sub.start.minutes
    if (start_minute not in sub_count.keys()):
        sub_count[start_minute] = 1
    else:
        sub_count[start_minute] += 1
    last_minute = start_minute
total = 0
print("Minute\tFrames")
for i in list(range(last_minute+1)):
    if (i not in sub_count.keys()):
        sub_count[i] = 0
    j = sub_count[i]
    print ('{key}\t{value} {stars}'.format(key = i, value = j, stars = j*'+'))
    total += j
print('Total: {somme}'.format(somme = total))
