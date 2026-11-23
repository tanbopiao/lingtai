"""灵台（LINGTAI）算子单测：名帖完整、行为达标、只增不覆盖。"""
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

    def test_store_recall(self):
        rid = self.op.store({"topic": "昆仑", "note": "世界模型"})
        self.assertTrue(rid.startswith("LT-"))
        hits = self.op.recall("昆仑")
        self.assertEqual(len(hits), 1)
        self.assertEqual(self.op.recall("无有"), [])


if __name__ == "__main__":
    unittest.main()
