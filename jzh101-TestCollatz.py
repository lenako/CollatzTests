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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

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
    
    def test_read2 (self) :
        r = StringIO.StringIO("100 200\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  100)
        self.assert_(a[1] == 200)
    
    def test_read3 (self) :
        r = StringIO.StringIO("201 210\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  201)
        self.assert_(a[1] == 210)

    def test_read4 (self) :
        r = StringIO.StringIO("900 1000\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  900)
        self.assert_(a[1] == 1000)   
		
    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval(1, 10)
        #print ("v: "+ str(v))
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

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")
    
    def test_print2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 100, 200, 125)
        self.assert_(w.getvalue() == "100 200 125\n")

    def test_print3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 201, 210, 89)
        self.assert_(w.getvalue() == "201 210 89\n")
    
    def test_print4 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 2, 3)
        self.assert_(w.getvalue() == "1 2 3\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve2 (self) :
        r = StringIO.StringIO("66 74\n74 65\n62 72\n67 66\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "66 74 116\n74 65 116\n62 72 108\n67 66 28\n")

    def test_solve3 (self) :
        r = StringIO.StringIO("68 56\n90 58\n100 58\n87 66\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "68 56 108\n90 58 116\n100 58 119\n87 66 116\n")
    def test_solve4 (self) :
        r = StringIO.StringIO("53 66\n68 72\n97 75\n87 51\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "53 66 113\n68 72 103\n97 75 119\n87 51 116\n")
# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
