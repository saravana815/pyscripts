
easyexpect
==========

        This tool is a modified version of original autoexpect script written by Don Libes.
        
        This tool can capture the interactive execution of commands telnet, SSH, etc and produces a script which replays the interactive session.


Changes to new tool
-------------------

    * Prompt mode check enabled by default. 
      The resulting script will check only for the prompt as end of command output match instead of whole show command output.
      This way script runs very reliable compared to script generated to autoexpect
    * The show command output verification
      Complete line match and delimited string match. Pass/Fail log messages upon output checks
    * Log file generation of when running interactive script. Log files named as script_logs_*.txt



git checkout
------------

  * git clone git@wwwin-gitlab-sjc.cisco.com:sargandh/easyexpect.git
      
 
Usage:

[sargandh:bgl-ads-1214]$ ./easyexpect -h

Usage  : ./easyexpect [-f output_script_name] [-h #For help] COMMAND
Example: ./easyexpect  -f ssh_login.exp ssh -l admin 173.39.26.130

 
Login to a router and generate script output
=======================================================

~/scripts/easyexpect
[sargandh:bgl-ads-1214]$ ls -lh
total 16K
-rw-r--r-- 1 sargandh eng 3.8K Feb 11 15:12 README.txt
-rwxr-xr-x 1 sargandh eng 9.2K Feb 11 14:42 easyexpect
~/scripts/easyexpect
[sargandh:bgl-ads-1214]$ ./easyexpect -f telnet_login.exp telnet crs-vega1-lnx 8001 
autoexpect started, file is telnet_login.exp
Trying 10.127.60.57...
Connected to crs-vega1-lnx.cisco.com (10.127.60.57).
Escape character is '^]'.


User Access Verification

Username: lab
Password: 


RP/0/RP1/CPU0:PE1#sh install active sum
Default Profile:
  Admin Resources
  SDRs:
    Owner
  Active Packages:
    disk0:hfr-k9sec-px-6.0.1.16I
    disk0:hfr-diags-px-6.0.1.16I
    disk0:hfr-asr9000v-nV-px-6.0.1.16I
    disk0:hfr-li-px-6.0.1.16I
    disk0:hfr-fpd-px-6.0.1.16I
    disk0:hfr-doc-px-6.0.1.16I
    disk0:hfr-video-px-6.0.1.16I
    disk0:hfr-services-px-6.0.1.16I
    disk0:hfr-mpls-px-6.0.1.16I
    disk0:hfr-mini-px-6.0.1.16I
    disk0:hfr-mgbl-px-6.0.1.16I
    disk0:hfr-mcast-px-6.0.1.16I
    disk0:hfr-px-6.0.1.16I.CSCux75653-0.0.13.i
    disk0:hfr-px-6.0.1.16I.CSCux38334-0.0.11.i
    disk0:hfr-px-6.0.1.16I.CSCux81440-1.0.0
    disk0:hfr-px-6.0.1.16I.CSCuy15359-0.0.2.i
    disk0:hfr-px-6.0.1.16I.CSCuy09501-0.0.4.d
    disk0:hfr-px-6.0.1.16I.CSCuy05069-0.0.2.i

RP/0/RP1/CPU0:PE1#sh bgp sum
BGP router identifier 5.5.5.5, local AS number 100
BGP generic scan interval 60 secs
Non-stop routing is enabled
BGP table state: Active
Table ID: 0xe0000000   RD version: 456403
BGP main routing table version 456403
BGP NSR Initial initsync version 52227 (Reached)
BGP NSR/ISSU Sync-Group versions 456403/0
BGP scan interval 60 secs

BGP is operating in STANDALONE mode.


Process       RcvTblVer   bRIB/RIB   LabelVer  ImportVer  SendTblVer  StandbyVer
Speaker          456403     456403     456403     456403      456403      456403

Neighbor        Spk    AS MsgRcvd MsgSent   TblVer  InQ OutQ  Up/Down  St/PfxRcd
6.6.6.6           0   100   31837   31143   456403    0    0    1d22h          0
7.7.7.7           0   100   23596   26277   456403    0    0    1d23h        100
8.8.8.8           0   100    4901   25174   456403    0    0    1d23h      15100
53.0.0.14         0  5050    2931    3180   456403    0    0 02:13:16       5000
53.0.0.18         0  5050    2931    3180   456403    0    0 02:13:09       5000
53.0.0.22         0  5050    2930    3180   456403    0    0 02:13:10       5000
53.0.0.26         0  5050    2931    3181   456403    0    0 02:13:16       5000
53.0.0.30         0  5050    2932    3182   456403    0    0 02:13:15       5000
53.0.0.34         0  5050    2930    3180   456403    0    0 02:13:13       5000
53.0.0.38         0  5050    2931    3181   456403    0    0 02:13:10       5000
53.0.0.42         0  5050    2930    3180   456403    0    0 02:13:14       5000
53.0.0.46         0  5050    2930    3181   456403    0    0 02:13:15       5000
53.0.0.50         0  5050    2931    3180   456403    0    0 02:13:16       5000

RP/0/RP1/CPU0:PE1#exit
Connection closed by foreign host.
autoexpect done, file is telnet_login.exp
~/scripts/easyexpect
[sargandh:bgl-ads-1214]$ ls -lh
total 24K
-rw-r--r-- 1 sargandh eng 3.8K Feb 11 15:12 README.txt
-rwxr-xr-x 1 sargandh eng 9.2K Feb 11 14:42 easyexpect
-rwxr-xr-x 1 sargandh eng 7.1K Feb 11 15:13 telnet_login.exp <<---------------Generated script


Running the script
==================

------------------------------------------------------------------------------------
Note - The script runs and executes the commands and DOES NOT verify the show output
------------------------------------------------------------------------------------

[sargandh:bgl-ads-1214]$ ./telnet_login.exp 
spawn telnet crs-vega1-lnx 8001
Trying 10.127.60.57...
Connected to crs-vega1-lnx.cisco.com (10.127.60.57).
Escape character is '^]'.


User Access Verification

Username: lab
Password: 


RP/0/RP1/CPU0:PE1#sh install active sum
Default Profile:
  Admin Resources
  SDRs:
    Owner
  Active Packages:
    disk0:hfr-k9sec-px-6.0.1.16I
    disk0:hfr-diags-px-6.0.1.16I
    disk0:hfr-asr9000v-nV-px-6.0.1.16I
    disk0:hfr-li-px-6.0.1.16I
    disk0:hfr-fpd-px-6.0.1.16I
    disk0:hfr-doc-px-6.0.1.16I
    disk0:hfr-video-px-6.0.1.16I
    disk0:hfr-services-px-6.0.1.16I
    disk0:hfr-mpls-px-6.0.1.16I
    disk0:hfr-mini-px-6.0.1.16I
    disk0:hfr-mgbl-px-6.0.1.16I
    disk0:hfr-mcast-px-6.0.1.16I
    disk0:hfr-px-6.0.1.16I.CSCux75653-0.0.13.i
    disk0:hfr-px-6.0.1.16I.CSCux38334-0.0.11.i
    disk0:hfr-px-6.0.1.16I.CSCux81440-1.0.0
    disk0:hfr-px-6.0.1.16I.CSCuy15359-0.0.2.i
    disk0:hfr-px-6.0.1.16I.CSCuy09501-0.0.4.d
    disk0:hfr-px-6.0.1.16I.CSCuy05069-0.0.2.i

RP/0/RP1/CPU0:PE1#sh bgp sum
BGP router identifier 5.5.5.5, local AS number 100
BGP generic scan interval 60 secs
Non-stop routing is enabled
BGP table state: Active
Table ID: 0xe0000000   RD version: 456403
BGP main routing table version 456403
BGP NSR Initial initsync version 52227 (Reached)
BGP NSR/ISSU Sync-Group versions 456403/0
BGP scan interval 60 secs

BGP is operating in STANDALONE mode.


Process       RcvTblVer   bRIB/RIB   LabelVer  ImportVer  SendTblVer  StandbyVer
Speaker          456403     456403     456403     456403      456403      456403

Neighbor        Spk    AS MsgRcvd MsgSent   TblVer  InQ OutQ  Up/Down  St/PfxRcd
6.6.6.6           0   100   31838   31144   456403    0    0    1d22h          0
7.7.7.7           0   100   23596   26278   456403    0    0    1d23h        100
8.8.8.8           0   100    4902   25175   456403    0    0    1d23h      15100
53.0.0.14         0  5050    2931    3180   456403    0    0 02:13:32       5000
53.0.0.18         0  5050    2931    3180   456403    0    0 02:13:25       5000
53.0.0.22         0  5050    2930    3180   456403    0    0 02:13:26       5000
53.0.0.26         0  5050    2931    3181   456403    0    0 02:13:32       5000
53.0.0.30         0  5050    2932    3182   456403    0    0 02:13:31       5000
53.0.0.34         0  5050    2930    3180   456403    0    0 02:13:29       5000
53.0.0.38         0  5050    2931    3181   456403    0    0 02:13:26       5000
53.0.0.42         0  5050    2930    3180   456403    0    0 02:13:30       5000
53.0.0.46         0  5050    2930    3181   456403    0    0 02:13:31       5000
53.0.0.50         0  5050    2931    3180   456403    0    0 02:13:32       5000

RP/0/RP1/CPU0:PE1#exit
Connection closed by foreign host.
~/scripts/easyexpect
[sargandh:bgl-ads-1214]$ ls -lh
total 28K
-rw-r--r-- 1 sargandh eng 3.8K Feb 11 15:12 README.txt
-rwxr-xr-x 1 sargandh eng 9.2K Feb 11 14:42 easyexpect
-rw-r--r-- 1 sargandh eng 2.8K Feb 11 15:13 script_log_1455183803
-rwxr-xr-x 1 sargandh eng 7.1K Feb 11 15:13 telnet_login.exp
~/scripts/easyexpect
[sargandh:bgl-ads-1214]$ 


Enable the script for output verification
=========================================

* line match verification
  -----------------------
  if we want to verify the show install active summary command output to contain an expected version to be present, edit the telnet_login.exp script file.

  Jump to line where show install active summary command is issued and uncomment below like lines.
  "#verify_this_output {    disk0:hfr-mini-px-6.0.1.16I\r}"
  to 
  "verify_this_output {    disk0:hfr-mini-px-6.0.1.16I\r}"

  By uncommenting the above lines, the script will check for line "    disk0:hfr-mini-px-6.0.1.16I\r}" to be present on output.
  PASS/FAIL messages are logged with comparision results.   

* Delimited string match verification
  -----------------------------------
  For most of the commands, full line matching will fail since timestamps, uptimes are used as part of the output.
  For example show bgp summary, show ospf neighbor command includes uptime in their output.
  For these type of commands, check only for specific fields in the output.

  Example edit the script for bgp neighbor, AS and prefix count verification.     
  Use "()" notation for specific string match

  "#verify_this_output {7.7.7.7           0   100   23596   26277   456403    0    0    1d23h        100\r}" 
  to
  "verify_this_output {(7.7.7.7)           0   (100)   23596   26277   456403    0    0    1d23h        (100)\r}"

  
  ~/scripts/easyexpect
  [sargandh:bgl-ads-1214]$ egrep ^verify ./telnet_login.exp 
  verify_this_output {    disk0:hfr-mini-px-6.0.1.16I\r}
  verify_this_output {(7.7.7.7)           0   (100)   23596   26277   456403    0    0    1d23h        (100)\r}
  ~/scripts/easyexpect
 
  PASS/FAIL LOG messages
  ----------------------

  ----------------------------------------------------
  Checking for the below line to be present on ouptut
      disk0:hfr-mini-px-6.0.1.16I\r
  ----------------------------------------------------
  PASS: Line {    disk0:hfr-mini-px-6.0.1.16I\r} found on output
  ----------------------------------------------------

  ----------------------------------------------------
  Checking for the below line to be present on ouptut
  (7.7.7.7)           0   (100)   23596   26277   456403    0    0    1d23h        (100)\r
  ----------------------------------------------------
  PASS: Line {(7.7.7.7)           0   (100)   23596   26277   456403    0    0    1d23h        (100)\r} found on output
  TCL regexp used: {7.7.7.7.*100.*100}
  ----------------------------------------------------
 

Adding sleep for show command verification
=========================================

When commands like "clear bgp *", "clear ospf process", etc are used, the next show output cannot be immediately verified and 
it needs to be verified after a sleep time. 

So the generated script adds a commented sleep command for every show command issued. Uncomment and modify the sleep time as needed.

#sleep 60; #sleep for 60 seconds
send -- "sh bgp sum\r"
expect -exact "RP/0/RP1/CPU0:PE1#"

to

sleep 60; #sleep for 60 seconds
send -- "sh bgp sum\r"
expect -exact "RP/0/RP1/CPU0:PE1#"


 
