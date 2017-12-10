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

subs = pysrt.open(filename)
sub_count = {}
for sub in subs:
    #print("Start", sub.start.minutes, "\t", sub.end.minutes, "\n")
    sub_count[sub.start.minutes] += 1

for
