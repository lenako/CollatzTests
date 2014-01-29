#!/usr/bin/env python
#__author__ = 'sophiahernandez'

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


class TestCollatz(unittest.TestCase):
    # ----
    # read
    # ----

    def test_read(self):
        r = StringIO.StringIO("1 10\n")
        p = collatz_read(r)
        (i, j) = p.next()
        self.assert_(i == 1)
        self.assert_(j == 10)

    def test_read1(self):
        r = StringIO.StringIO("92 10\n")
        p = collatz_read(r)
        (i, j) = p.next()
        self.assert_(i == 92)
        self.assert_(j == 10)

    def test_read2(self):
        r = StringIO.StringIO("5234 1000\n")
        p = collatz_read(r)
        (i, j) = p.next()
        self.assert_(i == 5234)
        self.assert_(j == 1000)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        v = collatz_eval((1, 10))
        self.assert_(v == 20)

    def test_eval_2(self):
        v = collatz_eval((100, 200))
        self.assert_(v == 125)

    def test_eval_3(self):
        v = collatz_eval((201, 210))
        self.assert_(v == 89)

    def test_eval_4(self):
        v = collatz_eval((900, 1000))
        self.assert_(v == 174)

    # -----
    # print
    # -----

    def test_print(self):
        w = StringIO.StringIO()
        collatz_print(w, (1, 10), 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_print1(self):
        w = StringIO.StringIO()
        collatz_print(w, (6756, 5153), 262)
        self.assert_(w.getvalue() == "6756 5153 262\n")

    def test_print2(self):
        w = StringIO.StringIO()
        collatz_print(w, (3106, 5915), 238)
        self.assert_(w.getvalue() == "3106 5915 238\n")

    # -----
    # solve
    # -----

    def test_solve(self):
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve1(self):
        r = StringIO.StringIO("6756 5153\n3106 5915\n3424 9728\n6211 1489\n957 7807\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "6756 5153 262\n3106 5915 238\n3424 9728 262\n6211 1489 262\n957 7807 262\n")

    def test_solve2(self):
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
