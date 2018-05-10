# Copyright (C) 2018 The NeoVintageous Team (NeoVintageous).
#
# This file is part of NeoVintageous.
#
# NeoVintageous is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# NeoVintageous is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with NeoVintageous.  If not, see <https://www.gnu.org/licenses/>.

from NeoVintageous.tests import unittest


class Test_w(unittest.FunctionalTestCase):

    def test_w(self):
        self.eq('one |two three', 'w', 'one two |three')
        self.eq('|one two three', '2w', 'one two |three')

    def test_v_w(self):
        self.eq('one |two three', 'v_w', 'one |two t|hree')
        self.eq('|one two three', 'v_2w', '|one two t|hree')
