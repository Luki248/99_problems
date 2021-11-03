#!/usr/bin/env python3

# Test all Solution

import unittest

import p01
import p02
import p03
import p04
import p05
import p06
import p07
import p08
import p09
import p10
import p11
import p12
import p13


class TestSolutionsMethods(unittest.TestCase):

    def test_p01(self):
        self.assertEqual(p01.p01([1, 2, 3, 4]), 4)

    def test_p02(self):
        self.assertEqual(p02.p02([1, 2, 3, 4]), [3, 4])

    def test_p02(self):
        self.assertEqual(p02.p02([1, 2]), [1, 2])

    def test_p03(self):
        input = [1, 2, 3, 4]
        self.assertEqual(p03.p03(input, 3), input[3])

    def test_p04(self):
        input = [1, 2, 3, 4]
        self.assertEqual(p04.p04(input), len(input))

    def test_p05_01(self):
        input = [1, 2, 3, 4]
        result = input.copy()
        result.reverse()
        self.assertEqual(p05.p05(input), result)

    def test_p05_02(self):
        input = [1, 2, 3, 4, 5]
        result = input.copy()
        result.reverse()
        self.assertEqual(p05.p05(input), result)

    def test_p06_01(self):
        self.assertEqual(p06.p06([1, 2, 3, 4]), False)

    def test_p06_02(self):
        self.assertEqual(p06.p06([1, 2, 3, 2, 1]), True)

    def test_p07(self):
        self.assertEqual(p07.p07([1, 2, [31, 32], [41, [42, 43]], 5]), [
                         1, 2, 31, 32, 41, 42, 43, 5])

    def test_p08(self):
        self.assertEqual(p08.p08([1, 2, 2, 3, 1, 5, 5, 5, 5]), [1, 2, 3, 1, 5])

    def test_p09(self):
        self.assertEqual(p09.p09([1, 2, 2, 3, 1, 5, 5, 5, 5]), [
                         [1], [2, 2], [3], [1], [5, 5, 5, 5]])

    def test_p10(self):
        self.assertEqual(p10.p10([1, 2, 2, 3, 1, 5, 5, 5, 5]), [
                         [1, 1], [2, 2], [1, 3], [1, 1], [4, 5]])

    def test_p11(self):
        self.assertEqual(p11.p11([1, 2, 2, 3, 1, 5, 5, 5, 5]), [
                         1, [2, 2], 3, 1, [4, 5]])

    def test_p12(self):
        self.assertEqual(p12.p12([1, [2, 2], 3, 1, [4, 5]]), [
                         1, 2, 2, 3, 1, 5, 5, 5, 5])

    def test_p13(self):
        self.assertEqual(p13.p13([1, 2, 2, 3, 1, 5, 5, 5, 5]), [
                         [1, 1], [2, 2], [1, 3], [1, 1], [4, 5]])


if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)
