import unittest

from htmlnode import HTMLNode

run_cases = [{"href": "https://www.google.com", "target": "_blank",}, {"HREF": "HTTPS://WWW.GOOGLE.COM", "TARGET": "_BLANK",}, {"":"", " ":"",}, {"": " ", " ": " "}]

class TestHTMLNode(unittest.TestCase):
    """First creates an HTMLNode to test. It then runs prop_to_html method.
    this method should convert a dictionary into a single line string with it's key value pairs.
    if successful returns True and if not False. If unable to run it raises an error to be read"""
    def test_prop_to_html(self):
        try:
            for run in run_cases:
                html = HTMLNode(props=run)
                case_string = ""
                for key in run:
                    case_string += f' {key}="{run[key]}"'
                if html.prop_to_html() == case_string:
                    print(html.prop_to_html())
                    return True 
                else:
                    print(html.prop_to_html())
                    return False
        except Exception as e:
            print(e)


if __name__ == "__main__":
    unittest.main()