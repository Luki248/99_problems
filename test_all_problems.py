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
import p14
import p15
import p16
import p17
import p18
import p19
import p20
import p21
import p22
import p23
import p24
import p25
import p26
import p27
import p28
import p31


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
        self.assertEqual(p07.p07([1, 2, [31, 32], [41, [42, 43]], 5]),
                         [1, 2, 31, 32, 41, 42, 43, 5])

    def test_p08(self):
        self.assertEqual(p08.p08([1, 2, 2, 3, 1, 5, 5, 5, 5]), [1, 2, 3, 1, 5])

    def test_p09(self):
        self.assertEqual(p09.p09([1, 2, 2, 3, 1, 5, 5, 5, 5]),
                         [[1], [2, 2], [3], [1], [5, 5, 5, 5]])

    def test_p10(self):
        self.assertEqual(p10.p10([1, 2, 2, 3, 1, 5, 5, 5, 5]),
                         [[1, 1], [2, 2], [1, 3], [1, 1], [4, 5]])

    def test_p11(self):
        self.assertEqual(p11.p11([1, 2, 2, 3, 1, 5, 5, 5, 5]),
                         [1, [2, 2], 3, 1, [4, 5]])

    def test_p12(self):
        self.assertEqual(p12.p12([1, [2, 2], 3, 1, [4, 5]]),
                         [1, 2, 2, 3, 1, 5, 5, 5, 5])

    def test_p13(self):
        self.assertEqual(p13.p13([1, 2, 2, 3, 1, 5, 5, 5, 5]),
                         [[1, 1], [2, 2], [1, 3], [1, 1], [4, 5]])

    def test_p14(self):
        self.assertEqual(p14.p14([1, 2, 3, 4]), [1, 1, 2, 2, 3, 3, 4, 4])

    def test_p15(self):
        self.assertEqual(p15.p15([1, 2, 3, 4], 3),
                         [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4])

    def test_p16(self):
        self.assertEqual(p16.p16([1, 2, 3, 4, 5, 6, 7, 8, 9], 3),
                         [1, 2, 4, 5, 7, 8])

    def test_p17(self):
        self.assertEqual(p17.p17([1, 2, 3, 4, 5, 6, 7, 8, 9], 3),
                         [[1, 2, 3], [4, 5, 6, 7, 8, 9]])

    def test_p18(self):
        self.assertEqual(
            p18.p18([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 7), [3, 4, 5, 6, 7])

    def test_p19_01(self):
        self.assertEqual(p19.p19([1, 2, 3, 4, 5, 6, 7, 8, 9], 3),
                         [4, 5, 6, 7, 8, 9, 1, 2, 3])

    def test_p19_02(self):
        self.assertEqual(
            p19.p19([1, 2, 3, 4, 5, 6, 7, 8, 9], -2), [8, 9, 1, 2, 3, 4, 5, 6, 7])

    def test_p20(self):
        self.assertEqual(p20.p20([1, 2, 3, 4], 2), [1, 3, 4])

    def test_p21(self):
        self.assertEqual(p21.p21(6, [1, 2, 3, 4], 2), [1, 6, 2, 3, 4])

    def test_p22_01(self):
        self.assertEqual(p22.p22(4, 9), [4, 5, 6, 7, 8, 9])

    def test_p22_02(self):
        self.assertEqual(p22.p22(9, 4), [9, 8, 7, 6, 5, 4])

    def test_p23(self):
        self.assertEqual(len(p23.p23([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)), 3)

    def test_p24(self):
        self.assertEqual(len(p24.p24(6, 49)), 6)

    def test_p25(self):
        self.assertEqual(len(p25.p25([1, 2, 3, 4, 5, 6, 7, 8, 9])), 9)

    def test_p26(self):
        self.assertEqual(len(p26.p26(3, [1, 2, 3, 4])), 3)

    def test_p27a(self):
        self.assertEqual(len(p27.p27a([1, 2, 3, 4, 5, 6, 7, 8, 9])), 362880)

    def test_p27b(self):
        self.assertEqual(len(p27.p27b([1, 2, 3, 4, 5, 6, 7, 8, 9], 2, 2, 5)),
                         362880)

    def test_p28a(self):
        self.assertEqual(p28.p28a([[1, 2], [3], [4, 5, 6, 7], [], [8, 9]]), [[],
                         [3], [1, 2], [8, 9], [4, 5, 6, 7]])

    def test_p28b(self):
        self.assertEqual(p28.p28b([[1, 2], [3], [4, 5, 6, 7], [], [8, 9]]),
                         [[4, 5, 6, 7], [1, 2], [8, 9], [3], []])

    def test_p31(self):
        self.assertEqual(p31.p31(113), True)


if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)
