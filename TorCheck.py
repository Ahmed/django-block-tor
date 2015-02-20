#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
 TorCheck.py

 https://check.torproject.org - originally in perl, rewritten in python

 By Jacob Appelbaum <jacob@appelbaum.net>
 Written at ToorCon Seattle 2008 (Thanks for the great time h1kari!)
 Thanks to Crispen for a power outlet :-)
 
 Additional python suggestions from nickm
 
 Best used with the Debian packages:
    python-dns
    libapache2-mod-python
    locales-all

"""

__program__ = 'TorCheck.py'
__version__ = '20100429.01'
__url__ = 'https://svn.torproject.org/svn/check/'
__author__ = 'Jacob Appelbaum <jacob@appelbaum.net>'
__copyright__ = 'Copyright (c) 2008, Jacob Appelbaum'
__license__ = 'See LICENSE for licensing information'

try:
    from future import antigravity
except ImportError:
    antigravity = None

import DNS
from DNS import DNSError
# This is pydns and can be downloaded from http://pydns.sourceforge.net/ 
# Or use the Debian package listed above
import cgitb

cgitb.enable()


# os.environ['LOCPATH']='/usr/share/locale:/srv/check.torproject.org/trunk/i18n/locale'
localedir = '/srv/check.torproject.org/trunk/i18n/locale'

# We could also explictly query the remote EL server
# This is not as good as using a cache for obvious reasons
DNS.DiscoverNameServers()


def is_using_tor(client_ip, el_port):
    # This is the exit node ip address
    # This is where we want to dynamically receive this from Apache
    split_ip = client_ip.split('.')
    split_ip.reverse()
    el_exit_node = ".".join(split_ip)

    # We'll attempt to reach this port on the Target host
    # ELPort is now set by the caller

    # We'll try to reach this host
    target = "38.229.70.31"

    # This is the ExitList DNS server we want to query
    host = "ip-port.exitlist.torproject.org"

    # Prepare the question as an A record request
    question = el_exit_node + "." + el_port + "." + target + "." + host
    request = DNS.DnsRequest(name=question, qtype='A')

    # Ask the question and load the data into our answer
    try:
        answer = request.req()
    except DNSError:
        return 2

    # Parse the answer and decide if it's allowing exits
    # 127.0.0.2 is an exit and NXDOMAIN is not
    if answer.header['status'] == "NXDOMAIN":
        # We're not exiting from a Tor exit
        return 1
    else:
        if not answer.answers:
            # We're getting unexpected data - fail closed
            return 2
        for a in answer.answers:
            if a['data'] != "127.0.0.2":
                return 2
        # If we're here, we've had a positive exit answer
        return 0
