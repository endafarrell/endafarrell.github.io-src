Title: Piping content through SSH
Date: 2011-12-08
Tags: proxy, ssh, unix, utilities
 
Thanks to [http://www.contentwithstyle.co.uk/content/4-ssh-config-tips-for-faster-remote-working/]() I can avoid 
creating files which need to be scp’d: I can pipe the content directly:

    :::bash
    local$ cat localfile.txt | ssh remote "cat - >> remotefile.txt"

For this to work, I have already got “remote” set up in my ```~/.ssh/config```. You can get much more involved in this: 
see

* [http://backdrift.org/transparent-proxy-with-ssh]()
* [http://www.cyberciti.biz/faq/howto-use-tar-command-through-network-over-ssh-session/]()
* [http://scratching.psybermonkey.net/2011/02/ssh-how-to-pipe-output-from-local-to.html]()

My favourite example from the last site (execute commands on remote server but save the output to local) is:

    :::bash
    ssh user@example.com "mysqldump -u DB_username -pDB_password DB_name | gzip -c" > /local/dir/DB_backup.gz



 