import unittest as u
import session3 as s


class MyTestCase(u.TestCase):
    def test01(self):
        t1 = s.Temperature(-124.3809, "C")
        t2 = s.Temperature(15.9155, "C")
        self.assertAlmostEqual(15.9155, t1.conversion(t2).value)
        self.assertEqual(t1.scale, t1.conversion(t2).scale )

    def test02(self):
        t1 = s.Temperature(-496.0484, "F")
        t2 = s.Temperature(395.6072, "K")
        self.assertAlmostEqual(252.423, t1.conversion(t2).value)
        self.assertEqual(t1.scale, t1.conversion(t2).scale)

    def test03(self):
        t1 = s.Temperature(218.36, "K")
        t2 = s.Temperature(-345.0377, "F")
        t3 = t1.add(t2)
        self.assertAlmostEqual(282.0446, t3.value)
        self.assertEqual(t1.scale, t3.scale)

    def test04(self):
        t1 = s.Temperature(-242.8278, "C")
        t2 = s.Temperature(-75.7804, "F")
        t3 = t1.add(t2)
        self.assertAlmostEqual(-302.7058, t3.value)
        self.assertEqual(t1.scale, t3.scale)

    def test05(self):
        t1 = s.Temperature(40.3094, "F")
        t2 = s.Temperature(-57.1392, "K")
        t3 = t1.substraction(t2)
        self.assertAlmostEqual(602.823 , t3.value)
        self.assertEqual(t1.scale, t3.scale)

    def test06(self):
        t1 = s.Temperature()
        t2 = s.Temperature()
        t3 = t1.substraction(t2)
        self.assertAlmostEqual( , t3.value)
        self.assertEqual(t1.scale, t3.scale)

    def test07(self):
        t1 = s.Temperature()
        t2 = s.Temperature()
        t3 = t1.multiply(t2)
        self.assertAlmostEqual( , t3.value)
        self.assertEqual(t1.scale, t3.scale)

    def test08(self):
        t1 = s.Temperature()
        t2 = s.Temperature()
        t3 = t1.multiply(t2)
        self.assertAlmostEqual( , t3.value)
        self.assertEqual(t1.scale, t3.scale)

    def test09(self):
        t1 = s.Temperature()
        t2 = s.Temperature()
        t3 = t1.division(t2)
        self.assertAlmostEqual( , t3.value)
        self.assertEqual(t1.scale, t3.scale)

    def test10(self):
        t1 = s.Temperature()
        t2 = s.Temperature()
        t3 = t1.division(t2)
        self.assertAlmostEqual( , t3.value)
        self.assertEqual(t1.scale, t3.scale)

    def test11(self):
        t1 = s.Temperature()
        t2 = s.Temperature()
        t3 = t1.add(t2)
        self.assertAlmostEqual( , t3.value)
        self.assertEqual(t1.scale, t3.scale)

    def test12(self):
        t1 = s.Temperature()
        t2 = s.Temperature()
        t3 = t1.add(t2)
        self.assertAlmostEqual( , t3.value)
        self.assertEqual(t1.scale, t3.scale)


def run():
    suite = u.TestLoader().loadTestsFromTestCase(MyTestCase)
    u.TextTestRunner(verbosity=3).run(suite)