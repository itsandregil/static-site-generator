import unittest
from src.html_node import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_node_without_props(self):
        node = HTMLNode("p", "hello world")
        self.assertEqual(node.props_to_html(), "")

    def test_node_with_one_prop(self):
        node = HTMLNode("a", "watch video", props={"href": "https://www.youtube.com"})
        self.assertEqual(node.props_to_html(), ' href="https://www.youtube.com"')

    def test_node_with_many_props(self):
        node = HTMLNode(
            "a",
            "watch video",
            props={"href": "https://www.youtube.com", "target": "_blank"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' href="https://www.youtube.com" target="_blank"',
        )
