# Overview

This software was created as a way to devlve into learning how networking between computers and servers work. This follows a Client/Server model
and so to start first the server because that is how the clients talk to each other. Both of these programs can be started through a powershell or command prompt terminal. Or if using VS Code, you can split the terminal and see everthing there.

The purpose of writing this software was to learn some of the basics of networking with computers.

[Software Demo Video](https://youtu.be/061q3BKRSJc)

# Network Communication

{Describe the architecture that you used (client/server or peer-to-peer)}
This is a client/server architecture meaning that unlike with peer-to-peer where two computers could talk directly to themselves, the clients connect on an IP address and port number.

what I used was TCP and the port 50000 as it is free to be assigned to something else.

The messages sent between the client and server and encoded/decoded from ascii text.

# Development Environment

VS Code IDE
Threading library
Socket library
Python 3.8.6 64-bit

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [Python Server](https://docs.python.org/3.8/library/socketserver.html)
* [Python Socket](https://docs.python.org/3.8/library/socket.html)

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}
* impliment GUI
* test not on local host
