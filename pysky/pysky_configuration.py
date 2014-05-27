#--
# Copyright (c) 2014, Darryl Quinn
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions and the following disclaimer in the documentation
#     and/or other materials provided with the distribution.
#   * Neither the name of copyright holders nor the names of its contributors
#     may be used to endorse or promote products derived from this software
#     without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
#--

import sys
import json
##from pyskytap import VMS
from pprint import pprint

class Configuration():

    def __init__(self, j_cfg):
    	## load object
    	self.__cfg = j_cfg
        self.__id = self.__cfg['id']
        self.__owner = self.__cfg['owner']
        self.__name = self.__cfg['name']
        self.__region = self.__cfg['region']
        ##self.__vms = None

    
    def get_owner(self):
        return self.__owner

    def get_name(self):
        return self.__name

    def get_region(self):
        return self.__region

    def get_id(self):
        return self.__id
        
    def get_vms(self):
        ## get the ['vms'] list
        vmslist = self.__cfg['vms']
        for vm in vmslist:
            ## vmobj=VMS(vm)
            self.__vms.append(vm)
        return self.__vms

    def dump(self):
    	print json.dumps(self.__cfg,indent=4)
    	return
