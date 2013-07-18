#!/usr/bin/env perl

use strict;
use warnings;

while ( my $line = <> ) {
    $line =~ s/(^\s+|\s+$)//g;
    my @keys = split(m/\s+/, $line);
    foreach my $key ( @keys ) {
        my $value = 1;
        printf( "%s\t%d\n", $key, $value );
    }
}
