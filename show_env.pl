#!/usr/bin/perl -w
for (sort keys %ENV) {
  print "$_: $ENV{$_}\n";
}
print "\$0: $0\n";
