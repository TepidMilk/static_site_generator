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
        self.assertListEqual(test, 
        [
            ("rick roll","https://i.imgur.com/aKaOqIh.gif"),
            ("obi wan","https://i.imgur.com/fJRm4Vk.jpeg")
        ])

    def test_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        test = extract_markdown_links(text)
        self.assertListEqual(test, 
        [
            ("to boot dev", "https://www.boot.dev"),
            ("to youtube", "https://www.youtube.com/@bootdotdev")
        ])

    def test_split_node_images(self):
        node = TextNode(
            "This is text with a image ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.NORMAL,
        )
        test = split_nodes_images([node])
        self.assertListEqual(test,
        [
            TextNode("This is text with a image ", TextType.NORMAL),
            TextNode("to boot dev", TextType.IMAGES, "https://www.boot.dev"),
            TextNode(" and ", TextType.NORMAL),
            TextNode("to youtube", TextType.IMAGES, "https://www.youtube.com/@bootdotdev"),
        ])

    def test_split_node_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.NORMAL,
        )
        test = split_nodes_links([node])
        self.assertListEqual(test,
        [
            TextNode("This is text with a link ", TextType.NORMAL),
            TextNode("to boot dev", TextType.LINKS, "https://www.boot.dev"),
            TextNode(" and ", TextType.NORMAL),
            TextNode("to youtube", TextType.LINKS, "https://www.youtube.com/@bootdotdev"),
        ])

    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        test = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.NORMAL),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.NORMAL),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.NORMAL),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.NORMAL),
                TextNode("obi wan image", TextType.IMAGES, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.NORMAL),
                TextNode("link", TextType.LINKS, "https://boot.dev"),
            ],
            test
        )


if __name__ == "__main__":
    unittest.main()