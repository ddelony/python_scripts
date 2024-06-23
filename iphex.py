#!/usr/bin/env python
# iphex - Display IP address in hex.

import netaddr
import sys

if len(sys.argv) == 2:
    ip = netaddr.IPAddress(sys.argv[1])
else:
    print("IP address required.")

print(hex(ip))
