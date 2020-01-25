# endafarrell.github.io-src

Sources for personal github pages

## Here's how I use this.

1. Clearly I need to have something to say :-) It doesn't really matter what.
2. ``conda activate pelican``
3. ``git pull`` in this top-level dir.
4. ``git pull`` in the ``output`` sub-dir
5. Write something in one of the ``content`` folders.
6. ``make html`` in this top-level dir
7. In a new console/terminal, ``cd`` into the ``output`` dir, ``python -m SimpleHTTPServer`` and preview the edits at
   [http://localhost:8000/](http://localhost:8000/)
8. Rinse and repeat.
9. ``git add <whatever>`` has changed while in this top-level dir.
10. ``git commit`` and ``git push`` to capture the edits. 
    * Interestingly, this does _NOT_ update the published (on github's infra) site :-)
11. ``cd`` into ``output`` and ``git add .``, ``git push`` there too.
    * **This** is the magic that updates the published site.

At this point, you're all good.

## Darken and Compress Images

https://pinetools.com/darken-image
https://compressor.io/compress
https://compress-or-die.com/webp-process?scale=100&trim=0&quality=75&alpha_quality=80&sharpness=0&extreme_compression=1

