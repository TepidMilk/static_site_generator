import unittest

from textnode import *
from htmlnode import *
from main import text_node_to_html_node

class testTexttoHTML(unittest.TestCase):
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