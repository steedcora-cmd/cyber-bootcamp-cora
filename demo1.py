ip_address="192.168.1.1"

import re
ip=re.search(r"\d+\.\d+\.\d+\.\d+", ip_address)
print(ip.group())