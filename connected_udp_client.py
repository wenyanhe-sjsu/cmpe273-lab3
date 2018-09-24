from __future__ import print_function
from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

class Helloer(DatagramProtocol):

    def startProtocol(self):
        host = "127.0.0.1"
        port = 12345

        self.transport.connect(host, port)
        self.transport.write(b'hello') # no need for address

    def datagramReceived(self, data, addr):
        data = data.decode()  # remove the annoying 'b' prefix
        print("received %r from server" % data, str(addr[0]) + ":"
            + str(addr[1]))

    # Possibly invoked if there is no server listening on the
    # address to which we are sending.
    def connectionRefused(self):
        print("No one listening")

# 0 means any port, we don't care in this case
reactor.listenUDP(0, Helloer())
reactor.run()
