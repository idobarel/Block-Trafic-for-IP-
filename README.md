# Block-Trafic-for-IP-
Block network traffic using python and arp spoofing<br>


This Project allows you to block a connection on a device that connected to the same wifi network as you.<br>
You can use it as a troll or whatever.<br>

*****MAKE SURE YOU HAVE NMAP FOR HOSTS SCANNING*****



how to use:
1) You need to make sure you have a windows computer, or that your machine is not transfering data to another local network device,
   For example: in kali linux you need to make sure that:
   The output of the command:<br>
   $ cat /proc/sys/net/ipv4/ip_forward<br>
   is:<br>
   $ 0

otherwise the data you blocking will transfer trough your device.<br>

2) when you run the program it will ask you for router ip, most of the times it will be 192.168.1.1 or 192.168.68.1,<br>
   Then it will ask for the target ip address , if u have NMAP it will be at the start on the program (this is why it takes so much time to load).<br>

3) The arp spoof will start as soon you prees enter.<br>



How is it working:

well it is simple, you just make the target's computer think that your ip is the router. Because it is not sending to the actual router anything the pc wont recive or send<br>
anything.<br>
<br>
<br>
Created By GeverAL!
