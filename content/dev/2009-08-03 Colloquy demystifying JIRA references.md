Title: Colloquy demystifying JIRA references
Date: 2009-08-03 20:20
Tags: Perl, bbc-forge, mac, unix, work, applescript, jira, Colloquy


The BBC’s Forge engineering team uses an IRC channel to hold meetings. It allows our team to not bother about exactly 
where everyone is - some folks work from home, people are (mostly) in the office, but can be in different parts of 
our buildings for all sorts of good reasons. So, we have JIRA instead of Agile “task cards” and we use IRC meetings 
instead of “standups”.

Link in any team, you’ll have some folks working on one aspect of the development, others on others. There’s an 
“idealisation” in many Agile software disciplines that suggests any developer can work on any task, yet this isn’t 
always so. Moreover, once someone is working on an aspect, the rest of the team are probably not going to stay on 
top of all of the JIRA references - yet in IRC we often just list those JIRA numbers to speed ourselves along.

It’s not at all difficult to link to these references but it takes quite a bit of discipline - and in fairness, I’d 
sooner be concentrating on what folks are saying rather than playing with URLs - hence a new plugin script for 
Colloquy that helps.

This script works with a small shell script that handles regex (there is an AppleScript plugin that can do this, but 
it’s not really needed for this) to identify a likely JIRA reference and to print out the title of the JIRA ticket.

First that little shell script:

    :::perl
    #!/opt/local/bin/perl
    $LINE = shift;
    my $JIRAREF = "";
    if ( $LINE =~ m/(\w+\-\d+)/ ) {
        $JIRAREF = $1;
    }
    print $JIRAREF;

As you can see it does very little - it finds strings like “FSRV-102”, or “KV-1” and prints it out, otherwise it 
outputs nothing. Quite simple.

Second the AppleScript Colloquy plugin script:

    :::applescript
    property scriptInitialPath : null
    property loadedScriptName : ""
    
    using terms from application "Colloquy"
    on process incoming chat message msg in msgChatRoom
   
        set frontRoom to description of active panel of front window
        -- to convert a chat room's name to a chat room's description, here's what
        -- I needed to do. Depending on how you connect, you may need to change
        -- this a little. You'll know that you do need to change this if you keep
        -- getting JIRA titles when your "front room" fills with unexpected JIRA
        -- titles! (Then again, perhaps you'd like to know what's being talked
        -- about and don't mind too much ...)
        set msgChatRoomName to "Chat Room #" & name of msgChatRoom & " (127.0.0.1)"
        
        -- check that the message we're processing is on our front panel
        if msgChatRoomName is equal to frontRoom then
            try
                -- the message is a class - not the text, so we have to extract it
                set thisMessage to HTML of msg
                -- I have a shell script that does the pattern matching. There is
                -- an extension to AppleScript that allows for this sort of work,
                -- but the Forge community is good with a little Unix and probably
                -- don't mind installing a script.
                -- The quotes are necessary as sentences often have spaces ...
                set jiraRef to do shell script "~/jiraRef.pl \"" & thisMessage & "\""
                -- call our separate method to handle this
                getJira(jiraRef)
            on error
                -- annoyingly, AppleScript often fails silently - and I've not
                -- actually seen this run.
                tell active panel of front window
                    add event message "error caught: " & errorMessage
                end tell
            end try
        end if
    end process incoming chat message
    
    on process user command cmd with args for chatRoom    
    -- This may be useful as it allows me to check jira refs
    if cmd is equal to "jira" then
        set jiraLine to args
        set jiraRef to do shell script "~/jiraRef.pl \"" & args & "\""
        getJira(jiraRef)
    end if
    
    end process user command
    
    -- I'm sure that in the future I'll add extra parameters to this so
    -- that I can get things like when it was last updated, the status
    -- and who perhaps last commented. But for now it's simple.
    to getJira(jiraRef)
        if jiraRef is not equal to "" then
            -- this next ommand is long - I might write this into a seperate
            -- script. But again, for now it works and allows me flexibility
            set jiraTitle to do shell script \
                "curl --cert --pass -k https://JIRA-SERVER/browse/" & jiraRef & " \
                | grep '<title>' | sed 's/title/em/g' | sed 's/ - BBC JIRA//'"
            tell active panel of front window
                --add event message jiraTitle with name "jiraTitle"
                add event message "JIRA " & jiraTitle
                --add event message "
                & "\">" & jiraTitle & "" with name "jiraTitle"
            end tell
        end if
    end getJira
    
    on load from scriptPath
        set scriptAlias to (POSIX file scriptPath) as alias
        set loadedScriptName to (name of (info for scriptAlias))
        
        set msg to (loadedScriptName & " Loaded /jira") as string
        set evt to (loadedScriptName & "loaded") as string
        tell active panel of front window
            add event message msg with name evt
        end tell
    end load
    
    on unload
        set msg to (loadedScriptName & " Unloaded") as string
        set evt to (loadedScriptName & "unloaded") as string
        tell active panel of front window
            add event message msg with name evt
        end tell
        set loadedScriptName to ""
    end unload
    
    end using terms from

So, this script - when placed in your ```~/Library/Application Support/Colloquy/PlugIns``` will look at incoming 
messages in your front window (in a hack-tastic way), get the first of the JIRA references (if any), looks at our 
JIRA-SERVER to find the title of these references. The code could do with quite a bit of tidy-up, but it works and for 
the speed at which our team’s messages comes in, it’s fast enough.
