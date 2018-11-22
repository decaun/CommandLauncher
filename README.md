# querylauncher
GUI to help you launch sqlcmd commands.
List taken from left pane for sqlcmd -S switch and querry on top pane passed for every destination at left pane.
On the bottom pane querry output will be visible after launch in a LIFO fashion by non-blocking order.
User name and password passed to -U and -P switch for database login.
If no password specified at database side please use "" as password.

Multithreading used to sustain non-blocking behaviour.
Thread pool increases due to stack space optimization on the run.

![alt text](https://image.ibb.co/iLY12A/Capture22.jpg)
