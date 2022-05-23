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
        t1 = s.Temperature(219.5862, "K")
        t2 = s.Temperature(-409.4712, "C")
        t3 = t1.substract(t2)
        self.assertAlmostEqual(355.9074, t3.value)
        self.assertEqual("K", t3.scale)

    def test07(self):
        t1 = s.Temperature(294.3932, "F")
        t2 = s.Temperature(19.1793, "C")
        t3 = t1.multiply(t2)
        self.assertAlmostEqual(19,583.8423, t3.value)
        self.assertEqual("F", t3.scale)

    def test08(self):
        t1 = s.Temperature(75.8430, "C")
        t2 = s.Temperature(190.5469, "K")
        t3 = t1.multiply(t2)
        self.assertAlmostEqual(-6,264.8669, t3.value)
        self.assertEqual("C", t3.scale)

    def test09(self):
        t1 = s.Temperature(-11.5765, "C")
        t2 = s.Temperature(-32.7466, "C")
        t3 = t1.divide(t2)
        self.assertAlmostEqual(0.3535, t3.value)
        self.assertEqual("C", t3.scale)

    def test10(self):
        t1 = s.Temperature(79.8964, "F")
        t2 = s.Temperature(61.5072, "K")
        t3 = t1.divide(t2)
        self.assertAlmostEqual(-0.2289, t3.value)
        self.assertEqual("F", t3.scale)

    def test11(self):
        t1 = s.Temperature(-257.4078, "C")
        t2 = s.Temperature(257.4078, "C")
        self.assertRaises(BaseException, t1.add(t2))

    def test12(self):
        t1 = s.Temperature(71.5363, "F")
        t2 = s.Temperature(-17.7778, "C")
        self.assertRaises(BaseException, t1.divide(t2))


def run():
    suite = u.TestLoader().loadTestsFromTestCase(MyTests)
    u.TextTestRunner(verbosity=3).run(suite)