Title: Bluetooth tethering an Edison
Date: 2018-06-29
Tags: insulin, pump, diabetes, openaps, bluetooth
Summary: Bluetooth tethering an Edison

There are good instructions on how to tether an Edison to Bluetooth in the 
[docs](https://openaps.readthedocs.io/en/latest/docs/Customize-Iterate/bluetooth-tethering-edison.html)
but I've found them a little difficult to follow, and I'm not certain that it worked "as is" for me,
so here's my version.

-2: Comment-out the local WiFi from ``/etc/wpa_supplicant/wpa_supplicant.conf``. The rig prefers 
WiFi over BT - a decision I very much agree with - but you'll need to ensure that you don't have any
WiFi going on for a while until you get this sorted out.

-1: ``bluetoothd --version`` If you don't have the correct ``bluetoothd`` you're going to be in 
trouble and will have to reflash the machine. Go and rebuild the rig.
 
0: Get the MAC of the phone's BT. Mine's  ``98:0D:2E:D8:59:73``.

1: ``reboot``. Best start off fresh.

2: ``service cron stop``. The OpenAPS crontab has lots, and it runs a lot every minute. You don't 
want them interfering.

3: ``ifconfig wlan0 down``. To get the rig to connect over Bluetooth, it's best if you don't have a 
WiFi connection there already. You can confirm that the WiFi is down with ``ifconfig``: 

    root@erig0:~# ifconfig
    lo        Link encap:Local Loopback
              inet addr:127.0.0.1  Mask:255.0.0.0
              UP LOOPBACK RUNNING  MTU:65536  Metric:1
              RX packets:0 errors:0 dropped:0 overruns:0 frame:0
              TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
              collisions:0 txqueuelen:0
              RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)
    
    usb0      Link encap:Ethernet  HWaddr 02:00:86:cf:e9:d8
              inet addr:10.11.12.13  Bcast:10.11.12.255  Mask:255.255.255.0
              UP BROADCAST MULTICAST  MTU:1500  Metric:1
              RX packets:0 errors:0 dropped:0 overruns:0 frame:0
              TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
              collisions:0 txqueuelen:1000
              RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)

What you don't see here is a ``wlan0`` interface.

4: ``killall bluetoothd``. Stop any existing bluetooth daemons. Repeat every few seconds until you 
see:

    root@edison:~# killall bluetoothd
    bluetoothd: no process found
    
Now there's none running.

5: ``hciconfig hci0 name $HOSTNAME``. Rename your bluetooth to be the name of your rig. My 
``$HOSTNAME`` is ``erig0`` - and that's what I expect to see in a few places here.

6: ``/usr/local/bin/bluetoothd &`` Start the bluetooth daemon. Wait a few seconds.

7: ``bluetoothctl`` Launch the bluetooth controller. You're going to stay in here for a bit, and to
help make that clear, I'll rename these points 7.1, 7.2 etc etc. When I launched ``bluetoothctl`` I 
saw this:

    [NEW] Controller 58:A8:39:01:D5:E0 erig0 [default]
    [NEW] Device 98:0D:2E:D8:59:73 Noncompliant
    Agent registered

I _suspect_ that this means that the rig already "knows" about my phone's Bluetooth (the 
98:0D:2E:D8:59:73 is indeed the phone). I want to be able to ensure that I'm setting up everything
cleanly, and have it repair nicely, so I first remove it: ``remove 98:0D:2E:D8:59:73`` which results 
in:

    [bluetooth]# remove 98:0D:2E:D8:59:73
    [DEL] Device 98:0D:2E:D8:59:73 Noncompliant
    Device has been removed
    
I then ``quit`` and restarted ``bluetoothctl``:

    bluetoothctl
    [NEW] Controller 58:A8:39:01:D5:E0 erig0 [default]
    Agent registered
    
This is the state I wanted to find things in.

7.1 ``discoverable on``:
    
    [bluetooth]# discoverable on
    Changing discoverable on succeeded
    [CHG] Controller 58:A8:39:01:D5:E0 Discoverable: yes

7.1.1 On your phone you should rescan and see the newly discoverable device named ``erig0``. Don't 
click on it yet though.

7.2 ``agent on``: Should say ``Agent is already registered``.

7.3 ``default-agent``: Should say ``Default agent request successful``

7.4 Pair from the phone by clicking on the ``erig0`` icon. 

7.4.1: When prompted on the rig, check that the numbers are correct and type ``yes``

7.4.2: Afterwards, click "Pair" on the phone.

Afterwards, you'll see a lot of ``UUID`` inco and then:
    
    [CHG] Device 98:0D:2E:D8:59:73 Paired: yes
    [CHG] Device 98:0D:2E:D8:59:73 ServicesResolved: no
    [CHG] Device 98:0D:2E:D8:59:73 Connected: no

7.5 ``paired-devices``: Confirm the phone is paired (from the rig's perspective):
      
      [bluetooth]# paired-devices
      Device 98:0D:2E:D8:59:73 Noncompliant
      
7.6 ``trust 98:0D:2E:D8:59:73``: Allow the rig to trust the phone.

    [bluetooth]# trust 98:0D:2E:D8:59:73
    [CHG] Device 98:0D:2E:D8:59:73 Trusted: yes
    Changing 98:0D:2E:D8:59:73 trust succeeded

7.7 ``quit``: Leave the bluetooth controller.

8: ``bt-pan client 98:0D:2E:D8:59:73``: See that the phone has a bluetooth connection now.

9: ``dhclient bnep0``: Get an IP. 
    
    root@erig0:~# ifconfig bnep0
    bnep0     Link encap:Ethernet  HWaddr 58:a8:39:01:d5:e0
              inet addr:192.168.44.151  Bcast:192.168.44.255  Mask:255.255.255.0
              UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
              RX packets:46 errors:0 dropped:0 overruns:0 frame:0
              TX packets:41 errors:0 dropped:0 overruns:0 carrier:0
              collisions:0 txqueuelen:1000
              RX bytes:4176 (4.0 KiB)  TX bytes:3386 (3.3 KiB)
          
Good. Verify with ``curl http://checkip.amazonaws.com/``

10: ``reboot``. Amongst other things, this will clean up temporary state and will check that all is
well with the configurations. 

11: Check that all is well. Wait a while. Check your Nightscout. Give it about 10 minutes to sort 
everything out.

12: _Eventually_ you can revert the commenting-out of the local WiFi from step -2 above.
