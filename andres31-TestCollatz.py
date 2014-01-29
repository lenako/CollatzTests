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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_cycle_length

# -----------
# TestCollatz
# -----------

class TestCollatz (unittest.TestCase) :
    # ----
    # read
    # ----

    def test_read_1 (self) :
        r = StringIO.StringIO("1 10\n")
        p = collatz_read(r)
        (i, j) = p.next()
        self.assert_(i ==  1)
        self.assert_(j == 10)

    
    def test_read_2 (self) :
	r = StringIO.StringIO("35 34\n4 5\n")
	p = collatz_read(r)
	(i, j) = p.next()
	(l, m) = p.next()
	self.assert_(i == 35)
	self.assert_(j == 34)
	self.assert_(l == 4)
	self.assert_(m == 5)


    def test_read_3 (self) :
	r = StringIO.StringIO("1 1\n1 1000\n655555 2")
	p = collatz_read(r)
	(i, j) = p.next()
	(l, m) = p.next()
	(n, o) = p.next()
	self.assert_(i == 1)
	self.assert_(j == 1)
	self.assert_(l == 1)
	self.assert_(m == 1000)
	self.assert_(n == 655555)
	self.assert_(o == 2)

    # ------------
    # cycle_length
    # ------------

    def test_cycle_length_1(self) :
	n = 22
	result = collatz_cycle_length(n)
        self.assert_(result == 16)


    def test_cycle_length_2(self) :
	n = 23
	result = collatz_cycle_length(n)
	self.assert_(result == 16)

    def test_cycle_length_3(self) :
	n = 7
	result = collatz_cycle_length(n)
	self.assert_(result == 17)

    def test_cycle_length_4(self) :
	n = 27
	result = collatz_cycle_length(n)
	self.assert_(result == 112)

    def test_cycle_length_5(self) :
	n = 35
	result = collatz_cycle_length(n)
	self.assert_(result == 14)

    # ----
    # eval
    # ----

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

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, (1, 1), 1)
        self.assert_(w.getvalue() == "1 1 1\n")

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, (200, 100), 125)
        self.assert_(w.getvalue() == "200 100 125\n")


    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve (self) :
        r = StringIO.StringIO("1 1\n1 2\n69 47\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 1 1\n1 2 2\n69 47 113\n")

    def test_solve (self) :
        r = StringIO.StringIO("5 10\n8 1\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "5 10 20\n8 1 17\n")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
