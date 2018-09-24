from __future__ import print_function
from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

class Helloer(DatagramProtocol):

    def startProtocol(self):
        host = "127.0.0.1"
        port = 12345

        print("Listening at port", port)

    def datagramReceived(self, data, addr):
        print("Heard request from client " + str(addr[0]) + ":" + str(addr[1]))
        self.transport.write(b'Hello world', addr) # no need for address

# 0 means any port, we don't care in this case
reactor.listenUDP(12345, Helloer())
reactor.run()
