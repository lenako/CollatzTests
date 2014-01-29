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

from Collatz import collatz_read, collatz_cycle_length, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------

class TestCollatz (unittest.TestCase) :
    # ----
    # read
    # ----

    def test_read (self) :
        r = StringIO.StringIO("1 10\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] == 10)

    def test_read_alpha(self):
        r = StringIO.StringIO("1 alpha\n")
        a = [0,0]
        self.assertRaises(ValueError, collatz_read, r, a)
   
    def test_read_multinumber(self):
        r = StringIO.StringIO("4 8 15 16 23 42\n")
        a = [0,0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] == 4)
        self.assert_(a[1] == 8)
        
	 
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

    def test_eval_4 (self) :
        v = collatz_eval(1, 5)
        self.assert_(v == 8)

    # -----
    # cycle length
    # -----

    def test_cycle_length_1 (self):
        self.assert_( collatz_cycle_length(1) == 1 );

    def test_cycle_length_2 (self):
        self.assert_( collatz_cycle_length(2) == 2 );

    def test_cycle_length_3 (self):
        self.assert_( collatz_cycle_length(3) == 8 );

    def test_cycle_length_zero (self):
        self.assertRaises(AssertionError, collatz_cycle_length, 0);

    def test_cycle_length_negative (self):
        self.assertRaises(AssertionError, collatz_cycle_length, -55);

    def test_cycle_length_5 (self):
        self.assert_( collatz_cycle_length(5) == 6 );



    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_print_2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 5, 8)
        self.assert_(w.getvalue() == "1 5 8\n")

    def test_print_negative (self) :
        w = StringIO.StringIO()
        collatz_print(w, -10, 0, 0)
        self.assert_(w.getvalue() == "-10 0 0\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")


# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
