title: Gerrit survival guide
date: 2018-04-11


At work, some of our projects use gerrit. It's different to git and to github, and we didn't get the right kind of 
training on howto use  it. This is a self-assembled survival guide. If you can articulate the differences between a 
``merge`` and a ``rebase`` then this is not for you!

Initial checkout
----------------

Your initial checkout should look something like this:

``git clone ssh://you@gerrit.hostname:29418/project/sub-project
&& scp -p -P 29418 you@gerrit.hostname:hooks/commit-msg sub-project/.git/hooks/``
            
You should then find yourself on the ``master`` branch.

You want to do some work
------------------------

Create a local branch to do your work. Always. Do not create a remote branch - it's almost never worth it, and if you're
reading this, you're doing the wrong thing ;-)

``git checkout -b BUG-1234 origin/master``
    
This creates, and checksout, a new branch called BUG-1234 based on the current master.

Do some work. Add, edit, delete some code. Then do the **first** checkin:

``git add <changes>``

``git commit``
    
Give your description. Now you might do some more work.

``git add <new-changes>``

``git commit --amend``
    
The *core concept* in gerrit *seems* to be that you only push a **single** commit. This means you need to modify/amend 
any pre-existing commits. gerrit itself sorts out the patch-sets when you push them, but you need to ``--amend`` locally 
when making your changes.

If it's been a while since you created the local branch, the origin/master may have changed. **REBASE** and **NEVER 
MERGE**:

``git pull --rebase``
    
When you ``merge`` you'll have a merge commit, that then means you have multiple commits. There _are_ ways of dealing 
with this, but if you're reading this survival guide, they're not for you ;-)

If you have conflicts, fix them.

Finally, you've rebased, you're happy with both your changes and commit message: time to send your code to be reviewed:

``git push origin HEAD:refs/for/master``
    
Then, go fix up some reviewers, with at least one who has ``+2``, and await feedback.


You have feedback from your reviews
-----------------------------------
Checkout your under-review branch. If you used a name like ``BUG-1234`` this will be easy:

``git checkout BUG-1234``
    
Then, edit based on the feedback and treat these edits as "more work" on this branch. That means:

``git add <review-changes>``

``git commit --amend``
    
Update, if necessary, your commit message, but **leave the ChangeId alone**! Then, when ready:

``git push origin HEAD:refs/for/master``
    
Gerrit itself sorts out the patchsets - but you'll need to redo the reviewers sometimes.


You want to review someone else's work
--------------------------------------
Someone's asked you to review - best get it locally and see that it's up-to-snuff!

* ``git checkout master`` (having first ensured that your git env is clean)
* Find the "**Download Checkout**" link on the gerrit UI.
* Paste that command at teh root of your checkout.
* ``git checkout -b change-owner-bug-number``  (so that you can tell who this code came from)

Here you get to see the changes. If you want you _could_:

* Make changes yourself
* ``git add <your-changes>``
* ``git commit --amend``
* ``git push origin HEAD:refs/for/master``

That will create another patchset for that review.

Survival!
---------
With this cheatsheet, your changes of survival have gone way up. Gerrit seems to work best when you have local branches.
You need for everything to be a *single commit*, but don't try squashing - always use ``--amend``. Never do a ``merge``
either -- always use ``git pull --rebase``. Some teams seem to have success when they configure their IDEs to run these
commands, but I have personally seen too many cases where terrible commits were included because of this - so always use 
the ``git`` CLI :-)


