import unittest as u
import session3 as s


class MyTestCase(u.TestCase):
    def test01(self):  # Conversion Method Test
        t1 = s.Temperature(-124.3809, "C")
        t2 = s.Temperature(15.9155, "C")
        self.assertAlmostEqual(15.9155, t1.conversion(t2).value, 4)
        self.assertEqual(t1.scale, t1.conversion(t2).scale)

    def test02(self):  # Conversion Method Test
        t1 = s.Temperature(-496.0484, "F")
        t2 = s.Temperature(395.6072, "K")
        self.assertAlmostEqual(252.423, t1.conversion(t2).value, 4)
        self.assertEqual(t1.scale, t1.conversion(t2).scale)

    def test03(self):  # Addition Method Test
        t1 = s.Temperature(218.36, "K")
        t2 = s.Temperature(-345.0377, "F")
        t3 = t1.addition(t2)
        self.assertAlmostEqual(t1.value + t1.conversion(t2).value, t3.value, 4)
        self.assertEqual(t1.scale, t3.scale)

    def test04(self):  # Addition Method Test
        t1 = s.Temperature(-242.8278, "C")
        t2 = s.Temperature(-75.7804, "F")
        t3 = t1.addition(t2)
        self.assertAlmostEqual(t1.value + t1.conversion(t2).value, t3.value, 4)
        self.assertEqual(t1.scale, t3.scale)

    def test05(self):  # Subtraction Method Test
        t1 = s.Temperature(40.3094, "F")
        t2 = s.Temperature(-57.1392, "K")
        t3 = t1.subtraction(t2)
        self.assertAlmostEqual(t1.value - t1.conversion(t2).value, t3.value, 4)
        self.assertEqual(t1.scale, t3.scale)

    def test06(self):  # Subtraction Method Test
        t1 = s.Temperature(33.3534, "C")
        t2 = s.Temperature(-62.0510, "F")
        t3 = t1.subtraction(t2)
        self.assertAlmostEqual(t1.value - t1.conversion(t2).value, t3.value, 4)
        self.assertEqual(t1.scale, t3.scale)

    def test07(self):  # Multiplication Method Test
        t1 = s.Temperature(296.6771, "K")
        t2 = s.Temperature(212.5461, "C")
        t3 = t1.multiplication(t2)
        self.assertAlmostEqual(t1.value * t1.conversion(t2).value, t3.value, 4)
        self.assertEqual(t1.scale, t3.scale)

    def test08(self):  # Multiplication Method Test
        t1 = s.Temperature(459.263, "F")
        t2 = s.Temperature(5.0754, "F")
        t3 = t1.multiplication(t2)
        self.assertAlmostEqual(t1.value * t1.conversion(t2).value, t3.value, 4)
        self.assertEqual(t1.scale, t3.scale)

    def test09(self):  # Division Method Test
        t1 = s.Temperature(-257.393, "F")
        t2 = s.Temperature(27.3613, "C")
        t3 = t1.division(t2)
        self.assertAlmostEqual(t1.value / t1.conversion(t2).value, t3.value, 4)
        self.assertEqual(t1.scale, t3.scale)

    def test10(self):  # Division Method Test
        t1 = s.Temperature(290.1718, "K")
        t2 = s.Temperature(169.4152, "F")
        t3 = t1.division(t2)
        self.assertAlmostEqual(t1.value / t1.conversion(t2).value, t3.value, 4)
        self.assertEqual(t1.scale, t3.scale)

    def test11(self):  # Zero Division Test
        t1 = s.Temperature(185.3084, "C")
        t2 = s.Temperature(32, "F")
        self.assertRaises(ZeroDivisionError, t1.division, t2)

    def test12(self):  # Zero Result Test
        t1 = s.Temperature(55.5156, "C")
        t2 = s.Temperature(131.92808, "F")
        self.assertRaises(ValueError, t1.subtraction, t2)


def run():
    suite = u.TestLoader().loadTestsFromTestCase(MyTestCase)
    u.TextTestRunner(verbosity=3).run(suite)


run()
