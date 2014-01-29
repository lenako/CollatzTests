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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_count

# -----------
# TestCollatz
# -----------

class TestCollatz (unittest.TestCase) :

    # ----
    # Count
    # ----
    def test_count_1(self) :
        self.assertTrue(collatz_count(1) == 1)    
        
    def test_count_2(self) :
        self.assertTrue(collatz_count(2) == 2)

    def test_count_3(self) :
        self.assertTrue(collatz_count(999999) == 259)  
     
    def test_count_4(self) :
        self.assertTrue(collatz_count(1001) == 143)  
        
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
        r = io.StringIO("1 999999\n")
        a = [0, 0]
        b = collatz_read(r, a)
        i, j = a
        self.assertTrue(b == True)
        self.assertTrue(i == 1)
        self.assertTrue(j == 999999)

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
        v = collatz_eval(1, 1000)
        self.assertTrue(v == 179)
        
    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = io.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertTrue(w.getvalue() == "1 10 20\n")

    def test_print_2 (self) :
        w = io.StringIO()
        collatz_print(w, -1, -1, -1)
        self.assertTrue(w.getvalue() == "-1 -1 -1\n")
        
    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = io.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
        
    def test_solve_2 (self) :
        r = io.StringIO("1 1\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "1 1 1\n")

# ----
# main
# ----

print("TestCollatz.py")
unittest.main()
print("Done.")
