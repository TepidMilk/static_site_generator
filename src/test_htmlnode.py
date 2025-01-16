import unittest

from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    #creates an HTMLNode and some tests. Checks if string created by prop_to_html equals another case strings
    def test_prop_to_html(self):
        actual_prop_to_html = [{"href": "https://www.google.com", "target": "_blank",}, {"HREF": "HTTPS://WWW.GOOGLE.COM", "TARGET": "_BLANK",}, {" ":" ", " ":" ",}]
        expected_prop_to_html = [' href="https://www.google.com" target="_blank"', ' HREF="HTTPS://WWW.GOOGLE.COM" TARGET="_BLANK"', '  =" "']
        try:
            for i in range(len(actual_prop_to_html)):
                html = HTMLNode(props=actual_prop_to_html[i])
                self.assertEqual(html.prop_to_html(), expected_prop_to_html[i])
                
        except Exception as e:
            print(e)
    

    def test_leaf_Node(self):
        actual_leaf = [LeafNode("p", "This is a paragraph of text."), LeafNode("a", "Click me!", {"href": "https://www.google.com"})]
        expected_leaf = ['<p>This is a paragraph of text.</p>', '<a href="https://www.google.com">Click me!</a>']
        try:
            for i in range(len(actual_leaf)):
                leaf = actual_leaf[i]
                self.assertEqual(leaf.to_html(), expected_leaf[i])
        except Exception as e:
            print(e)

    def test_parent_node(self):
        actual_parent = [
            ParentNode("p",[
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text")
                ]),
            ParentNode(None, None),
            ParentNode("p", [
                ParentNode("p",[
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text")
                    ]), 
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text")]
            )]
        expected_parent = [
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>", 
            "No Tag", 
            "<p><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
            ]
        try:
            for i in range(len(actual_parent)):
                parent = actual_parent[i]
                self.assertEqual(parent.to_html(), expected_parent[i])
        except Exception as e:
            print(e)

if __name__ == "__main__":
    unittest.main()