know-how
########

:summary: Short gists about some topics.
:imageclass: gist
:showtoc: true
:intro: There are times I find it useful to write down short notes about things that have value beyond the here and now. So much of what I deal with is short-term that it's helpful to recap occasionally. That's what this page is, a recap of some details that may yet prove useful.


Bluetooth tethering an Edison
-----------------------------
:when: 2018-

I use an Intel Edison computer with a communications board that gives it both wifi and bluetooth - but I kept finding
the instructions on how to tether to be kind of confusing. While the instructions are almost certainly better today,
I `wrote up my own notes </in-depth/bluetooth-tether-edison/>`_ in early 2018.


fish, git status
----------------
:when: 2018-

I'd always been a user of the ``bash`` shell, mostly due to two of my early mentors at Sapient in Australia and the fact
that most servers will only have ``bash`` and not a whole lot else. It wasn't helped that when I did have to jump onto
a server, it was often with a shared account, and it would not be polite to start reconfiguring things on the usual
admins.

Since about 2014 all of my source control is via `git <https://git-scm.com/>`_ and to have your prompt show you what
branch you're on, how clean your branch is (with respect to the most recent pull you've made), and most importantly how
far through a rebase you are is a real benefit:

.. image:: /images/2018/git-prompt.png
   :alt: an informative prompt

Previous incarnations of this was done with ``bsah`` and ``vcprompt`` but on big projects that was noticeably slow, and
there's a better way - the `fish shell <https://fishshell.com/>`_ with its ``Classic + Vcs`` prompt.

Don't let their homepage put you off though - find a YouTube video or two to see how productive you could become if you
never had to think about what branch you've checked out and whether it's clean - you can just see it.


git
---
:when: 2017

I wrote a `Gerrit survival guild </in-depth/gerrit-survival-guide/>`_ some time ago, and while I'm no longer on that
gerrit-backed project, I did come away with a few ``git`` lessons:

* If you administer a git repo, ensure that only ``fast-forward`` commits are allowed to ``master``. Better that the
  conflicts are dealt-with by one dev as they incorporate changes that have already landed on master than every single
  dev having to continuously deal with bad commits.
* Always, always to ``git pull --rebase --all`` and never a bare ``git pull``. This works hand-in-hand with
  ``fast-forward-only`` commits to master.
* Regularly ``git checkout master; git pull --rebase -all`` to get recent changes from master and then
  ``git checkout {feature-branch}`` and ``git rebase master``. It's possible to rebase the remote (rather than local)
  master, but the commands become longer and more prone to not being done right every time by everyone.


Jupyter
-------
:when: 2017-

What a game-changer notebooks are! Trying things out, having a REPL to play with, being able to run and rerun cells, the
list is long and getting longer.

The only occasional fly in the ointment is when a new data scientist thinks, as something "sort of" works in their
notebook, that they have produced production quality code fit to be deployed live ... There's then the "educational
talk" ;-)


Let's Encrypt
-------------
:when: 2019-07

As part of launching an awesome new service, I was leading the engineering team through Security Privacy & Continuity
requirements, and front and centre was the need for the company's AAA mechanism. This is good news - thought it involved
a lot of work - as to side-step robust (and ever-strengthening0 security processes is a stupid idea.

One part of this process involved gateway servers crossing AWS VPCs and I'd wanted to have TLS from our ``nginx``
reverse proxy, and rather than using self-signed certs I chose Let's Encrypt.

Using Let's Encrypt is suposed to be easy and straight-forward, but due to other corporate limitations, our EC2
instances were not able to ``apt-get install certbot`` so I ended up checking out the certbot source code and, as it's
python, using that to get the certificates. As I (a) really did not want to open this internal server to the public
internet, and (b) have control of the Route53 for these internal servers (which I grant you is an unusual combination),
I got the ``dns-route53`` to obtain the certs.

There are many tutorials, how-tos and what not about using certbot, and you can tell that Let's Encrypt recognise the
problems that too many, and not always well-written, and soon outdated articles cause to new users.


Mermaid
-------
:when: 2018

`Mermaid <https://mermaidjs.github.io/>`_ is a very useful way of writing a form of Markdown that defines graph images
- like this:

::

    graph TD
    A[Work not going well] --> B(What's the problem?)
    B --> C[Bad assumptions]
    B --> D[Unclear scope]
    B --> E[Poor planning]
    B --> F[Misunderstanding]
    F --> G[Make it happen]
    E --> G
    D --> G
    C --> G


After you run a document with the above through Mermaid, you'll get an image like this:

.. image:: /images/2019/make-it-happen.png
   :alt: simple diagram showing how to make it happen

Being able to draw simple diagrams like this is clearly very useful when documenting software
systems and data flows. I often use `Sphinx <http://www.sphinx-doc.org/en/master/>`_ when writing
docs and it comes with a ``Makefile`` so that you can simply ``make docs`` to take your Markdown or
reStructured Text and convert it into other formats for sharing.


nginx
-----
:when: 2019-07

I'm impressed with the ease of getting an nginx service running with TLS to reverse proxy an app server. 
