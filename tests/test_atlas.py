import unittest

from atlas import load_topics, search


class AtlasTests(unittest.TestCase):
    def test_hdfs_search(self):
        self.assertIn("hdfs", search("HDFS"))

    def test_links_resolve(self):
        topics = load_topics()
        ids = {topic["id"] for topic in topics}
        self.assertEqual(len(ids), len(topics), "存在重复的主题 ID")
        for topic in topics:
            for target in topic["links"]:
                self.assertIn(target, ids, f"{topic['id']} → {target}")
