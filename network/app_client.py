#!/usr/bin/env python3

import sys
import socket
import ssl
import selectors
import traceback
import threading
import PySide2.QtCore as QtCore
import network.libclient as libclient
import controllers.netNodeSelector as netNodeSelector

class ClientController(QtCore.QObject):
    connectionToServerFailed = QtCore.Signal()
    def __init__(self, controller):
        super().__init__()
        self.create_event_loop_thread()
        self.create_ssl_context()
        self.sel = selectors.DefaultSelector()
        self.controllerInstance = controller
        

        #Signals and Slots Connections
        if self.controllerInstance.__class__ == netNodeSelector.NetSelectorController:
            self.connectionToServerFailed.connect(self.controllerInstance.notifyConnectionToServer) 

    def create_request(self, action, value):
        # if action == "search" or action == "get_netnodes_in_use" or action == "add_node_in_use":
        return dict(
            type="text/json",
            encoding="utf-8",
            content=dict(action=action, value=value),
        )
        # else:
        #     return dict(
        #         type="binary/custom-client-binary-type",
        #         encoding="binary",
        #         content=bytes(action + value, encoding="utf-8"),
        #     )

    def create_ssl_context(self):
        self.ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        self.ssl_context.load_verify_locations("security/ca.crt")

    def create_event_loop_thread(self):
        self.connectionThread = threading.Thread(target=self.start_event_loop)
        self.connectionThread.daemon = False

    def start_connection(self, host, port, request):
        addr = (host, port)
        # print(f"Starting connection to {addr}")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ssl_sock = self.ssl_context.wrap_socket(sock, server_hostname="heatsserver")
        ssl_sock.setblocking(False)
        ssl_sock.connect_ex(addr)
        events = selectors.EVENT_READ | selectors.EVENT_WRITE
        message = libclient.Message(self.sel, ssl_sock, addr, request, self.controllerInstance)
        self.sel.register(ssl_sock, events, data=message)


    # if len(sys.argv) != 5:
    #     print(f"Usage: {sys.argv[0]} <host> <port> <action> <value>")
    #     sys.exit(1)

    def start_client(self, host, port, action, value):
        action, value = action, value
        request = self.create_request(action, value)
        self.start_connection(host, port, request)
        if not self.connectionThread.is_alive():
            self.connectionThread = threading.Thread(target=self.start_event_loop)
            self.connectionThread.daemon = False
            self.connectionThread.start()

    def start_event_loop(self):
        try:
            while True:
                events = self.sel.select(timeout=None)
                for key, mask in events:
                    message = key.data
                    try:
                        # self.processEventsSignal.emit(mask)
                        message.process_events(mask)
                    except Exception as e:
                        print(
                            f"Main: Error: Exception for {message.addr}:\n"
                            f"{traceback.format_exc()}"
                        )
                        if e.__class__ == ssl.SSLEOFError and e.args[0] == 8:
                            print("No se pudo conectar al servidor")
                            self.connectionToServerFailed.emit() 
                        message.close()
                # Check for a socket being monitored to continue.
                if not self.sel.get_map():
                    break
        except Exception as e:
            print(e)
        # finally:
        #     self.sel.close()
