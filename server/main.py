#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'dengzhc'

import sys
sys.path.append('..')

from example import Features
from example import ttypes
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from thrift.server import TNonblockingServer
import time
import detect

__HOST = '0.0.0.0'
__PORT = 6300

class CalculatorHandler(object):
    def __init__(self):
        print("init")
    def add(self, num1, num2):
        print(1)
        time.sleep(10)
        return num1 + num2

if __name__ == '__main__':
    handler = detect.FeaturesHandler()
    processor = Features.Processor(handler)
    transport = TSocket.TServerSocket(__HOST, __PORT)
    inpfactory = TBinaryProtocol.TBinaryProtocolFactory()
    outpfactory = TBinaryProtocol.TBinaryProtocolFactory()

    #rpcServer = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
    rpcServer = TNonblockingServer.TNonblockingServer(processor, transport, inpfactory, outpfactory)
    print("Starting the rpc server at %s:%d"%(__HOST, __PORT))
    rpcServer.serve()