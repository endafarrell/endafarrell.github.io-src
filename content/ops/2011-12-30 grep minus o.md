Title: "grep -o" - really quite useful
Date: 2011-12-30
Tags: grep, unix, utilities

One really quite useful command is “grep -o” - it allows you to fire off something like this:

    :::bash
    grep -o "Location supplier=\"\w*\"" locations.xml

And the output will be the phrases matching the regular expressions that start with “Location supplier=” with a double 
quoted word (\w) in the locations.xml file. :-) 

