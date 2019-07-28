know-how
########

:summary: Short gists about some topics.
:imageclass: gist
:showtoc: true
:intro: There are times I find it useful to write down short notes about things that have value beyond the here and now. So much of what I deal with is short-term that it's helpful to recap occasionally. That's what this page is, a recap of some details that may yet prove useful.


Bluetooth tethering an Edison
-----------------------------
.. figure:: {static}/images/2018/intel-edison.png
   :align: left

:when: 2018-

I use an Intel Edison computer with a communications board that gives it both wifi and bluetooth - but I kept finding
the instructions on how to tether to be kind of confusing. While the instructions are almost certainly better today,
I `wrote up my own notes </in-depth/bluetooth-tether-edison/>`_ in early 2018.

Chrome extn
-----------
.. figure:: {static}/images/2019/Chrome.png
   :align: left

:when: 2016-06

I had an itch to be able to easily find the Facebook ID for Place pages that I was visiting. You can - usually - find
the ID that the Facebook Graph API uses for a Place page by looking into the HTML source of the Facebook Place page and
recognising some patterns. It was a slow business, so I wrote this instead.

Due to my not really knowing how to set things up properly, the installation says that:

::

    It can:

    * Read and change all your data on all facebook.com site
    * Read your browsing history


And I guess it _could_, based on the permissions that I didn't properly set up, but version 1.0.4 doesn't. Except "Read
... data on ... facebook.com." of course. It does not need to read your browsing history, and it doesn't re-write nor
edit nor modify nor hide nor touch the Facebook HTML at all. And it most certainly does not in any way "change all your
data" on Facebook. I'll see about fixing these in a later version.

So: if ever getting the ID of a Facebook Place was something you wanted to do, then
`Get Facebook ID <https://chrome.google.com/webstore/detail/get-facebook-id/fakbnhhfckloijmnbpdanjeniajgjgcn?hl=en>`_
might be useful..


fish, git status
----------------
.. figure:: {static}/images/2018/fish-shell.png
   :align: left

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
.. figure:: {static}/images/2018/fish-shell.png
   :align: left

:when: 2017

I've been using git on and off for farious project for many many years, but you really only end up using the source
control systems that the project you're on is using. I was one part of a team looking at moving a large, decade-old
project from ``svn`` to ``git`` - but it didn't happen as (a) the devops processes relied on svn's incrementing revision
numbers (and the cost to rework those was very high), and (b) one (senior) member of the team claimed they needed the
ability to do "software archeology" to see who changed what when ... I believe it was a diversionary tactic to avoid the
learning curve of a new tool.

In 2016 I switched teams, one that was using ``git/gerrit`` and after months of team team I wrote a
`Gerrit survival guild </in-depth/gerrit-survival-guide/>`_ . While I'm no longer on that gerrit-backed project, I did
come away with a few ``git`` lessons:

* If you administer a git repo, ensure that only ``fast-forward`` commits are allowed to ``master``. Better that the
  conflicts are dealt-with by one dev as they incorporate changes that have already landed on master than every single
  dev having to continuously deal with bad commits.
* Always, always to ``git pull --rebase --all`` and never a bare ``git pull``. This works hand-in-hand with
  ``fast-forward-only`` commits to master.
* Regularly ``git checkout master; git pull --rebase -all`` to get recent changes from master and then
  ``git checkout {feature-branch}`` and ``git rebase master``. It's possible to rebase the remote (rather than local)
  master, but the commands become longer and more prone to not being done right every time by everyone.


gulp
----
:when: 2019-07

Frontend build tools and pipelines are unbelievably complex. I __totally__ resonate with the `Hackernoon **How it feels
to learn JavaScript in 2016** <https://hackernoon.com/how-it-feels-to-learn-javascript-in-2016-d3a717dd577f>`_ article
(which to be fair is the frontend port of something similar in the DevOps world `CircleCI's **It's The Future** article
from 2015 <https://circleci.com/blog/its-the-future/>`_) and just today I've stumbled into the differences between
``gulp 3`` and ``gulp 4`` and being stung by the pain caused when people, instructions, tutorials do not take the time
to ensure that each project has its own environment.

Watch out - and I mean go and check the syntax of calls and don't just assume - that you're not going to install
something into your "global" state - ensure that everything's in your venv, your conda, your working dir, your project
dirs and then go and fix-up the paths in whatever scripts are being run.


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
