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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_init_cache

# -----------
# TestCollatz
# -----------

class TestCollatz (unittest.TestCase) :
    # ----
    # read
    # ----

    def test_read (self) :
        r = StringIO.StringIO("1 10\n")
        p = collatz_read(r)
        (i, j) = p.next()
        self.assert_(i ==  1)
        self.assert_(j == 10)

    def test_read_1 (self) :
        r = StringIO.StringIO("0 10\n")
        p = collatz_read(r)
        (i, j) = p.next()
        self.assert_(i ==  0)
        self.assert_(j == 10)

    def test_read_2 (self) :
        r = StringIO.StringIO("10 1\n")
        p = collatz_read(r)
        (i, j) = p.next()
        self.assert_(i ==  10)
        self.assert_(j == 1)

    def test_read_3 (self) :
        r = StringIO.StringIO("100 1000\n")
        p = collatz_read(r)
        (i, j) = p.next()
        self.assert_(i ==  100)
        self.assert_(j == 1000)  

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

    def test_eval_5 (self) :
        v = collatz_eval((901, 936))
        self.assert_(v == 130)

    def test_eval_6 (self) :
        v = collatz_eval((901, 935))
        self.assert_(v == 130)

    def test_eval_7 (self) :
        v = collatz_eval((1, 1001))
        self.assert_(v == 179)

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, (1, 10), 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_print_1 (self) :
        w = StringIO.StringIO()
        collatz_print(w, (0, 0), 0)
        self.assert_(w.getvalue() == "0 0 0\n")

    def test_print_2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, (9, 99), 999)
        self.assert_(w.getvalue() == "9 99 999\n")

    def test_print_3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, (1, 1), 1)
        self.assert_(w.getvalue() == "1 1 1\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve (self) :
        r = StringIO.StringIO("9 9\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "9 9 20\n")

    def test_solve (self) :
        r = StringIO.StringIO("10 1\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "10 1 20\n")

    def test_solve (self) :
        r = StringIO.StringIO("74 686\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "74 686 145\n")

    # -----
    # init_cache
    # -----
    def test_init_cache1 (self):
        cache = {}
        collatz_init_cache(cache)
        i = 1
        j = 1

        while(i <= 4194304):

            self.assert_(cache[i] == j)
            i = i * 2
            j = j + 1

    def test_init_cache2 (self):
        cache = {}
        collatz_init_cache(cache)            
        self.assert_(cache[9] == 3 + cache[7])

    def test_init_cache3 (self):
        cache = {}
        collatz_init_cache(cache)            
        self.assert_(10001 not in cache)


# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
