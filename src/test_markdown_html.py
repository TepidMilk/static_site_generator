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
    
    def test_markdown_to_html_node(self):
        text = "This block is a paragraph"
        test = markdown_to_html_node(text)
        self.assertEqual(test, ParentNode("div", [ParentNode("p", [LeafNode(None, "This block is a paragraph")])]))
    
    def test_markdown_to_html_node_heading(self):
        text = "### This is a heading"
        test = markdown_to_html_node(text)
        self.assertEqual(test, ParentNode("div", [ParentNode("h3", [LeafNode(None, "This is a heading")])]))

    def test_markdown_to_html_node_quote(self):
        text = "> This is a quote"
        test = markdown_to_html_node(text)
        self.assertEqual(test, ParentNode("div", [ParentNode("blockquote", [LeafNode(None, "This is a quote")])]))

    def test_markdown_to_html_node_quote_bold(self):
        text = """> This is a **quote**"""
        test = markdown_to_html_node(text)
        self.assertEqual(test.tag, "div")
        self.assertEqual(test.children[0].tag, "blockquote")
        self.assertEqual(test.children[0].children, [LeafNode(None, "This is a "), LeafNode("b", "quote")])

    def test_markdown_to_html_node_code(self):
        text = "```This is some code```"
        test = markdown_to_html_node(text)
        self.assertEqual(test, ParentNode("div", [ParentNode("code", [LeafNode(None, "This is some code")])]))

    def test_markdown_to_html_node_code(self):
        text = "```This is some code\nit has two lines and **bold text**```"
        test = markdown_to_html_node(text)
        self.assertEqual(test.tag, "div")
        self.assertEqual(test.children[0].tag, "pre")
        self.assertEqual(test.children[0].children[0].tag, "code")
        self.assertEqual(test.children[0].children[0].children, [LeafNode(None, "This is some code\nit has two lines and "), LeafNode("b", "bold text")])

    def test_markdown_to_html_node_ul(self):
        text = "- This is a list item"
        test = markdown_to_html_node(text)
        self.assertEqual(test, ParentNode("div", [ParentNode("ul", [ParentNode("li", [LeafNode(None, "This is a list item")])])]))

    def test_markdown_to_html_node_ul_multi(self):
        text = """
- list item 1
- list item 2
"""
        test = markdown_to_html_node(text)
        self.assertEqual(test.tag, "div")
        self.assertEqual(test.children[0].tag, "ul")
        self.assertEqual(test.children[0].children[0].tag, "li")
        self.assertEqual(test.children[0].children[1].tag, "li")
        self.assertEqual(test.children[0].children[0].children, [LeafNode(None, "list item 1")])
        self.assertEqual(test.children[0].children[1].children, [LeafNode(None, "list item 2")])
        
    def test_markdown_to_html_node_ol(self):
        text = "1. This is a list item"
        test = markdown_to_html_node(text)
        self.assertEqual(test, ParentNode("div", [ParentNode("ol", [ParentNode("li", [LeafNode(None, "This is a list item")])])]))

    def test_markdown_to_html_node_ol_multi(self):
        text = """
1. list item 1
2. list item 2
"""
        test = markdown_to_html_node(text)
        self.assertEqual(test.tag, "div")
        self.assertEqual(test.children[0].tag, "ol")
        self.assertEqual(test.children[0].children[0].tag, "li")
        self.assertEqual(test.children[0].children[1].tag, "li")
        self.assertEqual(test.children[0].children[0].children, [LeafNode(None, "list item 1")])
        self.assertEqual(test.children[0].children[1].children, [LeafNode(None, "list item 2")])

    


if __name__ == "__main__":
    unittest.main()