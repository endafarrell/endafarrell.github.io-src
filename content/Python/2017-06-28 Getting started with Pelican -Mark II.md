Title: Getting started with Pelican - Mark II
Date: 2017-06-28 20:20
Category: Python
Tags: pelican, publishing, blog, "github pages"

It's been a year since my original [Getting started with Pelican](../../2016-05-08/getting-started-with-pelican/) post and 
clearly I didn't write at all - why not?

Part of it was that I'd little interesting to say, but part was that I had trouble with how I had Pelican set up and with
how I published to github. I'd started using plugins - a good thing - but I foolishly started to customise them in their
installed location and not in a source-code-managed local subdirectory. If I was only ever going to publish from that one
machine then I'd have gotten away with my foolishness, but I wanted to/needed to blog both from home and the office - yet
my Pelican code was different and I didn't have a way of keeping them in sync.

I _could_ have fixed that problem by moving the code to a plugins sub-directory, but there was something else too that 
bothered me. It still bothers me to be honest, but I don't know if the fault is mine, github's, writers of other "how to
publish Pelican sites on github pages" articles - or most likely - a combination of all.

Instead of one endafarrell.github.io repository with different branches - the route I'd tried to use (with some limited 
success) _ I now use two different repos and gitmodules.

The short version is that I have <https://github.com/endafarrell/endafarrell.github.io-src> to hold the sources - the 
content, the theme, the plugings and settings. This is my "here I do work" repo. In the (Pelican standard) output folder
I have my output directory as a git(sub)module to <https://github.com/endafarrell/endafarrell.github.io>:

    efarrell:endafarrell.github.io-src$ cat .gitmodules
    [submodule "output"]
    	path = output
    	url = git@github.com:endafarrell/endafarrell.github.io.git
    	ignore = all

All thanks - and quick write-ups that are both useful and readable - for this goes to:

* <http://mathamy.com/migrating-to-github-pages-using-pelican.html>
* <http://hernantz.github.io/how-to-publish-a-pelican-site-on-github.html>
* <https://fedoramagazine.org/make-github-pages-blog-with-pelican/>


Other sites with advise I'd like to take are:

* <http://cyrille.rossant.net/pelican-github/> 
* <http://nafiulis.me/making-a-static-blog-with-pelican.html>


