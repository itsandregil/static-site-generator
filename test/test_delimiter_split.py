import unittest
from src.utils import split_node_delimiter
from src.text_node import TextNode, TextType


class TestSplitOnDelimeter(unittest.TestCase):
    def test_split_node(self):
        node = TextNode("Hello **world** friend", TextType.TEXT)
        new_nodes = split_node_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            new_nodes,
            [
                TextNode("Hello ", TextType.TEXT),
                TextNode("world", TextType.BOLD),
                TextNode(" friend", TextType.TEXT),
            ],
        )
