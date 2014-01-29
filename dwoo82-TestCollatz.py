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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, do_collatz

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

	def test_read_multiline (self) :
		r = StringIO.StringIO("1 2\n3 4\n")
		p = collatz_read(r)
		(i, j) = p.next()
		self.assert_(i == 1)
		self.assert_(j == 2)
		(i,j) = p.next()
		self.assert_(i == 3)
		self.assert_(j == 4)

	def test_read_reverse (self) :
		r = StringIO.StringIO("10 1\n")
		p = collatz_read(r)
		(i,j) = p.next()
		self.assert_(i == 10)
		self.assert_(j == 1)

	def test_read_bad_input (self) :
		r = StringIO.StringIO("\n")
		p = collatz_read(r)
		i = p.next()
		self.assert_(i == [])

	# ----------
	# do_collatz
	# ----------

	def test_do_collatz_1 (self) :
		v = do_collatz(1)
		self.assert_(v == 1)
	def test_do_collatz_2 (self) :
		v = do_collatz(2)
		self.assert_(v == 2)
	def test_do_collatz_3 (self) :
		v = do_collatz(10)
		self.assert_(v == 7)
	def test_do_collatz_4 (self) :
		v = do_collatz(1024)
		self.assert_(v == 11)
	def test_do_collatz_5 (self) :
		v = do_collatz(9)
		self.assert_(v == 20)

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

	def test_eval_identical_input_1 (self) :
		v = collatz_eval((2, 2))
		self.assert_(v == 2)

	def test_eval_identical_input_2 (self) :
		v = collatz_eval((10, 10))
		self.assert_(v == 7)

	def test_eval_reverse_input_1 (self) :
		v = collatz_eval((10, 1))
		self.assert_(v == 20)

	def test_eval_reverse_input_2 (self) :
		v = collatz_eval((1000, 900))
		self.assert_(v == 174)

    # -----
    # print
    # -----

	def test_print_1 (self) :
		w = StringIO.StringIO()
		collatz_print(w, (1, 10), 20)
		self.assert_(w.getvalue() == "1 10 20\n")

	def test_print_2 (self) :
		w = StringIO.StringIO()
		collatz_print(w, (2, 1), 3)
		self.assert_(w.getvalue() == "2 1 3\n")

	def test_print_3 (self) :
		w = StringIO.StringIO()
		collatz_print(w, (10, 20), 100)
		self.assert_(w.getvalue() == "10 20 100\n")

    # -----
    # solve
    # -----

	def test_solve (self) :
		r = StringIO.StringIO("1 10\n")
		w = StringIO.StringIO()
		collatz_solve(r, w)
		self.assert_(w.getvalue() == "1 10 20\n")

	def test_solve_multiline (self) :
		r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
		w = StringIO.StringIO()
		collatz_solve(r, w)
		self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

	def test_solve_reverse_input (self) :
		r = StringIO.StringIO("10 1\n")
		w = StringIO.StringIO()
		collatz_solve(r, w)
		self.assert_(w.getvalue() == "10 1 20\n")

	def test_solve_reverse_multiline (self) :
		r = StringIO.StringIO("10 1\n200 100\n")
		w = StringIO.StringIO()
		collatz_solve(r, w)
		self.assert_(w.getvalue() == "10 1 20\n200 100 125\n")
		

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
