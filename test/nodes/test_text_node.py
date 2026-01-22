import unittest
from src.nodes.text_node import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_nodes_are_equal(self):
        node = TextNode("This is a text node", TextType.BOLD)
        other = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, other)

    def test_node_texts_are_not_equal(self):
        node = TextNode("This is a text node", TextType.TEXT)
        other = TextNode("This is another text node", TextType.TEXT)
        self.assertNotEqual(node, other)

    def test_node_types_are_not_equal(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        other = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, other)

    def test_node_links_are_not_equal(self):
        node = TextNode("This is a text node", TextType.LINK, "https://www.youtube.com")
        other = TextNode("This is a text node", TextType.LINK, "https://www.twitch.com")
        self.assertNotEqual(node, other)


if __name__ == "__main__":
    unittest.main()
