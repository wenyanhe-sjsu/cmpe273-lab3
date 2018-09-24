from __future__ import print_function

from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor


class MulticastPingClient(DatagramProtocol):

    def startProtocol(self):
        IPaddr = "228.0.0.5"
        #IPaddr = "127.0.0.1"
        port = 9999

        # Join the multicast address, so we can receive replies:
        self.transport.joinGroup(IPaddr)
        # Send to IPaddr:port - all listeners on the multicast address
        # (including us) will receive this message.
        # self.transport.write(b'Client: Ping', (IPaddr, port))
        self.transport.write(b'Hello world', (IPaddr, port))

    def datagramReceived(self, datagram, address):
        datagram = datagram.decode()  # remove the 'b' prefix
        print("Datagram %r received from" % datagram, str(address[0]) + ":"
            + str(address[1]))


port = 9999
reactor.listenMulticast(port, MulticastPingClient(), listenMultiple=True)
reactor.run()
