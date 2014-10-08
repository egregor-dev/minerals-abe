# Copyright(C) 2014 by Abe developers.

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public
# License along with this program.  If not, see
# <http://www.gnu.org/licenses/agpl.html>.

from .X11PosChain import X11PosChain
from .. import util

class Minerals(X11PosChain):
    """
    Experimental module for Minerals, an X11 PoW/PoS crypto currency
    """
    def __init__(chain, **kwargs):
        chain.name = 'Minerals'
        chain.code3 = 'MIN'
        chain.address_version = '\x32'
        chain.script_addr_vers = '\x05'
        chain.magic = "\xa1\xa0\xa2\xa3"
        super(Minerals, chain).__init__(**kwargs)

#    def transaction_hash(chain, binary_tx):
#        return util.sha256(binary_tx)

    datadir_conf_file_name = 'Minerals.conf'
    datadir_rpcport = 33441
    datadir_p2pport = 33442
