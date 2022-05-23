import unittest as u
import session2 as s


class MyTests(u.TestCase):
    def test01(self):  # Conversion Test
        t1 = s.Temperature(249.4426, "C")
        t2 = s.Temperature(8.1888, "F")
        t3 = t1.conversion(t2)
        self.assertAlmostEqual(-13.2284444, t3.value)
        self.assertEqual("C", t3.scale)

    def test02(self):  # Conversion Test
        t1 = s.Temperature(241.0029, "C")
        t2 = s.Temperature(-270.1657, "K")
        t3 = t1.conversion(t2)
        self.assertAlmostEqual(-543.3157, t3.value)
        self.assertEqual("C", t3.scale)

    def test03(self):
        t1 = s.Temperature(-173.7856, "F")
        t2 = s.Temperature(317.6799, "K")
        t3 = t1.add(t2)
        self.assertAlmostEqual(-61.63178, t3.value)
        self.assertEqual("F", t3.scale)

    def test04(self):
        t1 = s.Temperature(-43.0363, "K")
        t2 = s.Temperature(365.3039, "F")
        t3 = t1.add(t2)
        self.assertAlmostEqual(415.28253333, t3.value)
        self.assertEqual("K", t3.scale)

    def test05(self):
        t1 = s.Temperature(64.1594, "F")
        t2 = s.Temperature(-422.8018, "F")
        t3 = t1.substract(t2)
        self.assertAlmostEqual(486.9612, t3.value)
        self.assertEqual("F", t3.value)

    def test06(self):
        t1 = s.Temperature()
        t2 = s.Temperature
        t3 = t1.substract(t2)
        self.assertAlmostEqual()
        self.assertEqual()

    def test07(self):
        t1 = s.Temperature()
        t2 = s.Temperature
        t3 = t1.multiply(t2)
        self.assertAlmostEqual()
        self.assertEqual()

    def test08(self):
        t1 = s.Temperature()
        t2 = s.Temperature
        t3 = t1.multiply(t2)
        self.assertAlmostEqual()
        self.assertEqual()

    def test09(self):
        t1 = s.Temperature()
        t2 = s.Temperature
        t3 = t1.divide(t2)
        self.assertAlmostEqual()
        self.assertEqual()

    def test10(self):
        t1 = s.Temperature()
        t2 = s.Temperature
        t3 = t1.divide(t2)
        self.assertAlmostEqual()
        self.assertEqual()


def run():
    suite = u.TestLoader().loadTestsFromTestCase(MyTests)
    u.TextTestRunner(verbosity=3).run(suite)