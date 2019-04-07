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

    def test_n(self):
        self.eq('one |two three', 'n_w', 'one two |three')
        self.eq('|one two three', 'n_2w', 'one two |three')
        self.eq('|one two', 'n_3w', 'one tw|o')

    def test_v(self):
        self.eq('one |two three', 'v_w', 'one |two t|hree')
        self.eq('|one two three', 'v_2w', '|one two t|hree')
        self.eq('r_|on|e two three', 'v_w', 'o|ne t|wo three')
        self.eq('r_|one two three|', 'v_w', 'r_one |two three|')
        self.eq('r_|one two three|', 'v_2w', 'r_one two |three|')
        self.eq('|o|ne', 'v_2w', '|one|')
        self.eq('|o|ne\n', 'v_2w', '|one\n|')
        self.eq('r_|one t|wo', 'v_w', 'r_one |t|wo')
        self.eq('r_|one |two', 'v_w', 'one| t|wo')
        self.eq('fi|zz', 'v_w', 'fi|zz|')
        self.eq('r_fi|zz b|uzz', 'v_w', 'r_fizz |b|uzz')
        self.eq('r_fi|zz |buzz', 'v_w', 'fizz| b|uzz')

    def test_b(self):
        self.eq('|fi|zz buzz\n|fi|zz buzz\n', 'b_w', '|fizz b|uzz\n|fizz b|uzz\n')
        self.eq('r_|fi|zz buzz\n|fi|zz buzz\n', 'b_w', 'f|izz b|uzz\nf|izz b|uzz\n')
        self.eq('r_f|izz buz|z\nf|izz buz|z\n', 'b_w', 'r_fizz |buz|z\nfizz |buz|z\n')
        self.eq('fizz |', 'b_w', 'fizz |')
        self.eq('fizz | |', 'b_w', 'fizz | |')
        self.eq('|', 'b_w', '|')

    def test_d(self):
        self.eq('one |two three', 'dw', 'one |three')
        self.eq('one t|wo three', 'dw', 'one t|three')
        self.eq('1\n|\n2\n3', 'dw', '1\n|2\n3')
        self.eq('1\n|\n\n2\n3', 'dw', '1\n|\n2\n3')
