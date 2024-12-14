import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    """First creates an HTMLNode to test. It then runs prop_to_html method.
    this method should convert a dictionary into a single line string with it's key value pairs.
    if successful returns True and if not False. If unable to run it raises an error to be read"""
    def test_prop_to_html(self):
        try:
            html = HTMLNode(props={"href": "https://www.google.com", "target": "_blank",})
            if html.prop_to_html() == ' href="https://www.google.com" target="_blank"':
                return True 
            else:
                return False
        except Exception as e:
            print(e)


if __name__ == "__main__":
    unittest.main()