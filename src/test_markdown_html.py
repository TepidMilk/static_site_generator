import unittest

from markdown_html import *

class TestMarkdownHtml(unittest.TestCase):
    def test_text_to_children(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        test = text_to_children(text)
        
        self.assertListEqual(
            [
                LeafNode(None, "This is "),
                LeafNode("b", "text"),
                LeafNode(None, " with an "),
                LeafNode("i", "italic"),
                LeafNode(None, " word and a "),
                LeafNode("code", "code block"),
                LeafNode(None, " and an "),
                LeafNode("img", "", {"src": "https://i.imgur.com/fJRm4Vk.jpeg", "alt": "obi wan image"}),
                LeafNode(None, " and a "),
                LeafNode("a", "link", {"href": "https://boot.dev"})
            ],
            test
        )

    def test_text_to_children_block(self):
        text = "> This is **text** with an *italic*\n > word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        test = text_to_children(text)
        self.assertListEqual(
            [
                LeafNode(None, "> This is "),
                LeafNode("b", "text"),
                LeafNode(None, " with an "),
                LeafNode("i", "italic"),
                LeafNode(None, " > word and a "),
                LeafNode("code", "code block"),
                LeafNode(None, " and an "),
                LeafNode("img", "", {"src": "https://i.imgur.com/fJRm4Vk.jpeg", "alt": "obi wan image"}),
                LeafNode(None, " and a "),
                LeafNode("a", "link", {"href": "https://boot.dev"})
            ],
            test
        )

if __name__ == "__main__":
    unittest.main()