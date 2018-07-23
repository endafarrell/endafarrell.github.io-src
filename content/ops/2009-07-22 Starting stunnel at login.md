title: Running stunnel at startup
date: 2009-07-22
tags:  mac, ops, unix, work

You might want your stunnels to be running all the time - and to start automatically when you log in. Here’s how:

  * get your stunnel working. You’ll need to fix your certs, choose the correct ports, and all that yourself.
  * write a script (/Users/you/stunnel.sh) that’s just like this:

    #!/bin/sh
    /opt/local/bin/stunnel /opt/local/etc/stunnel/stunnel.conf

  * in a terminal window write this:

    sudo defaults write com.apple.loginwindow LoginHook /Users/you/stunnel.sh

Now you’re all set. Next time you login, the LoginHook will fire, running your “stunnel.sh” command which in turn calls 
(with full paths) the stunnel config you’ve got set up.

<http://support.apple.com/kb/HT2420> has more info about creating LoginHooks

