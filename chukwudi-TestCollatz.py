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

    def test_read_1 (self) :
        r = StringIO.StringIO("300 400\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  300)
        self.assert_(a[1] == 400)

    def test_read_2 (self) :
        r = StringIO.StringIO("105 115\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  105)
        self.assert_(a[1] == 115)

    def test_read_3 (self) :
        r = StringIO.StringIO("603 703\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  603)
        self.assert_(a[1] == 703)

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval(300, 400)
        self.assert_(v == 144)

    def test_eval_2 (self) :
        v = collatz_eval(105, 115)
        self.assert_(v == 114)

    def test_eval_3 (self) :
        v = collatz_eval(603, 703)
        self.assert_(v == 171)

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 300, 400, 144)
        self.assert_(w.getvalue() == "300 400 144\n")

    def test_print_2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 105, 115, 114)
        self.assert_(w.getvalue() == "105 115 114\n")

    def test_print_3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 603, 703, 171)
        self.assert_(w.getvalue() == "603 703 171\n")

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO.StringIO("300 400\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "300 400 144\n")

    def test_solve_2 (self) :
        r = StringIO.StringIO("300 400\n105 115\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "300 400 144\n105 115 114\n")

    def test_solve_3 (self) :
        r = StringIO.StringIO("300 400\n105 115\n603 703")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "300 400 144\n105 115 114\n603 703 171\n")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
