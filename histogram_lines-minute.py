#!/usr/bin/python
# histogram_lines-minute.py
import sys
import pysrt
if (len(sys.argv) != 2):
    raise Exception("Incorrect input")
filename = sys.argv[1]
#For the above command is there a perl-like operation like
#my ($filename) = @ARGV; ?

#In this first implementation, count based on starting times
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
Sum = 0
print("Minute\tFrames")
for i in list(range(last_minute+1)):
    if (i not in sub_count.keys()):
        sub_count[i] = 0
    j = sub_count[i]
    print ('{}\t{} {}'.format(i, j, j*'+'))
    Sum += j
#print("Total: " + repr(Sum))
print('Total: {}'.format(Sum))
