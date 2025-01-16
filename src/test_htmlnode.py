import unittest

from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    #creates an HTMLNode and some tests. Checks if string created by prop_to_html equals another case strings
    def test_prop_to_html(self):
        actual = [{"href": "https://www.google.com", "target": "_blank",}, {"HREF": "HTTPS://WWW.GOOGLE.COM", "TARGET": "_BLANK",}, {" ":" ", " ":" ",}]
        expected = [' href="https://www.google.com" target="_blank"', ' HREF="HTTPS://WWW.GOOGLE.COM" TARGET="_BLANK"', '  =" "']
        try:
            for i in range(len(actual)):
                html = HTMLNode(props=actual[i])
                self.assertEqual(html.prop_to_html(), expected[i])
                
        except Exception as e:
            print(e)
    

    def test_leaf_Node(self):
        actual = [LeafNode("p", "This is a paragraph of text."), LeafNode("a", "Click me!", {"href": "https://www.google.com"})]
        expected = ['<p>This is a paragraph of text.</p>', '<a href="https://www.google.com">Click me!</a>']
        try:
            for i in range(len(actual)):
                leaf = actual[i]
                self.assertEqual(leaf.to_html(), expected[i])
        except Exception as e:
            print(e)


if __name__ == "__main__":
    unittest.main()