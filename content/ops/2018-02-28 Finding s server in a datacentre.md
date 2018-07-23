title: Finding a server in a datacentre
date: 2018-02-28
tags: unix, nmap

At work, we're in the process of moving datacentres and some of my (extensive) monitoring needs to be updated. In 
particular, I have a monitor on Hadoop jobs which looks for job names of a specific pattern and posts them to a 
TeamUp calendar so that we can see what's running where. Over the weekend, the old datacentre's Hadoop job-trackers were
shut down - now my monitor is complaining that it can't connect. 

The datacentre migration does not have a central documentation location showing the URLs of old and new (for reasons
I cannot understand, the ops people decided to change the hostnames in a way that does not allow for any kind of mapping
from old to new), so now I need to find the server running the job-tracker in the new datacentre. The main clue I had is
that it's running on port 50030.

    nmap -p 50030 10.xxx.yyy.0/24 |\
     grep -B4 "50030/tcp open" 
     
Luckily, ``nmap`` is still available, and I have an account on a server in the datacentre, so the hardest part was 
removing the ``nmap`` entries for servers where the port was closed: the ``grep``.