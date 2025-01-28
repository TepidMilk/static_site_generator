import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_type(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        node2 = TextNode("This is a text node", TextType.NORMAL)
        self.assertEqual(node, node2)

    def test_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.google.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.google.com")
        self.assertEqual(node, node2)

    def test_textnode_to_htmlnode(self):
        text_node = TextNode("Hello, world!", TextType.NORMAL)
        html_node = text_node_to_html_node(text_node)
        expected = LeafNode(None, "Hello, world!")
        try:
            self.assertEqual(html_node, expected)
        except Exception as e:
            print(e)
        


if __name__ == "__main__":
    unittest.main()