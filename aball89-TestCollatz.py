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

from Collatz import collatz_read, collatz_eval, collatz_print, \
                    collatz_solve, collatz_single

# -----------
# TestCollatz
# -----------

class TestCollatz (unittest.TestCase) :
    # ----
    # read
    # ----

    def test_read (self) :
        r = io.StringIO("1 10\n")
        a = [0, 0]
        b = collatz_read(r, a)
        i, j = a
        self.assertTrue(b == True)
        self.assertTrue(i ==  1)
        self.assertTrue(j == 10)

    # Lines read where the greater number comes first should be 
    # go to eval accordingly
    def test_read_unordered (self) :
        r = io.StringIO("10 1\n")
        a = [0, 0]
        b = collatz_read(r, a)
        i, j = a
        self.assertTrue(b == True)
        self.assertTrue(i == 10)
        self.assertTrue(j == 1)

    # Lines read where there are less than two words
    # should raise a ValueError
    def test_read_too_few (self) :
        r = io.StringIO("10\n")
        a = [0, 0]
        self.assertRaises(ValueError, collatz_read, r, a)

    # Lines read where there are more than two words
    # should also raise a ValueError
    def test_read_too_many (self) :
        r = io.StringIO("10 1 20\n")
        a = [0, 0]
        self.assertRaises(ValueError, collatz_read, r, a)

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval(1, 10)
        self.assertTrue(v == 20)

    def test_eval_1_unordered (self) :
        v = collatz_eval(10, 1)
        self.assertTrue(v == 20)

    def test_eval_2 (self) :
        v = collatz_eval(100, 200)
        self.assertTrue(v == 125)

    def test_eval_2_unordered (self) :
        v = collatz_eval(200, 100)
        self.assertTrue(v == 125)

    def test_eval_3 (self) :
        v = collatz_eval(201, 210)
        self.assertTrue(v == 89)

    def test_eval_3_unordered (self) :
        v = collatz_eval(210, 201)
        self.assertTrue(v == 89)

    def test_eval_4 (self) :
        v = collatz_eval(900, 1000)
        self.assertTrue(v == 174)

    def test_eval_4_unordered (self) :
        v = collatz_eval(1000, 900)
        self.assertTrue(v == 174)

    def test_eval_bounds_1 (self) :
        self.assertRaises(AssertionError, collatz_eval, 0, 100)

    def test_eval_bounds_2 (self) :
        self.assertRaises(AssertionError, collatz_eval, 1000000, 100)
        
    def test_eval_bounds_3 (self) :
        self.assertRaises(AssertionError, collatz_eval, 100, 0)

    def test_eval_bounds_4 (self) :
        self.assertRaises(AssertionError, collatz_eval, 100, 1000000)

    # ------
    # single
    # ------

    def test_single_1 (self) :
        v = collatz_single(1)
        self.assertTrue(v == 1)

    def test_single_2 (self) :
        v = collatz_single(2)
        self.assertTrue(v == 2)

    def test_single_3 (self) :
        v = collatz_single(3)
        self.assertTrue(v == 8)

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = io.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertTrue(w.getvalue() == "1 10 20\n")

    def test_print_2 (self) :
        w = io.StringIO()
        collatz_print(w, 10, 1, 20)
        self.assertTrue(w.getvalue() == "10 1 20\n")

    def test_print_3 (self) :
        w = io.StringIO()
        collatz_print(w, 201, 210, 89)
        self.assertTrue(w.getvalue() == "201 210 89\n")

    def test_print_4 (self) :
        w = io.StringIO()
        collatz_print(w, 210, 201, 89)
        self.assertTrue(w.getvalue() == "210 201 89\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = io.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_unordered (self) :
        r = io.StringIO("10 1\n200 100\n210 201\n1000 900\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "10 1 20\n200 100 125\n210 201 89\n1000 900 174\n")

    def test_solve_empty (self) :
        r = io.StringIO("")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "")

    def test_solve_same (self) :
        r = io.StringIO("1 1\n2 2\n3 3\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "1 1 1\n2 2 2\n3 3 8\n")

# ----
# main
# ----

print("TestCollatz.py")
unittest.main()
print("Done.")
