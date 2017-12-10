#!/usr/bin/perl
#histgram_lines-minute.pl

use strict; use warnings;
use Subtitles;
die "Usage $0 <file.srt>" if (@ARGV != 1);
my ($file) = @ARGV;
open (my $fh, "<", $file) or die "Cannot open < $file: $!";
my $subtitle = Subtitles->new();
die "Cannot load:$@\n" unless $sub->load($fh);
close ($fh);

