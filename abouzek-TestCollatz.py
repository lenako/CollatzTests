#!/usr/bin/env python

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2014
# Glenn P. Downing
# -------------------------------

"""
To test the program:
    % python TestCollatz.py >& TestCollatz.out
    % chmod ugo+x TestCollatz.py
    % TestCollatz.py >& TestCollatz.out
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
        r = StringIO.StringIO("10 11\n")
        m = collatz_read(r)
        i, j = list(next(m))
        self.assertTrue(i ==  10)
        self.assertTrue(j == 11)

    def test_read_2 (self) :
        r = StringIO.StringIO("1 1\n")
        m = collatz_read(r)
        i, j = list(next(m))
        self.assertTrue(i ==  1)
        self.assertTrue(j == 1)

    def test_read_3 (self) :
        r = StringIO.StringIO("100 -1\n")
        m = collatz_read(r)
        i, j = list(next(m))
        self.assertTrue(i ==  100)
        self.assertTrue(j == -1)


    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval(1, 10)
        self.assertTrue(v == 20)

    def test_eval_2 (self) :
        v = collatz_eval(100, 200)
        self.assertTrue(v == 125)

    def test_eval_3 (self) :
        v = collatz_eval(201, 210)
        self.assertTrue(v == 89)

    def test_eval_4 (self) :
        v = collatz_eval(900, 1000)
        self.assertTrue(v == 174)

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertTrue(w.getvalue() == "1 10 20\n")

    def test_print_2 (self):
        w = StringIO.StringIO()
        collatz_print(w, -1, -1, -1)
        self.assertTrue(w.getvalue() == "-1 -1 -1\n")

    def test_print_3 (self):
        w = StringIO.StringIO()
        collatz_print(w, 0, 1000, 1)
        self.assertTrue(w.getvalue() == "0 1000 1\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2 (self) :
        r = StringIO.StringIO("29166 79904\n24838 13813\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "29166 79904 351\n24838 13813 282\n")

    def test_solve_3 (self) :
        r = StringIO.StringIO("7477 73577\n11579 32095\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "7477 73577 340\n11579 32095 308\n")

# ----
# main
# ----

print("TestCollatz.py")
unittest.main()
print("Done.")