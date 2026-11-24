import unittest

from atlas import load_topics, search


class AtlasTests(unittest.TestCase):
    def test_hdfs_search(self):
        self.assertIn("hdfs", search("HDFS"))

    def test_hdfs_search_in_chinese(self):
        self.assertIn("hdfs", search("分布式文件系统"))

    def test_mapreduce_search(self):
        self.assertIn("mapreduce", search("MapReduce"))
        self.assertIn("mapreduce", search("映射归约"))

    def test_links_resolve(self):
        topics = load_topics()
        ids = {topic["id"] for topic in topics}
        self.assertEqual(len(ids), len(topics), "存在重复的主题 ID")
        for topic in topics:
            for target in topic["links"]:
                self.assertIn(target, ids, f"{topic['id']} → {target}")
