from __future__ import print_function

from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor


class MulticastPingPong(DatagramProtocol):

    def startProtocol(self):
        IPaddr = "228.0.0.5"
        #IPaddr = "127.0.0.1"

        """
        Called after protocol has started listening.
        """
        # Set the TTL>1 so multicast will cross router hops:
        self.transport.setTTL(5)
        # Join a specific multicast group:
        self.transport.joinGroup(IPaddr)

    def datagramReceived(self, datagram, address):
        datagram = datagram.decode()
        print("Datagram %r received from" % datagram, str(address[0]) + ":"
            + str(address[1]))
        if datagram == "Client: Ping":
            # Rather than replying to the group multicast address, we send the
            # reply directly (unicast) to the originating port:
            self.transport.write(b"Server: Pong", address)
        if datagram == "Hello world"
            self.transport.write(b"From Server: Hello world", address)


# We use listenMultiple=True so that we can run MulticastServer.py and
# MulticastClient.py on same machine:
port = 9999
reactor.listenMulticast(port, MulticastPingPong(), listenMultiple=True)
reactor.run()
