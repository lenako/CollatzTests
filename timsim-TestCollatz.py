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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, single_collatz

# -----------
# TestCollatz
# -----------

class TestCollatz (unittest.TestCase) :
    # ----
    # read
    # ----

    def test_read_1 (self) :
        r = StringIO.StringIO("1 10\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] == 10)

    def test_read_2 (self) :
        r = StringIO.StringIO("1 120\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] == 120)

    def test_read_3 (self) :
        r = StringIO.StringIO("9 10\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  9)
        self.assert_(a[1] == 10)

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

    #Test reversed range
    def test_eval_5 (self) :
        v = collatz_eval(10, 1)
        self.assert_(v == 20)

    # ---
    # single_collatz
    # ---
    def test_single_1 (self) :
        v = single_collatz(1)
        self.assert_(v == 1)

    def test_single_2 (self) :
        v = single_collatz(2)
        self.assert_(v == 2)

    def test_single_3 (self) :
        v = single_collatz(4)
        self.assert_(v == 3)

    def test_single_4 (self) :
        v = single_collatz(5)
        self.assert_(v == 6)

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_print_2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 10, 100, 21)
        self.assert_(w.getvalue() == "10 100 21\n")

    def test_print_3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 3, 2)
        self.assert_(w.getvalue() == "1 3 2\n")

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2 (self) :
        r = StringIO.StringIO("3 70\n5 248\n201 210\n4 232\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "3 70 113\n5 248 128\n201 210 89\n4 232 128\n")

    def test_solve_3 (self) :
        r = StringIO.StringIO("4 66\n5 52\n1 207")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "4 66 113\n5 52 112\n1 207 125\n")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."