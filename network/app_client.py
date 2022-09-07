#!/usr/bin/env python3

import sys
import socket
import selectors
import traceback
import threading

import network.libclient as libclient

class ClientController():
    def __init__(self):
        self.sel = None

    def create_request(self, action, value):
        if action == "search" or action == "get_netnodes_in_use" or action == "add_node_in_use":
            return dict(
                type="text/json",
                encoding="utf-8",
                content=dict(action=action, value=value),
            )
        else:
            return dict(
                type="binary/custom-client-binary-type",
                encoding="binary",
                content=bytes(action + value, encoding="utf-8"),
            )


    def start_connection(self, host, port, request, controllerInstance):
        addr = (host, port)
        print(f"Starting connection to {addr}")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setblocking(False)
        sock.connect_ex(addr)
        events = selectors.EVENT_READ | selectors.EVENT_WRITE
        message = libclient.Message(self.sel, sock, addr, request, controllerInstance)
        self.sel.register(sock, events, data=message)


    # if len(sys.argv) != 5:
    #     print(f"Usage: {sys.argv[0]} <host> <port> <action> <value>")
    #     sys.exit(1)

    def start_client(self, host, port, action, value, controllerInstance):
        self.sel = selectors.DefaultSelector()
        action, value = action, value
        request = self.create_request(action, value)
        self.start_connection(host, port, request, controllerInstance)
        connectionThread = threading.Thread(target=self.start_event_loop)
        connectionThread.daemon = False
        connectionThread.start()

    def start_event_loop(self):
        try:
            while True:
                events = self.sel.select(timeout=None)
                for key, mask in events:
                    message = key.data
                    try:
                        message.process_events(mask)
                    except Exception:
                        print(
                            f"Main: Error: Exception for {message.addr}:\n"
                            f"{traceback.format_exc()}"
                        )
                        message.close()
                # Check for a socket being monitored to continue.
                if not self.sel.get_map():
                    break
        finally:
            self.sel.close()
