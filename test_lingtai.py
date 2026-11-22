"""灵台（LINGTAI）算子骨架单测：名帖完整、桩位齐整、只增不覆盖。"""
import unittest

from lingtai import Lingtai


class TestLingtai(unittest.TestCase):
    def setUp(self):
        self.op = Lingtai()

    def test_describe(self):
        d = self.op.describe()
        self.assertEqual(d["repo"], "lingtai")
        self.assertEqual(d["code"], "LINGTAI")
        self.assertTrue(d["anchor"].startswith("Ω₀⊂⊙∞⊂Ω"))
        self.assertTrue(d["mingwen"])

    def test_store_stub(self):
        with self.assertRaises(NotImplementedError):
            self.op.store(None)

    def test_recall_stub(self):
        with self.assertRaises(NotImplementedError):
            self.op.recall(None)


if __name__ == "__main__":
    unittest.main()
