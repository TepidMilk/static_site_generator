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
        self.assertEqual(html_node, expected)
        
    
    def test_textnode_to_htmlnode_bold(self):
        text_node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(text_node)
        expected = LeafNode("b", "This is bold")
        self.assertEqual(html_node, expected)
        

    def test_textnode_to_htmlnode_italic(self):
        text_node = TextNode("This is Italic", TextType.ITALIC)
        html_node = text_node_to_html_node(text_node)
        expected = LeafNode("i", "This is Italic")
        self.assertEqual(html_node, expected)
        

    def test_textnode_to_htmlnode_code(self):
        text_node = TextNode("This is code", TextType.CODE)
        html_node = text_node_to_html_node(text_node)
        expected = LeafNode("code", "This is code")
        self.assertEqual(html_node, expected)
        
    
    def test_textnode_to_htmlnode_links(self):
        text_node = TextNode("This is a link", TextType.LINKS, "https://www.google.com")
        html_node = text_node_to_html_node(text_node)
        expected = LeafNode("a", "This is a link", {"href": "https://www.google.com"})
        self.assertEqual(html_node, expected)

    def test_textnode_to_htmlnode_images(self):
        text_node = TextNode("This is an image", TextType.IMAGES, "https://www.google.com")
        html_node = text_node_to_html_node(text_node)
        expected = LeafNode("img", "", {"src": "https://www.google.com", "alt": "This is an image"})
        self.assertEqual(html_node, expected)
    
        


if __name__ == "__main__":
    unittest.main()