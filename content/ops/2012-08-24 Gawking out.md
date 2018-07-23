Title: Gawking out
Date: 2012-08-24
Tags: work, awk, unix, ops, gawk


![awk logo]({filename}/images/gawking-out.jpg){:style="float: left; margin-right: 7px;"} I've been 
processing log files recently to see how a live system is 
being used. When you have millions of hits daily, you need these processors to be fast.

Today the best way is to have your log files shipped over onto a Hadoop cluster and map-reduce them: but sometimes 
there's still a call for quick scripts. Here awk is a king :-)

## Converting to a HTML table
I couldn't find a decent online version of converting a CSV into a HTML table - but with awk it's easy. Here's the 
awk script:

    :::awk
    BEGIN {
        print "<table>" HDR;
    } { 
        printf "<tr>";
        for (i=1; i <= NF; i++) {
            printf "<td>%s</td>", $i;
        }
        print "</tr>";
    } END {
        print "</table>";
    }

This makes use of the field separator handling of awk: so a CSV can be converted into a simple HTML table like this:

    :::bash
    cat stats.csv |\
    awk -F',' -f 2Table.awk \
    --assign HDR="<tr><th>A>/th>...</tr>" > stats.html


## Summing distinct rows
So the best way to describe this is to show an example:
    
    :::raw
    IP1 GET url1 200 32
    IP2 GET url1 200 29
    IP1 GET url1 200 21

The "distinct rows" here would be "IP1 GET url1 200" and "IP2 GET url1 200". You could think of these as just a few 
entries of the access_logs. Anyway, I wanted to sum together the times that these calls were taking (the last column). 
Sometimes the number of fields varied so a general solution was needed.

The desired output is:

    :::raw
    IP1 GET url1 200 53
    IP2 GET url1 200 29

and the script to do this is:

    :::gawk
    {
        # Grab the value
        num = 0 + $NF; 
        # Strip the value - $0 no longer has the value
        NF--;
        # Increments the value at hash[$0] or creates it
        # if not already present.
        hash[$0] = hash[$0] + num
    }
    END {
        for (ndx in hash) {
            print ndx,hash[ndx];
        }
    }
