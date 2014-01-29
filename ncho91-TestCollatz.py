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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------

class TestCollatz (unittest.TestCase) :
    # ----
    # read
    # ----

    def test_read (self) :
        r = StringIO.StringIO("1 10\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] == 10)

    def test_read_2(self) :
        r = StringIO.StringIO("1 100\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 1)
        self.assert_(a[1] == 100)

    def test_read_3(self) :
        r = StringIO.StringIO("999999 999999\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 999999)
        self.assert_(a[1] == 999999)
    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval(1, 10)
        self.assert_(v == 20)

    def test_eval_2 (self) :
        v = collatz_eval(100, 200)
        self.assert_(v == 125)

    def test_eval_3 (self) :
        v = collatz_eval(201, 210)
        self.assert_(v == 89)

    def test_eval_4 (self) :
        v = collatz_eval(900, 1000)
        self.assert_(v == 174)

    def test_eval_5 (self) :
        v = collatz_eval(1, 999999)
        self.assert_(v == 525)

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_print_2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 100, 200, 125)
        self.assert_(w.getvalue() == "100 200 125\n")

    def test_print_3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 900, 1000, 174)
        self.assert_(w.getvalue() == "900 1000 174\n")

    def test_print_4 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 999999, 525)
        self.assert_(w.getvalue() == "1 999999 525\n")


    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2 (self) :
        r = StringIO.StringIO("10 20\n30 40\n50 60\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "10 20 21\n30 40 107\n50 60 113\n")

    def test_solve_3 (self) :
        r = StringIO.StringIO("100 1000\n12345 123456\n500 991991\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "100 1000 179\n12345 123456 354\n500 991991 525\n")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."