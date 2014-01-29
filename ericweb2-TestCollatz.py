#!/usr/bin/env python

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2014
# Glenn P. Downing
# -------------------------------

"""
To test the program:
    % python TestCollatz.py &> TestCollatz.out
    % chmod ugo+x TestCollatz.py
    % TestCollatz.py &> TestCollatz.out
"""

# -------
# imports
# -------

import StringIO
import unittest

from Collatz import collatz_read, collatz_eval, populate_cache, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------

class TestCollatz (unittest.TestCase) :
    # ----
    # read
    # ----

    def test_read_1 (self) :
        r = StringIO.StringIO("1 10\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] == 10)
        b = collatz_read(r, a)
        self.assert_(b    == False)

    def test_read_2 (self) :
        r = StringIO.StringIO("1 999999\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] == 999999)
        b = collatz_read(r, a)
        self.assert_(b    == False)

    def test_read_3 (self) :
        r = StringIO.StringIO("999999 999999\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  999999)
        self.assert_(a[1] == 999999)
        b = collatz_read(r, a)
        self.assert_(b    == False)

    def test_read_4 (self) :
        r = StringIO.StringIO("999999 1\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  999999)
        self.assert_(a[1] == 1)
        b = collatz_read(r, a)
        self.assert_(b    == False)

    def test_read_5 (self) :
        r = StringIO.StringIO("1 10\n100 200\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] == 10)
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] == 100)
        self.assert_(a[1] == 200)
        b = collatz_read(r, a)
        self.assert_(b    == False)

    def test_read_6 (self) :
        r = StringIO.StringIO("")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == False)
        self.assert_(a    == [0, 0])
        b = collatz_read(r, a)
        self.assert_(b    == False)

    def test_read_7 (self) :
        r = StringIO.StringIO("1993 9019\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] == 1993)
        self.assert_(a[1] == 9019)
        b = collatz_read(r, a)
        self.assert_(b    == False)

    def test_read_8 (self) :
        r = StringIO.StringIO("4284 6099\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] == 4284)
        self.assert_(a[1] == 6099)

    def test_read_9 (self) :
        r = StringIO.StringIO("20 5086\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==   20)
        self.assert_(a[1] == 5086)
        b = collatz_read(r, a)
        self.assert_(b    == False)

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
        v = collatz_eval(7704, 1354)
        self.assert_(v == 262)

    def test_eval_6 (self) :
        v = collatz_eval(27831, 19841)
        self.assert_(v == 308)

    def test_eval_7 (self) :
        v = collatz_eval(18177, 27780)
        self.assert_(v == 308)

    def test_eval_8 (self) :
        v = collatz_eval(159, 27)
        self.assert_(v == 122)

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_print_2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 977, 745, 179)
        self.assert_(w.getvalue() == "977 745 179\n")

    def test_print_3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 13, 17, 18)
        self.assert_(w.getvalue() == "13 17 18\n")

    def test_print_4 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 747, 638, 171)
        self.assert_(w.getvalue() == "747 638 171\n")

    def test_print_5 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 950, 827, 179)
        self.assert_(w.getvalue() == "950 827 179\n")

    # -----
    # populate_cache
    # -----

    def test_populate_cache_1 (self) :
        cache = {2:2}
        h = [2, 1]
        begin = 1
        end = 2
        populate_cache(cache, h, begin, end)
        self.assert_(cache[1] == 1)
        
    def test_populate_cache_2 (self) :
        cache = {10:7}
        h = [10, 5, 16, 8, 4, 2, 1]
        begin = 1
        end = 20
        populate_cache(cache, h, begin, end)
        self.assert_(cache[5]  == 6)
        self.assert_(cache[16] == 5)
        self.assert_(cache[8]  == 4)
        self.assert_(cache[4]  == 3)
        self.assert_(cache[2]  == 2)
        self.assert_(cache[1]  == 1)
        
    def test_populate_cache_3 (self) :
        cache = {100:26}
        h = [100, 50, 25, 76, 38, 19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 02, 10, 5, 16, 8, 4, 2, 1]
        begin = 1
        end = 200
        populate_cache(cache, h, begin, end)
        self.assert_(cache[100] == 26)
        self.assert_(cache[50] == 25)
        self.assert_(cache[25] == 24)
        self.assert_(cache[76] == 23)
        self.assert_(cache[38] == 22)
        self.assert_(cache[19] == 21)
        self.assert_(cache[58] == 20)
        self.assert_(cache[29] == 19)
        self.assert_(cache[88] == 18)
        self.assert_(cache[44] == 17)
        self.assert_(cache[22] == 16)
        self.assert_(cache[11] == 15)
        self.assert_(cache[34] == 14)
        self.assert_(cache[17] == 13)
        self.assert_(cache[52] == 12)
        self.assert_(cache[26] == 11)
        self.assert_(cache[13] == 10)
        self.assert_(cache[40] == 9)
        self.assert_(cache[20] == 8)
        self.assert_(cache[10] == 7)
        self.assert_(cache[5]  == 6)
        self.assert_(cache[16] == 5)
        self.assert_(cache[8]  == 4)
        self.assert_(cache[4]  == 3)
        self.assert_(cache[2]  == 2)
        self.assert_(cache[1]  == 1)
        
    def test_populate_cache_4 (self) :
        cache = {7:17}
        h = [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        begin = 1
        end = 100
        populate_cache(cache, h, begin, end)
        self.assert_(cache[22] == 16)
        self.assert_(cache[11] == 15)
        self.assert_(cache[34] == 14)
        self.assert_(cache[17] == 13)
        self.assert_(cache[52] == 12)
        self.assert_(cache[26] == 11)
        self.assert_(cache[13] == 10)
        self.assert_(cache[40] == 9)
        self.assert_(cache[20] == 8)
        self.assert_(cache[10] == 7)
        self.assert_(cache[5]  == 6)
        self.assert_(cache[16] == 5)
        self.assert_(cache[8]  == 4)
        self.assert_(cache[4]  == 3)
        self.assert_(cache[2]  == 2)
        self.assert_(cache[1]  == 1)
        
    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2 (self) :
        r = StringIO.StringIO("836 977\n30216 98463\n424 847\n480974 656584\n10 25\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "836 977 179\n30216 98463 351\n424 847 171\n480974 656584 509\n10 25 24\n")

    def test_solve_3 (self) :
        r = StringIO.StringIO("423 816\n23 52\n856 156\n743 896\n55 4\n540011 430664\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "423 816 171\n23 52 112\n856 156 171\n743 896 179\n55 4 113\n540011 430664 470\n")

    def test_solve_4 (self) :
        r = StringIO.StringIO("")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "")

    def test_solve_5 (self) :
        r = StringIO.StringIO("31 48\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "31 48 110\n")
        
        
        
# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
