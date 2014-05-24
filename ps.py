#!/usr/bin/env python
import os
import sys
from pprint import pprint

from pyskytap import Skytap, VMS, Configuration

st=Skytap()

print "Connected?" + str(st.is_connected())
st.connect('http://cloud.skytap.com','spark','@lftra1n','trace.out',30)
print "Connected?" + str(st.is_connected())

c=st.get_configuration(1873144)
##vms=c.get_vms()


print c.get_id()
print c.get_name()
print c.get_owner()
print c.get_region()



