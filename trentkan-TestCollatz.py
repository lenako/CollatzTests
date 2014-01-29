#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2014
# Glenn P. Downing
# Contributor: Trent Kan
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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, get_cycle_len

# -----------
# TestCollatz
# -----------

class TestCollatz (unittest.TestCase) :
    # ----
    # read
    # ----

    def test_read1 (self) :
        r = io.StringIO("1 10\n")
        a = [0, 0]
        b = collatz_read(r, a)
        i, j = a
        self.assertTrue(b == True)
        self.assertTrue(i == 1)
        self.assertTrue(j == 10)

    def test_read2 (self) :
        r = io.StringIO("345634 2451\n")
        a = [0, 0]
        b = collatz_read(r, a)
        i, j = a
        self.assertTrue(b == True)
        self.assertTrue(i == 345634)
        self.assertTrue(j == 2451)

    def test_read3 (self) :
        r = io.StringIO("4 400\n")
        a = [0, 0]
        b = collatz_read(r, a)
        i, j = a
        self.assertTrue(b == True)
        self.assertTrue(i == 4)
        self.assertTrue(j == 400)




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

    def test_eval5 (self) :
        v = collatz_eval(50, 25)
        self.assertTrue(v == 112)

    # -----
    # print
    # -----

    def test_print (self) :
        w = io.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertTrue(w.getvalue() == "1 10 20\n")

    def test_print2 (self) :
        w = io.StringIO()
        collatz_print(w, 10, 1, 20)
        self.assertTrue(w.getvalue() == "10 1 20\n")

    def test_print3 (self) :
        w = io.StringIO()
        collatz_print(w, 2, 5, 7)
        self.assertTrue(w.getvalue() == "2 5 7\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = io.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    #tests first optimization    
    def test_solve2 (self) :
        r = io.StringIO("1 100\n50 100\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "1 100 119\n50 100 119\n")

    def test_solve3 (self) :
        r = io.StringIO("1 50\n600 2353\n325 565\n5676 543\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "1 50 112\n600 2353 183\n325 565 144\n5676 543 238\n")
    
    def test_solve4 (self) :
        r = io.StringIO("1 1\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "1 1 1\n")

    # -----
    # get_cycle_len
    # -----
    def test_get_cycle_len1(self) : 
        max_length = [0]
        max_length[0] = 245
        get_cycle_len(10, max_length)
        self.assertTrue(max_length[0] == 245)

    def test_get_cycle_len2 (self) :
        max_length = [0]
        max_length[0] = 4
        get_cycle_len(50, max_length)
        self.assertTrue(max_length[0] == 25)

    def test_get_cycle_len3 (self) :
        max_length = [0]
        max_length[0] = 20
        get_cycle_len(9, max_length)
        self.assertTrue(max_length[0] == 20)


# ----
# main
# ----

print("TestCollatz.py")
unittest.main()
print("Done.")