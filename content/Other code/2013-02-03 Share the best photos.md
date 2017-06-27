title: Note to self: sharing the best photos
date: 2013-02-03
tags: photos, rsync, library, manage, aperture, nas

We take quite a few photos and I'm forever reinventing how I look after them. Here's where I am at at the moment:

  * Photos come from a few different cameras
  * Aperture (now 3.2.4) is what we use to manage them
  * All photos/videos are imported
  * Good ones get a 3 start rating, very good a 4 and the best a 5.
  * Rejected, one and two star photos are deleted - unrated get to live for another day
  * I export full size JPGs to my ~/Pictures/ApertureExports into subdirectories for each year.
  * After exporting I use (the very excellent) [exiftool](http://www.sno.phy.queensu.ca/~phil/exiftool/)
    to change the ctime of the file to be the photos's Original Datetime: (see the code block below)
  * I have a [ReadyNAS](http://www.readynas.com/?cat=3) server for backups.
  * I mount the NAS and rsync the exports: (see the code block below)


    exiftool "-filemodifydate<datetimeoriginal" .
     
    rsync -rv --delete --progress --times \
        /Users/Shared/ApertureExports/ \
        /Volumes/nasmedia/Pictures/BestApertureExports/

