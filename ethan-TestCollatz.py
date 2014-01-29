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

import io
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

    def test_read_simple (self) :
        r = StringIO.StringIO("1 10\n")
        m = collatz_read(r)
        (i, j) = m.next()
        self.assertTrue(i == 1)
        self.assertTrue(j == 10)

    def test_read_same (self) :
        r = StringIO.StringIO("1 1\n")
        m = collatz_read(r)
        (i, j) = m.next()
        self.assertTrue(i == 1)
        self.assertTrue(j == 1)
        self.assertTrue(j == i)

    def test_read_large (self) :
        r = StringIO.StringIO("1 999999\n")
        m = collatz_read(r)
        (i, j) = m.next()
        self.assertTrue(i == 1)
        self.assertTrue(j == 999999)

    def test_read_reverse (self) :
        r = StringIO.StringIO("999999 1\n")
        m = collatz_read(r)
        (i, j) = m.next()
        self.assertTrue(i == 999999)
        self.assertTrue(j == 1)

    # # ----
    # # eval
    # # ----

    def test_eval_1 (self) :
        v = collatz_eval((1, 10))
        self.assertTrue(v == 20)

    def test_eval_2 (self) :
        v = collatz_eval((100, 200))
        self.assertTrue(v == 125)

    def test_eval_3 (self) :
        v = collatz_eval((201, 210))
        self.assertTrue(v == 89)

    def test_eval_4 (self) :
        v = collatz_eval((900, 1000))
        self.assertTrue(v == 174)

    def test_eval_midrange (self) :
        v = collatz_eval((30116, 42098))
        self.assertTrue(v == 324)

    def test_eval_lowbound (self) :
        v = collatz_eval((1, 1))
        self.assertTrue(v == 1)

    def test_eval_highbound (self) :
        v = collatz_eval((999999, 999999))
        self.assertTrue(v == 259)

    # # -----
    # # print
    # # -----

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, (1, 10), 20)
        self.assertTrue(w.getvalue() == "1 10 20\n")

    def test_print_lowbound (self) :
        w = StringIO.StringIO()
        collatz_print(w, (1, 1), 1)
        self.assertTrue(w.getvalue() == "1 1 1\n")

    def test_print_highbound (self) :
        w = StringIO.StringIO()
        collatz_print(w, (999999, 999999), 259)
        self.assertTrue(w.getvalue() == "999999 999999 259\n")

    def test_print_bigMax (self) :
        w = StringIO.StringIO()
        collatz_print(w, (12345, 98765), 43210)
        self.assertTrue(w.getvalue() == "12345 98765 43210\n")

    # # -----
    # # solve
    # # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_empty (self) :
        r = StringIO.StringIO("")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "")

    def test_solve_same (self) :
        r = StringIO.StringIO("27 27\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "27 27 112\n")
# ----
# main
# ----

print("TestCollatz.py")
unittest.main()
print("Done.")


