import unittest as u
import main as m


class MyTestCase(u.TestCase):
    def test01(self):
        t1 = m.Temperature(19.76, "F")
        t2 = m.Temperature(86.74, "C")
        t3 = t1.multiply(t2)
        self.assertAlmostEqual(3717.48832, t3.value)
        self.assertEqual("F", t3.scale)


def run():
    suite = u.TestLoader().loadTestsFromTestCase(MyTestCase)
    u.TextTestRunner(verbosity=3).run(suite)


run()