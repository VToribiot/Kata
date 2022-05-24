import unittest as u
import session3 as s


class MyTestCase(u.TestCase):
    def test01(self):
        t1 = s.Temperature()
        t2 = s.Temperature()
        t3 = t1.add(t2)
        self.assertAlmostEqual( , t3.value)
        self.assertEqual(t1.scale, t3.scale)

    def test02(self):
        t1 = s.Temperature()
        t2 = s.Temperature()
        t3 = t1.add(t2)
        self.assertAlmostEqual( , t3.value)
        self.assertEqual(t1.scale, t3.scale)

    def test03(self):
        t1 = s.Temperature()
        t2 = s.Temperature()
        t3 = t1.add(t2)
        self.assertAlmostEqual( , t3.value)
        self.assertEqual(t1.scale, t3.scale)

    def test04(self):
        t1 = s.Temperature()
        t2 = s.Temperature()
        t3 = t1.add(t2)
        self.assertAlmostEqual( , t3.value)
        self.assertEqual(t1.scale, t3.scale)

    def test05(self):
        t1 = s.Temperature()
        t2 = s.Temperature()
        t3 = t1.add(t2)
        self.assertAlmostEqual( , t3.value)
        self.assertEqual(t1.scale, t3.scale)

    def test06(self):
        t1 = s.Temperature()
        t2 = s.Temperature()
        t3 = t1.add(t2)
        self.assertAlmostEqual( , t3.value)
        self.assertEqual(t1.scale, t3.scale)

    def test07(self):
        t1 = s.Temperature()
        t2 = s.Temperature()
        t3 = t1.add(t2)
        self.assertAlmostEqual( , t3.value)
        self.assertEqual(t1.scale, t3.scale)

    def test08(self):
        t1 = s.Temperature()
        t2 = s.Temperature()
        t3 = t1.add(t2)
        self.assertAlmostEqual( , t3.value)
        self.assertEqual(t1.scale, t3.scale)

    def test09(self):
        t1 = s.Temperature()
        t2 = s.Temperature()
        t3 = t1.add(t2)
        self.assertAlmostEqual( , t3.value)
        self.assertEqual(t1.scale, t3.scale)

    def test10(self):
        t1 = s.Temperature()
        t2 = s.Temperature()
        t3 = t1.add(t2)
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