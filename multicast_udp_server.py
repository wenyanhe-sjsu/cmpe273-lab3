from __future__ import print_function

from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor


class MulticastPingPong(DatagramProtocol):

    def startProtocol(self):
        #IPaddr = "228.0.0.5"
        IPaddr = "127.0.0.1"

        """
        Called after protocol has started listening.
        """
        #self.transport.setLookbackMode(0)
        print(self.transport.getLoopbackMode())
        # Set the TTL>1 so multicast will cross router hops:
        self.transport.setTTL(5)
        # Join a specific multicast group:
        print(5)
        self.transport.joinGroup(IPaddr)

    def datagramReceived(self, datagram, address):
        print("Datagram %s received from %s" % (repr(datagram), repr(address)))
        if datagram == b"Client: Ping" or datagram == "Client: Ping":
            # Rather than replying to the group multicast address, we send the
            # reply directly (unicast) to the originating port:
            self.transport.write(b"Server: Pong", address)


# We use listenMultiple=True so that we can run MulticastServer.py and
# MulticastClient.py on same machine:
port = 9999
reactor.listenMulticast(port, MulticastPingPong(), listenMultiple=True)
reactor.run()
