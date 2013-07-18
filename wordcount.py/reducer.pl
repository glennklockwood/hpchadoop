#!/usr/bin/env perl

use strict;
use warnings;

my ($last_key, $this_key, $running_total);

while ( my $line = <> )
{
    my $value;
    $line =~ s/(^\s+|\s+$)//g;
    ( $this_key, $value ) = split( m/\t/, $line, 2 );

    if ( $last_key && $last_key eq $this_key ) {
        $running_total += $value;
    }
    else {
        if ( $last_key ) {
            printf( "%s\t%d\n", $last_key, $running_total );
        }
        $running_total = $value;
        $last_key = $this_key;
    }
}
 
if ( $last_key eq $this_key ) {
    printf( "%s\t%d\n", $last_key, $running_total );
}
