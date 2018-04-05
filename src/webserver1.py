# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: He Yu, Date:2018/4/6

import socket

HOST, PORT = '', 8888

# Create a socket (SOCK_STREAM means a TCP socket)
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Receive data from the server
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(5)
print('Serving HTTP on port %s ...' % PORT)
while True:
    # Accept a connection(or a new socket) from client
    client_connection, client_address = listen_socket.accept()
    print('client_connection: %s; client_address: %s ...' % (client_connection, client_address))

    # Receive data from the client socket
    request = client_connection.recv(1024)
    print('request: %s ...' % request)

    http_response = """\
HTTP/1.1 200 OK

Hello, World!
"""
    # Send data to client by client socket
    client_connection.sendall(bytes(http_response, encoding='utf-8'))
    # CLose client socket
    client_connection.close()
