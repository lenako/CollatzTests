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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------

class TestCollatz (unittest.TestCase) :
    # ----
    # read
    # ----

    def test_read (self) :
        r = StringIO.StringIO("123 321\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  123)
        self.assert_(a[1] == 321)

    #Ver's read tests

    def test_read_1 (self) :
        r = StringIO.StringIO("1 10\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 1)
        self.assert_(a[1] == 10)
        b = collatz_read(r, a)
        self.assert_(b == False)

    def test_read_2 (self) :
        r = StringIO.StringIO("1 999999\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 1)
        self.assert_(a[1] == 999999)
        b = collatz_read(r, a)
        self.assert_(b == False)

    def test_read_3 (self) :
        r = StringIO.StringIO("999999 999999\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 999999)
        self.assert_(a[1] == 999999)
        b = collatz_read(r, a)
        self.assert_(b == False)

    def test_read_4 (self) :
        r = StringIO.StringIO("999999 1\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 999999)
        self.assert_(a[1] == 1)
        b = collatz_read(r, a)
        self.assert_(b == False)

    def test_read_5 (self) :
        r = StringIO.StringIO("1 10\n100 200\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 1)
        self.assert_(a[1] == 10)
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 100)
        self.assert_(a[1] == 200)
        b = collatz_read(r, a)
        self.assert_(b == False)

    def test_read_6 (self) :
        r = StringIO.StringIO("")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == False)
        self.assert_(a == [0, 0])
        b = collatz_read(r, a)
        self.assert_(b == False)

    def test_read_7 (self) :
        r = StringIO.StringIO("7823 5555\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 7823)
        self.assert_(a[1] == 5555)
        b = collatz_read(r, a)
        self.assert_(b == False)

    def test_read_8 (self) :
        r = StringIO.StringIO("726 8512\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 726)
        self.assert_(a[1] == 8512)

    def test_read_9 (self) :
        r = StringIO.StringIO("20 7034\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 20)
        self.assert_(a[1] == 7034)
        b = collatz_read(r, a)
        self.assert_(b == False)

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

    #Ver's eval tests

    def test_eval_5 (self) :
        v = collatz_eval(4853, 6325)
        self.assert_(v == 262)

    def test_eval_6 (self) :
        v = collatz_eval(253, 3375)
        self.assert_(v == 217)

    def test_eval_7 (self) :
        v = collatz_eval(9599, 9822)
        self.assert_(v == 198)

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    #Ver's print tests

    def test_print_2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 3191, 4539, 238)
        self.assert_(w.getvalue() == "3191 4539 238\n")

    def test_print_3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1861, 11, 182)
        self.assert_(w.getvalue() == "1861 11 182\n")

    def test_print_4 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 175, 9887, 262)
        self.assert_(w.getvalue() == "175 9887 262\n")

    def test_print_5 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 14, 6396, 262)
        self.assert_(w.getvalue() == "14 6396 262\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    #Ver's solve tests

    def test_solve_1 (self) :
        r = StringIO.StringIO("5265 1265\n8471 5014\n4627 9310\n2757 6909\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "5265 1265 238\n8471 5014 262\n4627 9310 262\n2757 6909 262\n")

    def test_solve_2 (self) :
        r = StringIO.StringIO("5726 3975\n8329 6529\n7333 6666\n1380 461\n10 25\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "5726 3975 236\n8329 6529 257\n7333 6666 257\n1380 461 182\n10 25 24\n")

    def test_solve_3 (self) :
        r = StringIO.StringIO("4306 6036\n8646 3569\n9352 6927\n3604 260\n55 4\n540011 430664\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "4306 6036 236\n8646 3569 262\n9352 6927 260\n3604 260 217\n55 4 113\n540011 430664 470\n")

    def test_solve_4 (self) :
        r = StringIO.StringIO("")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "")

    def test_solve_5 (self) :
        r = StringIO.StringIO("1 2\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 2 2\n")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
