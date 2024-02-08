# Copyright (C) 2017-2024 Pier Carlo Chiodi
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from .base import MaxPrefixScenarioBIRD2
from .data6 import MaxPrefixScenario_Data6
from pierky.arouteserver.tests.live_tests.bird import BIRDInstanceIPv6, BIRD2Instance

class MaxPrefixScenario_BIRD2IPv6(MaxPrefixScenario_Data6,
                                  MaxPrefixScenarioBIRD2):
    __test__ = True

    SHORT_DESCR = "Live test, BIRD v2, max-prefix, IPv6"
    RS_INSTANCE_CLASS = BIRD2Instance
    CLIENT_INSTANCE_CLASS = BIRDInstanceIPv6
