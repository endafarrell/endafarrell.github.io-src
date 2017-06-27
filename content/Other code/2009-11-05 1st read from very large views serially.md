Title: CouchDB 0.9x - 1st read from v large views serially
Date: 2009-11-05 20:20
Tags: bbc-forge, CouchDB, work, NoSQL, how-to

On a server, we run 4 different CouchDB nodes, each with 30 or so databases. We can therefore have over 100 databases - 
and if you’re reading from large views - or view over large databases - you will need to do so serially.

We have 4 as “normally” CouchDB is kind re it’s use of memory, and kind in terms of CPU usage (we have 8-core machines 
here). Yes - there is a headache re being disk-IO bound, but it’s not normally a problem.

But views are now needed (to identify conflicting docs) as we have many applications using our KV service in both of 
our datacentres. And adding them is not straight-forward.

In the docs, you’ll see that a view is no more than a “special” document, so “creating” them is indeed 
straight-forward. What’s not in the docs (yet at least) is that if you’re going to add a view to a large database, 
you’re going to need to have PLENTY of memory. Last night we ran into “eheap_alloc” which took down each of the nodes.

So - you gotta take your time, and do them serially.

Unfortunately, the first read of a view over a very large database can take some time. Even a 70 thousand doc 8 GB 
database can take 2 to 4 hours to build even a simple view (which led to the code that added and read them in 
parallel) - go give yourself many days.
 

Here’s what top looks like mid-1st read:

    :::bash
    top - 15:05:54 up 71 days, 17:26, 1 user, load average: 1.02, 1.04, 1.04
    Tasks: 147 total, 1 running, 146 sleeping, 0 stopped, 0 zombie
    Cpu(s): 11.5%us, 1.7%sy, 0.0%ni, 86.9%id, 0.0%wa, 0.0%hi, 0.0%si, 0.0%st
    Mem:  16438912k total, 16331660k used,   107252k free,    19048k buffers
    Swap: 16771820k total,  8493532k used,  8278288k free,  6754524k cached
     
      PID USER      PR  NI  VIRT  RES  SHR S %CPU %MEM    TIME+  COMMAND
     8893 couchdb   18   0 15.6g 7.8g 1944 S    0 49.6  13:53.09 couchjs
     2790 couchdb   25   0  357m 132m 4180 S    0  0.8  76:06.97 beam.smp
     2843 couchdb   25   0  342m 167m 4116 S   86  1.0  81:54.23 beam.smp
     2896 couchdb   25   0  175m  17m 3896 S    0  0.1   0:06.73 beam.smp
     2949 couchdb   25   0  171m  14m 3744 S    0  0.1   0:06.03 beam.smp
    32320 couchdb   18   0  150m 105m 1948 S   15  0.7  13:36.61 couchjs

