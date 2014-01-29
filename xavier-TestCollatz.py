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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------

class TestCollatz (unittest.TestCase) :
    # ----
    # read
    # ----

    def test_read_basic (self) :
        r = io.StringIO("1 10\n")
        m = collatz_read(r)
        i, j = list(next(m))
        self.assertTrue(i ==  1)
        self.assertTrue(j == 10)

    def test_read_backwards (self) :
        r = io.StringIO("10 1\n")
        m = collatz_read(r)
        i, j = list(next(m))
        self.assertTrue(i ==  10)
        self.assertTrue(j == 1)

    def test_read_big (self) :
        r = io.StringIO("999999 1000000\n")
        m = collatz_read(r)
        i, j = list(next(m))
        self.assertTrue(i ==  999999)
        self.assertTrue(j == 1000000)

    # ----
    # eval
    # ----

    def test_eval_basic (self) :
        v = collatz_eval(1, 10)
        self.assertTrue(v == 20)

    def test_eval_big (self) :
        v = collatz_eval(1, 1000000)
        self.assertTrue(v == 525)

    def test_eval_backwards (self) :
        v = collatz_eval(456456, 123123)
        self.assertTrue(v == 449)

    def test_eval_singleton (self) :
        v = collatz_eval(4, 4)
        self.assertTrue(v == 3)

    def test_eval_one (self) :
        v = collatz_eval(1, 1)
        self.assertTrue(v == 1)     

    # -----
    # print
    # -----

    def test_print_basic (self) :
        w = io.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertTrue(w.getvalue() == "1 10 20\n")

    def test_print_big (self) :
        w = io.StringIO()
        collatz_print(w, 1, 1000000, 525)
        self.assertTrue(w.getvalue() == "1 1000000 525\n")  

    def test_print_one (self) :
        w = io.StringIO()
        collatz_print(w, 1, 1, 1)
        self.assertTrue(w.getvalue() == "1 1 1\n") 

    # -----
    # solve
    # -----

    def test_solve_multi (self) :
        r = io.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_same (self) :
        r = io.StringIO("1 10\n1 10\n1 10\n1 10\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "1 10 20\n1 10 20\n1 10 20\n1 10 20\n")

    def test_solve_bigs (self) :
        r = io.StringIO("119756 756423\n1000000 1\n951230 872345\n123456 987654\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "119756 756423 509\n1000000 1 525\n951230 872345 507\n123456 987654 525\n")

    def test_solve_one (self) :
        r = io.StringIO("1 1\n1 10\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "1 1 1\n1 10 20\n")        

    def test_solve_backwards (self) :
        r = io.StringIO("15 3\n200 1\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "15 3 20\n200 1 125\n")          

# ----
# main
# ----

print("TestCollatz.py")
unittest.main()
print("Done.")
