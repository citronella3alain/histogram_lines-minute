#!/usr/bin/env python3
# histogram_lines-minute.py
import sys
import pysrt
if (len(sys.argv) != 2):
    raise Exception("Incorrect input")
filename = sys.argv[1]
#For the above command is there a perl-like operation like
#my ($filename) = @ARGV; ?

#In this first implementation, count based on starting times
print (filename + "\n")
subs = pysrt.open(filename)
sub_count = {}
for sub in subs:
    if (sub.start.minutes not in sub_count.keys()):
        sub_count[sub.start.minutes] = 1
    else:
        sub_count[sub.start.minutes] += 1
Sum = 0
print("Minute\tFrames")
for i, j in sub_count.items():
    print(repr(i) + " \t"+ repr(j)+ " " + j*"+");
    Sum += j
print("Total: " + repr(Sum))
