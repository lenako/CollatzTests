#!/usr/bin/env python

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2013
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
import sys

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_single

# -----------
# TestCollatz
# -----------

class TestCollatz (unittest.TestCase) :
    # ----
    # read
    # ----

    def test_read_1 (self) :
        r = StringIO.StringIO("1 10\n")
        p = collatz_read(r)
        (i, j) = p.next()
        self.assert_(i ==  1)
        self.assert_(j == 10)

    def test_read_2 (self) :
        r = StringIO.StringIO("7851 38927\n")
        p = collatz_read(r)
        (i, j) = p.next()
        self.assert_(i ==  7851)
        self.assert_(j == 38927)

    def test_read_3 (self) :
        r = StringIO.StringIO("89523 2389\n")
        p = collatz_read(r)
        (i, j) = p.next()
        self.assert_(i ==  89523)
        self.assert_(j == 2389)

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval((1, 10), { 1 : 1})
        self.assert_(v == 20)

    def test_eval_2 (self) :
        v = collatz_eval((100, 200), { 1 : 1})
        self.assert_(v == 125)

    def test_eval_3 (self) :
        v = collatz_eval((201, 210), { 1 : 1})
        self.assert_(v == 89)

    def test_eval_4 (self) :
        v = collatz_eval((900, 1000), { 1 : 1})
        self.assert_(v == 174)

# ------------
# collatz_single
# ------------

    def test_single_1 (self) :
        s = collatz_single(10,{ 1 : 1})
        self.assert_(s == 7)

    def test_single_2 (self) :
        s = collatz_single(100,{ 1 : 1})
        self.assert_(s == 26)

    def test_single_3 (self) :
        s = collatz_single(1000,{ 1 : 1})
        self.assert_(s == 112)

    def test_single_4 (self) :
        s = collatz_single(99999,{ 1 : 1})
        self.assert_(s == 227)

    def test_single_5 (self) :
        s = collatz_single(420,{ 1 : 1})
        self.assert_(s == 41)

    def test_single_6 (self) :
        s = collatz_single(80085,{ 1 : 1})
        self.assert_(s == 33)

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO.StringIO()
        collatz_print(w, (1, 10), 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_print_2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, (100, 200), 125)
        self.assert_(w.getvalue() == "100 200 125\n")

    def test_print_3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, (900, 1000), 174)
        self.assert_(w.getvalue() == "900 1000 174\n")


    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

# ----
# main
# ----

print "TestCollatz.py"
sys.stdout.flush()
unittest.main()
print "Done."
