#!/usr/bin/env python
#
# Copyright 2018-present Facebook. All Rights Reserved.
#
# This program file is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; version 2 of the License.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
# for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program in a file named COPYING; if not, write to the
# Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA
#

from common.base_fans_test import CommonFanUtilBasedFansTest
from utils.cit_logger import Logger


class FansTest(CommonFanUtilBasedFansTest):
    def setUp(self):
        self.start_logging(__name__)
        self.fans = [0, 1]
        self.pwms = [0, 1]
        self.kill_fan_ctrl_cmd = ["/usr/bin/sv stop fscd"]
        self.start_fan_ctrl_cmd = ["/usr/bin/sv start fscd"]

    def tearDown(self):
        self.kill_fan_controller()
        self.start_fan_controller()
