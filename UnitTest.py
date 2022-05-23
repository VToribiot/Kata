import unittest as u
import main as m


class MyTestCase(u.TestCase):
    def test01(self):
        t1 = m.Temperature(19.76, "F")
        t2 = m.Temperature(86.74, "C")
        t3 = t1.multiply(t2)
        self.assertAlmostEqual(3717.48832, t3.value)
        self.assertEqual("F", t3.scale)

    def test02(self):
        t1 = m.Temperature(54.7299, "C")
        t2 = m.Temperature(88.1415, "F")
        t3 = t1.divide(t2)
        self.assertAlmostEqual(1.7547, t3.value)
        self.assertEqual("C", t3.scale)

    def test03(self):
        t1 = m.Temperature(98.2014, "K")
        t2 = m.Temperature(110.4158, "F")
        t3 = t1.add(t2)
        self.assertAlmostEqual(414.91573333, t3.value)
        self.assertEqual("K", t3.scale)

    def test04(self):
        t1 = m.Temperature(-13.1042, "F")
        t2 = m.Temperature(34.7924, "K")
        t3 = t1.substract(t2)
        self.assertAlmostEqual(-47.8966, t3.value)
        self.assertEqual("F", t3.scale)

    def test05(self):
        t1 = m.Temperature(-91.0450, "C")
        t2 = m.Temperature(26.2170, "K")
        t3 = t1.multiply(t2)
        self.assertAlmostEqual(22436.492485, t3.value)
        self.assertEqual("C", t3.scale)

    def test06(self):
        t1 = m.Temperature(-148.2101, "K")
        t2 = m.Temperature(81.6525, "C")
        t3 = t1.add(t2)
        self.assertAlmostEqual(206.5924, t3.value)
        self.assertEqual("K", t3.scale)

def run():
    suite = u.TestLoader().loadTestsFromTestCase(MyTestCase)
    u.TextTestRunner(verbosity=3).run(suite)


run()