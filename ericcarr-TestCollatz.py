#!/usr/bin/env python

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2014
# Glenn P. Downing
# -------------------------------

"""
To test the program:
    % python TestCollatz.py > TestCollatz.out
    % chmod ugo+x TestCollatz.py
    % TestCollatz.py > TestCollatz.out
"""

# -------
# imports
# -------

import StringIO
import unittest

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, get_cycle

# -----------
# TestCollatz
# -----------

class TestCollatz (unittest.TestCase) :
    # ----
    # read
    # ----

    def test_read1 (self) :
        r = StringIO.StringIO("1 10\n")
        p = collatz_read(r)
        (i, j) = p.next()
        self.assert_(i ==  1)
        self.assert_(j == 10)

    def test_read_2(self):
        r = StringIO.StringIO("2 492819\n")
        p = collatz_read(r)
        (i, j) = p.next()
        self.assert_(i ==  2)
        self.assert_(j == 492819)

    def test_read_3(self):
        r = StringIO.StringIO("1 1000000\n")
        p = collatz_read(r)
        (i, j) = p.next()
        self.assert_(i ==  1)
        self.assert_(j == 1000000)


    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval((1, 10))
        self.assert_(v == 20)

    def test_eval_2 (self) :
        v = collatz_eval((100, 200))
        self.assert_(v == 125)

    def test_eval_3 (self) :
        v = collatz_eval((201, 210))
        self.assert_(v == 89)

    def test_eval_4 (self) :
        v = collatz_eval((900, 1000))
        self.assert_(v == 174)

    def test_eval_5 (self):
        v = collatz_eval((40810, 38305))
        self.assert_(v == 306)

    def test_eval_6 (self):
        v = collatz_eval((4253, 3179))
        self.assert_(v == 238)

    def test_eval_7 (self):
        v = collatz_eval((36, 112))
        self.assert_(v == 119)


    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO.StringIO()
        collatz_print(w, (1, 10), 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_print_2 (self):
        w = StringIO.StringIO()
        collatz_print(w, (525600, 60), 40)
        self.assert_(w.getvalue() == "525600 60 40\n")

    def test_print_3 (self):
        w = StringIO.StringIO()
        collatz_print(w, (1, 2), 3)
        self.assert_(w.getvalue() == "1 2 3\n")

    def test_print_4 (self):
        w = StringIO.StringIO()
        collatz_print(w, (525600, 60), 40)
        self.assert_(w.getvalue() == "525600 60 40\n")

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2 (self) :
        r = StringIO.StringIO("1 1\n15228 66057\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 1 1\n15228 66057 340\n")

    def test_solve_3 (self) :
        r = StringIO.StringIO("747 38331\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "747 38331 324\n")

    def test_get_cycle_1 (self):
        self.assert_(get_cycle(1, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 1, 10) == 1)

    def test_get_cycle_2 (self):
        self.assert_(get_cycle(1, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 1, 10) == 1)

    def test_get_cycle_3 (self):
        self.assert_(get_cycle(20, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 11, 20) == 8)

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
