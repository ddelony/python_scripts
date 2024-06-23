#!/usr/bin/env python
# urlproto - Print the protocol of a URL
import sys
from urllib.parse import urlparse

url = urlparse(sys.argv[1])
proto = url.scheme
print(proto)
