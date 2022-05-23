import unittest as u
import main as m


class MyTestCase(u.TestCase):
    def test01(self):  # Celcius To Fahrenheit Multiplication
        t1 = m.Temperature(19.76, "F")
        t2 = m.Temperature(86.74, "C")
        t3 = t1.multiply(t2)
        self.assertAlmostEqual(3717.48832, t3.value, 4)
        self.assertEqual("F", t3.scale)

    def test02(self):  # Fahrenheit to Celcius Division
        t1 = m.Temperature(54.7299, "C")
        t2 = m.Temperature(88.1415, "F")
        t3 = t1.divide(t2)
        self.assertAlmostEqual(1.7547, t3.value, 4)
        self.assertEqual("C", t3.scale)

    def test03(self):  # Fahrenheit to Kelvin Addition
        t1 = m.Temperature(98.2014, "K")
        t2 = m.Temperature(110.4158, "F")
        t3 = t1.add(t2)
        self.assertAlmostEqual(414.91573333, t3.value, 4)
        self.assertEqual("K", t3.scale)

    def test04(self):  # Kelvin to Fahrenheit Substraction
        t1 = m.Temperature(-13.1042, "F")
        t2 = m.Temperature(34.7924, "K")
        t3 = t1.substract(t2)
        self.assertAlmostEqual(383.93948, t3.value, 4)
        self.assertEqual("F", t3.scale)

    def test05(self):  # Kelvin to Celcius Multiplication
        t1 = m.Temperature(-91.0450, "C")
        t2 = m.Temperature(26.2170, "K")
        t3 = t1.multiply(t2)
        self.assertAlmostEqual(22482.014985, t3.value, 4)
        self.assertEqual("C", t3.scale)

    def test06(self):  # Celcius to Kelvin Addition
        t1 = m.Temperature(-148.2101, "K")
        t2 = m.Temperature(81.6525, "C")
        t3 = t1.add(t2)
        self.assertAlmostEqual(206.5924, t3.value, 4)
        self.assertEqual("K", t3.scale)

    def test07(self):  # Conversion Kelvin to Fahrenheit
        t1 = m.Temperature(66.2479, "F")
        t2 = m.Temperature(263.7106, "K")
        t3 = t1.conversion(t2)
        self.assertAlmostEqual(15.00908, t3.value)

    def test08(self):  # Non-zero result
        t1 = m.Temperature(29.5229, "C")
        t2 = m.Temperature(85.14122, "F")
        self.assertRaises(BaseException, t1.substract(t2))
        # This will throw the expected error, so it does what it's intended

    def test09(self):  # Same scale Addition
        t1 = m.Temperature(27.1485, "C")
        t2 = m.Temperature(-12.3833, "C")
        t3 = t1.add(t2)
        self.assertAlmostEqual(14.7652, t3.value)
        self.assertEqual("C", t3.scale)


def run():
    suite = u.TestLoader().loadTestsFromTestCase(MyTestCase)
    u.TextTestRunner(verbosity=3).run(suite)


run()