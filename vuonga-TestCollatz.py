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

from Collatz import collatz_read, collatz_eval, cycle_length, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------

class TestCollatz (unittest.TestCase) :
    # ----
    # read
    # ----

    def test_read_1 (self) :
        r = io.StringIO("1 10\n")
        a = [0, 0]
        b = collatz_read(r, a)
        i, j = a
        self.assertTrue(b == True)
        self.assertTrue(i ==  1)
        self.assertTrue(j == 10)

    def test_read_2 (self) :
        r = io.StringIO("10 1\n")
        a = [0, 0]
        b = collatz_read(r, a)
        i, j = a
        self.assertTrue(b == True)
        self.assertTrue(i ==  10)
        self.assertTrue(j == 1)

    def test_read_3 (self) :
        r = io.StringIO("1000 1000\n")
        a = [0, 0]
        b = collatz_read(r, a)
        i, j = a
        self.assertTrue(b == True)
        self.assertTrue(i ==  1000)
        self.assertTrue(j == 1000)

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
    # cycle_length
    # -----

    def test_cycle_1 (self) :
        w = io.StringIO()
        v = cycle_length(5)
        self.assertTrue(v == 6)

    def test_cycle_2 (self) :
        w = io.StringIO()
        v = cycle_length(10)
        self.assertTrue(v == 7)
        
    def test_cycle_3 (self) :
        w = io.StringIO()
        v = cycle_length(10)
        self.assertTrue(v == 7)


    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = io.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertTrue(w.getvalue() == "1 10 20\n")

    def test_print_2 (self) :
        w = io.StringIO()
        collatz_print(w, 978, 978, 50)
        self.assertTrue(w.getvalue() == "978 978 50\n")
        
    def test_print_3 (self) :
        w = io.StringIO()
        collatz_print(w, 4835, 4840, 166)
        self.assertTrue(w.getvalue() == "4835 4840 166\n")
        
    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = io.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2 (self) :
        r = io.StringIO("10 12\n10 100\n210 201\n4862 4863\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "10 12 15\n10 100 119\n210 201 89\n4862 4863 166\n")


    def test_solve_3 (self) :
        r = io.StringIO("10 16\n6 12992\n10777 42768\n10 1 20\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "10 16 18\n6 12992 268\n10777 42768 324\n10 1 20\n")
      
# ----
# main
# ----

print("TestCollatz.py")
unittest.main()
print("Done.")
