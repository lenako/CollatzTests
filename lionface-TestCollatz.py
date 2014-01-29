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

import StringIO
import unittest

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, evaluate_for_this

# -----------
# TestCollatz
# -----------

class TestCollatz (unittest.TestCase) :
    # ----
    # read
    # ----

    def test_read (self) :
        r = StringIO.StringIO("1 10\n")
        i, j = list(next(collatz_read(r)))
        self.assert_(i ==  1)
        self.assert_(j == 10)
    
    def test_read_robs1 (self) :
        r = StringIO.StringIO("10 1\n")
        i, j = list(next(collatz_read(r)))
        self.assert_(i ==  10)
        self.assert_(j == 1)
    
    def test_read_robs2 (self) :
        r = StringIO.StringIO("")
        i = (collatz_read(r))
        self.assert_(i != True )

    def test_read_robs3 (self) :
        r = StringIO.StringIO("999999 999999\n")
        i, j = list(next(collatz_read(r)))
        self.assert_(i ==  999999)
        self.assert_(j == 999999)

    # -----------------
    # evaluate_for_this
    # -----------------
    
    def test_evaluate_for_this_robs1 (self) :
    	v = evaluate_for_this(1)
    	self.assert_(v == 1)
    	
    def test_evaluate_for_this_robs2 (self) :
    	v = evaluate_for_this(999999)
    	self.assert_(v != 1)
    	
    def test_evaluate_for_this_robs3 (self) :
    	v = evaluate_for_this(2)
    	self.assert_(v == 2)
    	
    # ----
    # eval
    # ----

    def test_eval_robs1 (self) :
        v = collatz_eval((1, 1))
        self.assert_(v == 1)

    def test_eval_robs2 (self) :
        v = collatz_eval((999999, 999999))
        self.assert_(v == 259)

    def test_eval_robs3 (self) :
        v = collatz_eval((1, 999999))
        self.assert_(v == 525)

    def test_eval_1 (self) :
        v = collatz_eval((1, 10))
        self.assert_(v == 20)

    def test_eval_2 (self) :
        v = collatz_eval((100, 200))
        self.assert_(v == 125)

    def test_eval_3 (self) :
        v = collatz_eval((201, 210))
        self.assert_(v == 89)

    def test_eval_4 (self) :
        v = collatz_eval((900, 1000))
        self.assert_(v == 174)

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, (1, 10), 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_print_robs1 (self) :
        w = StringIO.StringIO()
        collatz_print(w, (100, 200), 125)
        self.assert_(w.getvalue() == "100 200 125\n")

    def test_print_robs2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, (201, 210), 89)
        self.assert_(w.getvalue() == "201 210 89\n")
    
    def test_print_robs3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, (900, 1000), 174)
        self.assert_(w.getvalue() == "900 1000 174\n")
    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
    
    def test_solve_robs1 (self):
        r = StringIO.StringIO("1 1\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 1 1\n")

    def test_solve_robs2 (self):
        r = StringIO.StringIO("1 999999\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 999999 525\n")

    def test_solve_robs3 (self):
        r = StringIO.StringIO("1 1\n1 2\n1 3\n1 4\n1 5\n1 6\n1 7\n1 8\n1 9\n1 10\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 1 1\n1 2 2\n1 3 8\n1 4 8\n1 5 8\n1 6 9\n1 7 17\n1 8 17\n1 9 20\n1 10 20\n")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
