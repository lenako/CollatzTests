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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, cycleLength

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
        
    def test_read_2 (self) :
        r = StringIO.StringIO("1 20\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] == 20)
        
    def test_read_3 (self) :
        r = StringIO.StringIO("20 100\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  20)
        self.assert_(a[1] == 100)
        
        

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
        
    def test_eval_5 (self) :
        v = collatz_eval(84442, 75795)
        self.assert_(v == 351)
        
    # -----------
    # cycleLength
    # -----------
    
    def test_cycleLength_1 (self):
    	v = cycleLength(1)
    	self.assert_(v == 1)

    def test_cycleLength_2 (self):
        v = cycleLength(5)
    	self.assert_(v == 6)
    
    def test_cycleLength_3 (self):
        v = cycleLength(10)
        self.assert_(v == 7)
        
    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")
    
    def test_print_2 (self) :
    	w = StringIO.StringIO()
        collatz_print(w, 1, 20, 21)
        self.assert_(w.getvalue() == "1 20 21\n")
        
    def test_print_3 (self) :
    	w = StringIO.StringIO()
        collatz_print(w, 20, 100, 119)
        self.assert_(w.getvalue() == "20 100 119\n")
             


    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
        
    def test_solve_2 (self): 
        r = StringIO.StringIO("1 20\n20 100\n50 75\n1000 900\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 20 21\n20 100 119\n50 75 116\n1000 900 174\n")
        
    def test_solve_3 (self): 
        r = StringIO.StringIO("3000 2500\n123 456\n2000 8000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "3000 2500 217\n123 456 144\n2000 8000 262\n")
        

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
