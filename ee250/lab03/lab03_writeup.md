Question 1
---
udpServer1.py Output:

```
Process 1 Server Started
```

udpServer2.py Output:
```
Traceback (most recent call last):
  File "udpServer2.py", line 30, in <module>
    Process2()
  File "udpServer2.py", line 16, in Process2
    s.bind((host,port))
OSError: [Errno 98] Address already in use
```
When we try running both scripts the second one fails because it is trying to bind the same port that the first server has already bound.

Question 2
---
udpClient.py Output with Port of 1023:
```
Traceback (most recent call last):
  File "udpClient.py", line 32, in <module>
    Main()
  File "udpClient.py", line 12, in Main
    s.bind((host,port))
PermissionError: [Errno 13] Permission denied
```

udpClient.py Output with Port of 1024:
```
destination port->
```

The port number of 1023 fails because ports 0-1023 are the port numbers for common protocols so it needs superuser privilege to use port 1023.

Question 3
---
Raspberry Pi IP:
`192.168.1.20`

VM VirtualBox IP: `10.0.2.15`
