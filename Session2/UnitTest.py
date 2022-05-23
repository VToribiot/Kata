import unittest as u
import session2 as s


class MyTests(u.TestCase):
    def test01(self):  # Conversion Test
        t1 = s.Temperature(249.4426, "Cº")
        t2 = s.Temperature(8.1888, "Fº")
        t3 = t1.conversion(t2)
        self.assertAlmostEqual(-13.2284444, t3.value, 4)
        self.assertEqual("Cº", t3.scale)

    def test02(self):  # Conversion Test
        t1 = s.Temperature(241.0029, "Cº")
        t2 = s.Temperature(-270.1657, "Kº")
        t3 = t1.conversion(t2)
        self.assertAlmostEqual(-543.3157, t3.value, 4)
        self.assertEqual("Cº", t3.scale)

    def test03(self):  # Addition Test
        t1 = s.Temperature(-173.7856, "Fº")
        t2 = s.Temperature(317.6799, "Kº")
        t3 = t1.add(t2)
        self.assertAlmostEqual(-61.63178, t3.value, 4)
        self.assertEqual("Fº", t3.scale)

    def test04(self):  # Addition Test
        t1 = s.Temperature(-43.0363, "Kº")
        t2 = s.Temperature(365.3039, "Fº")
        t3 = t1.add(t2)
        self.assertAlmostEqual(415.28253333, t3.value, 4)
        self.assertEqual("Kº", t3.scale)

    def test05(self):  # Substraction Test
        t1 = s.Temperature(64.1594, "Fº")
        t2 = s.Temperature(-422.8018, "Fº")
        t3 = t1.substract(t2)
        self.assertAlmostEqual(486.9612, t3.value, 4)
        self.assertEqual("Fº", t3.scale)

    def test06(self):  # Subtraction Test
        t1 = s.Temperature(219.5862, "Kº")
        t2 = s.Temperature(-409.4712, "Cº")
        t3 = t1.substract(t2)
        self.assertAlmostEqual(355.9074, t3.value, 4)
        self.assertEqual("Kº", t3.scale)

    def test07(self):  # Multiplication Test
        t1 = s.Temperature(294.3932, "Fº")
        t2 = s.Temperature(19.1793, "Cº")
        t3 = t1.multiply(t2)
        self.assertAlmostEqual(19583.8423, t3.value, 4)
        self.assertEqual("Fº", t3.scale)

    def test08(self):  # Multiplication Test
        t1 = s.Temperature(75.8430, "Cº")
        t2 = s.Temperature(190.5469, "Kº")
        t3 = t1.multiply(t2)
        self.assertAlmostEqual(-6264.8669, t3.value, 4)
        self.assertEqual("Cº", t3.scale)

    def test09(self):  # Division Test
        t1 = s.Temperature(-11.5765, "Cº")
        t2 = s.Temperature(-32.7466, "Cº")
        t3 = t1.divide(t2)
        self.assertAlmostEqual(0.3535, t3.value, 4)
        self.assertEqual("Cº", t3.scale)

    def test10(self):  # Division Test
        t1 = s.Temperature(234.6318, "Fº")
        t2 = s.Temperature(222.5054, "Kº")
        t3 = t1.divide(t2)
        self.assertAlmostEqual(-3.9660, t3.value, 4)
        self.assertEqual("Fº", t3.scale)

    def test11(self):  # Zero result Test
        t1 = s.Temperature(-257.4078, "Cº")
        t2 = s.Temperature(257.4078, "Cº")
        self.assertRaises(ValueError, t1.add, t2)

    def test12(self):  # Zero Division Test
        t1 = s.Temperature(71.5363, "Fº")
        t2 = s.Temperature(-17.7778, "Cº")
        self.assertRaises(BaseException, t1.divide(t2))


def run():
    suite = u.TestLoader().loadTestsFromTestCase(MyTests)
    u.TextTestRunner(verbosity=3).run(suite)

run()