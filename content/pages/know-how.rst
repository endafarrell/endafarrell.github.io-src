know how
########

:date: 2019-07-26 10:44
:modified: 2019-07-26 10:44
:tags: code, skills
:slug: know-how
:authors: Enda Farrell
:summary: Short gists about some topics I have expertise in.

Jupyter
-------

2017-

What a game-changer notebooks are! Trying things out, having a REPL to play with, being able to run and rerun cells, the
list is long and getting longer.

The only occasional fly in the ointment is when a new data scientist thinks, as something "sort of" works in their
notebook, that they have produced production quality code fit to be deployed live ... There's then the "educational
talk" ;-)


Let's Encrypt
-------------

2019-07

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


nginx
-----

2019-07

I'm impressed with the ease of getting an nginx service running with TLS to reverse proxy an app server. The last
