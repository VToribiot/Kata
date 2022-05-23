import unittest as u
import session2 as s


class MyTests(u.TestCase):
    def test01(self):
        t1 = s.Temperature()
        t2 = s.Temperature
        t3 = t1.add(t2)
        self.assertAlmostEqual()
        self.assertEqual()

    def test02(self):
        t1 = s.Temperature()
        t2 = s.Temperature
        t3 = t1.add(t2)
        self.assertAlmostEqual()
        self.assertEqual()

    def test03(self):
        t1 = s.Temperature()
        t2 = s.Temperature
        t3 = t1.add(t2)
        self.assertAlmostEqual()
        self.assertEqual()

    def test04(self):
        t1 = s.Temperature()
        t2 = s.Temperature
        t3 = t1.add(t2)
        self.assertAlmostEqual()
        self.assertEqual()

    def test05(self):
        t1 = s.Temperature()
        t2 = s.Temperature
        t3 = t1.add(t2)
        self.assertAlmostEqual()
        self.assertEqual()

    def test06(self):
        t1 = s.Temperature()
        t2 = s.Temperature
        t3 = t1.add(t2)
        self.assertAlmostEqual()
        self.assertEqual()

    def test07(self):
        t1 = s.Temperature()
        t2 = s.Temperature
        t3 = t1.add(t2)
        self.assertAlmostEqual()
        self.assertEqual()

    def test08(self):
        t1 = s.Temperature()
        t2 = s.Temperature
        t3 = t1.add(t2)
        self.assertAlmostEqual()
        self.assertEqual()

    def test09(self):
        t1 = s.Temperature()
        t2 = s.Temperature
        t3 = t1.add(t2)
        self.assertAlmostEqual()
        self.assertEqual()

    def test10(self):
        t1 = s.Temperature()
        t2 = s.Temperature
        t3 = t1.add(t2)
        self.assertAlmostEqual()
        self.assertEqual()


def run():
    suite = u.TestLoader().loadTestsFromTestCase(MyTests)
    u.TextTestRunner(verbosity=3).run(suite)