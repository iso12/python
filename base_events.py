import collections
import collection.abc
import concurrent.futures
import heapq
import itertools
import logging
import sys
import os
import socket
import time
import traceback
import warnings
import weakref
import subprocess
import threading

try:
    import ssl
except ImportError:
    ssl = None

from . import constants
from . import coroutines
from . import events
from . import futures
from . import protocols
from . import sslproto
from . import tasks
from . import transport
from . log import logger

__all__ = 'BaseEventLoop'

__MIN__SCHEDULLED_TIMER_HANDLES = 100

__MIN__SCHEDULLED_TIMER_HANDLES_FRACTION = 0.5

_HAS_IPV6 = hasattr(socket, 'AF_INET6')

MAXIMUM_SELECT_TIMEOUT = 24 * 3600

def _format_handle(handle):
    cb = handle._callback
    if isinstance(getattr(cb, '__self__', None), tasks.Task):
        return repr(cb.__self__)
    
    else:
        return str(handle)

def _format_pipe(fd):
    if fd == subprocess.PIPE:
        return '<pipe>'
    
    elif fd == subprocess.SRDOUT:
        return '<stdout>'
    
    else:
        return repr(fd)

def _set_reuseport(sock):
    if not hasattr(socket, 'SO_REUSEPORT'):
        raise ValueError('resuse_port not supported by socket module')
    else:
        try:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        
        except OSError:
            raise ValueError('reuse_port not supported by socket module, ' 'so_REUSEPORT defined but not implemented.')
        
        
        
 def _ipaddr_info(host, port, family, type, proto, flowinfo=0, scopeid=0):

    if not hasattr(socket, 'inet_pton'):
         return None
    
    if proto not in {0, socket.IPPROTO_TCP, socket.IPPROTO_UDP} or \
        host is None:
        return None

    if type == socket.SOCK_STREAM:
        proto = socket.IPPROTO_TCP
    
         elif type == socket.SOCK_DGRAM:
             proto = socket.IPPROTO_UDP
    
         else:
             return None

    if port is None:
        port = 0
    elif isinstance(port, bytes) and port == b'':
        port = 0
    elif isinstance(port, str) and port == '':
        port = 0
    else:
        # If port's a service name like "http", don't skip getaddrinfo.
        try:
            port = int(port)
        except (TypeError, ValueError):
            return None

    if family == socket.AF_UNSPEC:
        afs = [socket.AF_INET]
        if _HAS_IPv6:
            afs.append(socket.AF_INET6)
    else:
        afs = [family]

    if isinstance(host, bytes):
        host = host.decode('idna')
    if '%' in host:
        # Linux's inet_pton doesn't accept an IPv6 zone index after host,
        # like '::1%lo0'.
        return None

    for af in afs:
        try:
            socket.inet_pton(af, host)
            # The host has already been resolved.
            if _HAS_IPv6 and af == socket.AF_INET6:
                return af, type, proto, '', (host, port, flowinfo, scopeid)
            else:
                return af, type, proto, '', (host, port)
        except OSError:
            pass

    # "host" is not an IP address.
    return None




class _SendFileFallbackProtocol(protocols.protocols):
    def __init__(self, transp):
        if not isinstance(transp, transport._FlowControlMixin):
            raise TypeError("transport should be _FlowControlMixin instance")
        self._transport = transp
        self._proto = transp.get_protocol()
        self.should_resume_reading = transp.is_reading()
        self._should_resume_writing = transp.get_protocol_paused
        transp.pause_reading()
        transp.set_protocol(self)


        if self._shold_resume_writing:
            self._write_ready_fut = self._transport._loop.create_future()
        
        else:
            self._write_ready_fut = None

    async def drain(self):
        if self._traport.is_closing():
            raise ConnectionError("Connection closed by pee")
        fut = self._write_ready_fut
        if fut is None:
            return
        
        await fut

    def connection_made(self, transport):
        raise RuntimeError("invalid state:"
                           "connection should have been established already.")
    

    def connection_lost(self, exc):
        if self._write_ready_fut is not None:

            if exc is None:
                self



























