import unittest

from inline_markdown import *
from textnode import TextNode, TextType

class TestInlineMarkdown(unittest.TestCase):
    def test_bold_text(self):
        node = TextNode("This text is **Bold**", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            new_nodes,
            [
                TextNode("This text is ", TextType.NORMAL), 
                TextNode("Bold", TextType.BOLD)
            ])
    
    def test_italic(self):
        node = TextNode("This text is *Italic*", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertListEqual(
            new_nodes,
            [
                TextNode("This text is ", TextType.NORMAL),
                TextNode("Italic", TextType.ITALIC)
            ])
        
    def test_code(self):
        node = TextNode("This text is `code`", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            new_nodes,
            [
                TextNode("This text is ", TextType.NORMAL),
                TextNode("code", TextType.CODE)
            ])

    def test_multiword(self):
        node = TextNode("**This** text is **Bold**", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            new_nodes,
            [
                TextNode("This", TextType.BOLD),
                TextNode(" text is ", TextType.NORMAL),
                TextNode("Bold", TextType.BOLD)
            ])
        
    def test_multi_delimiter(self):
        node = TextNode("*This* text is **Bold** and `code`", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)
        new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)
        self.assertListEqual(
            new_nodes,
            [
                TextNode("This", TextType.ITALIC),
                TextNode(" text is ", TextType.NORMAL),
                TextNode("Bold", TextType.BOLD),
                TextNode(" and ", TextType.NORMAL),
                TextNode("code", TextType.CODE)
            ])
        
    def test_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        test = extract_markdown_images(text)
        self.assertEqual(test, [
            ("rick roll","https://i.imgur.com/aKaOqIh.gif"),
            ("obi wan","https://i.imgur.com/fJRm4Vk.jpeg")
        ])

    def test_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        test = extract_markdown_links(text)
        self.assertEqual(test, [
            ("to boot dev", "https://www.boot.dev"),
            ("to youtube", "https://www.youtube.com/@bootdotdev")
        ])
        
if __name__ == "__main__":
    unittest.main()