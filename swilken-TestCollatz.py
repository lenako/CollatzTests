#!/usr/bin/env python3

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

    def test_read_reverse (self) :
        r = io.StringIO("10 1\n")
        m = collatz_read_3(r)
        i, j = list(next(m))
        self.assertTrue(i == 10)
        self.assertTrue(j == 1)

    def test_read_none (self) :
        r = io.StringIO("\n")
        m = collatz_read_3(r)
        j = list(next(m))
        self.assertTrue(not j)

    def test_read_blanks (self) :
        r = io.StringIO("\n1 10\n")
        for m in collatz_read_3(r) :
            p = list(m)
            if len(p) == 2 :
                i, j = p
        self.assertTrue(i == 1)
        self.assertTrue(j == 10)
    def test_read_same (self) :
        r = io.StringIO("10 10\n")
        m = collatz_read_3(r)
        i, j = list(next(m))
        self.assertTrue(i == 10)
        self.assertTrue(j == 10)

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
        w = io.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertTrue(w.getvalue() == "1 10 20\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = io.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_reverse (self) :
        r = io.StringIO("10 1\n200 100\n210 201\n1000 900\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "10 1 20\n200 100 125\n210 201 89\n1000 900 174\n")

# ----
# main
# ----

print("TestCollatz.py")
unittest.main()
print("Done.")
