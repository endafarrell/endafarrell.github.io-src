# endafarrell.github.io-src
Sources for personal github pages

# Here's how I use this.

1. Clearly I need to have something to say :-) It doesn't really matter what.
2. ``git pull`` in this top-level dir.
3. ``git pull`` in the ``output`` sub-dir
4. Write something in one of the ``content`` folders.
5. ``make html`` in this top-level dir
6. In a new console/terminal, ``cd`` into the ``output`` dir, ``python -m SimpleHTTPServer`` and preview the edits at
   [http://localhost:8000/](http://localhost:8000/) 
7. Rinse and repeat.
8. ``git add <whatever>`` has changed while in this top-level dir.
9. ``git commit`` and ``git push`` to capture the edits. 
    * Interestingly, this does _NOT_ update the published (on github's infra) site :-)
10. ``cd`` into ``output`` and ``git add .``, ``git push`` there too. 
    * **This** is the magic that updates the published site.

At this point, you're all good.

