#!/usr/bin/env python3

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

import io
import unittest

from Collatz import collatz_read_1, collatz_read_2, collatz_read_3, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------

class TestCollatz (unittest.TestCase) :
    # ----
    # read
    # ----

    def test_read_1 (self) :
        r = io.StringIO("1 10\n")
        m = collatz_read_1(r)
        i, j = list(next(m))
        self.assertTrue(i ==  1)
        self.assertTrue(j == 10)

    def test_read_2 (self) :
        r = io.StringIO("1 10\n")
        m = collatz_read_2(r)
        i, j = list(next(m))
        self.assertTrue(i ==  1)
        self.assertTrue(j == 10)

    def test_read_3 (self) :
        r = io.StringIO("1 10\n")
        m = collatz_read_3(r)
        i, j = list(next(m))
        self.assertTrue(i ==  1)
        self.assertTrue(j == 10)

    def test_read_1_2 (self) :
        r = io.StringIO("3 1000\n")
        m = collatz_read_1(r)
        i, j = list(next(m))
        self.assertTrue(i ==  3)
        self.assertTrue(j == 1000)

    def test_read_2_2 (self) :
        r = io.StringIO("3 1000\n")
        m = collatz_read_2(r)
        i, j = list(next(m))
        self.assertTrue(i ==  3)
        self.assertTrue(j == 1000)

    def test_read_3_2 (self) :
        r = io.StringIO("3 1000\n")
        m = collatz_read_3(r)
        i, j = list(next(m))
        self.assertTrue(i ==  3)
        self.assertTrue(j == 1000)

    def test_read_1_3 (self) :
        r = io.StringIO("1 100000\n")
        m = collatz_read_1(r)
        i, j = list(next(m))
        self.assertTrue(i ==  1)
        self.assertTrue(j == 100000)

    def test_read_2_3 (self) :
        r = io.StringIO("1 100000\n")
        m = collatz_read_2(r)
        i, j = list(next(m))
        self.assertTrue(i ==  1)
        self.assertTrue(j == 100000)

    def test_read_3_3 (self) :
        r = io.StringIO("1 100000\n")
        m = collatz_read_3(r)
        i, j = list(next(m))
        self.assertTrue(i ==  1)
        self.assertTrue(j == 100000)

    def test_read_1_4 (self) :
        r = io.StringIO("2 3\n")
        m = collatz_read_1(r)
        i, j = list(next(m))
        self.assertTrue(i ==  2)
        self.assertTrue(j == 3)

    def test_read_2_4 (self) :
        r = io.StringIO("2 3\n")
        m = collatz_read_2(r)
        i, j = list(next(m))
        self.assertTrue(i ==  2)
        self.assertTrue(j == 3)

    def test_read_3_4 (self) :
        r = io.StringIO("2 3\n")
        m = collatz_read_3(r)
        i, j = list(next(m))
        self.assertTrue(i ==  2)
        self.assertTrue(j == 3)

    def test_read_1_5 (self) :
        r = io.StringIO("15 5\n")
        m = collatz_read_1(r)
        i, j = list(next(m))
        self.assertTrue(i ==  15)
        self.assertTrue(j == 5)

    def test_read_2_5 (self) :
        r = io.StringIO("15 5\n")
        m = collatz_read_2(r)
        i, j = list(next(m))
        self.assertTrue(i ==  15)
        self.assertTrue(j == 5)

    def test_read_3_5 (self) :
        r = io.StringIO("15 5\n")
        m = collatz_read_3(r)
        i, j = list(next(m))
        self.assertTrue(i ==  15)
        self.assertTrue(j == 5)

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

    def test_eval_5 (self) :
       v = collatz_eval(1, 100000)
       self.assertTrue(v == 351)

    def test_eval_6 (self) :
        v = collatz_eval(210, 201)
        self.assertTrue(v == 89)

    def test_eval_7 (self) :
        v = collatz_eval(1, 125)
        self.assertTrue(v == 119)

    def test_eval_7 (self) :
        v = collatz_eval(582394, 583749)
        self.assertTrue(v == 328)

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = io.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertTrue(w.getvalue() == "1 10 20\n")

    def test_print_2 (self) :
        w = io.StringIO()
        collatz_print(w, 201, 210, 89)
        self.assertTrue(w.getvalue() == "201 210 89\n")

    def test_print_3 (self) :
        w = io.StringIO()
        collatz_print(w, 10, 10, 7)
        self.assertTrue(w.getvalue() == "10 10 7\n")

    def test_print_4 (self) :
        w = io.StringIO()
        collatz_print(w, 100, 200, 125)
        self.assertTrue(w.getvalue() == "100 200 125\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = io.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve2 (self) :
        r = io.StringIO("10 1\n200 100\n210 201\n1000 900\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "10 1 20\n200 100 125\n210 201 89\n1000 900 174\n")

    def test_solve3 (self) :
        r = io.StringIO("999999 1000000\n10 10\n210 201\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "999999 1000000 259\n10 10 7\n210 201 89\n")

    def test_solve4 (self) :
        r = io.StringIO("999999 1000000\n1000000 999999\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "999999 1000000 259\n1000000 999999 259\n")

# ----
# main
# ----

print("TestCollatz.py")
unittest.main()
print("Done.")