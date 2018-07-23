title: Tidying up build server workspaces
date: 2017-09-21
tags: unix

You're not going to want to do this - but if you have to do it ...

I have a job that needs 200+ GB of disk to run. I have build servers which do have that kind of 
space, but as they are shared servers, other jobs can take some of that space, and occasionally I 
have jobs which run into the "No space left on device" problem.

Like with all build servers, it's easy to add new jobs when you need them - but we humans are not
good at removing old jobs - and more importantly their old, unused workspaces - when we've moved on
to other work - and this does mean that my 200+ GB jobs fail more often than is needed.

So: how about we remove old workspaces that are no longer needed? My definition of "no longer 
needed" is "hasn't been written to in over 30 days" - but more on that later.

First - you'll need to know when each of the workspace directories was last written to: this next
line - when run from the `/data/workspaces/` dir will give that - recursively - in a YYYY-MM-DD
format:

    for d in $(ls -1); do echo -n ${d}; find ${d} -type f -printf " %TY-%Tm-%Td\n" | sort -nr | head -n1; done;

I've found that subdirs with an @ symbol in their name causes problems, but there are not many of 
those and I want to be able to eyeball these to ensure nothing unexpected has happened. I then copy
that output into a `/tmp/jobs-last-write-dates.txt` file and fix anything that needs fixing. I then
swap them around so that I can see them in date order (which I could of course have done above, but
...)

    cat /tmp/jobs-last-write-dates.txt | awk '{print $2 " " $1}' | sort > /tmp/last-write-dates-for-jobs.txt
    
At this point in time, 2017-09-21, I wanted to remove jobs where the last write was some time ago - 
hence the first grep. The latter greps are there as a precaution against things I missed

    cat /tmp/last-write-dates-for-jobs.txt | grep '^2017-08-[01]' | awk '{print "rm -rf " $2}' | grep -v '@' | grep -v '<important-high-profile>' | sh
    
That very last `| sh` is the step you're "not going to want to do"- be careful.