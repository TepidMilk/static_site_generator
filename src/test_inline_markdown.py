import unittest

from inline_markdown import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_bold_text(self):
        node = TextNode("This text is **Bold**", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This text is ", TextType.NORMAL), 
                TextType("Bold", TextType.BOLD)
            ])
    def test_multiword(self):
        node = TextNode("**This** text is **Bold**", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This", TextType.BOLD),
                TextNode(" text is ", TextType.NORMAL),
                TextNode("Bold", TextType.BOLD)
            ]
        )