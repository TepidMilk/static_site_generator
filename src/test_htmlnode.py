import unittest

from htmlnode import HTMLNode

run_cases = [{"href": "https://www.google.com", "target": "_blank",}, {"HREF": "HTTPS://WWW.GOOGLE.COM", "TARGET": "_BLANK",}, {" ":"", " ":"",}, {"": " ", " ": " "}]

class TestHTMLNode(unittest.TestCase):
    """creates an HTMLNode and checks """
    def test_prop_to_html(self):
        try:
            for run in run_cases:
                html = HTMLNode(props=run)
                case_string = ""
                for key in run:
                    case_string += f' {key}="{run[key]}"'
                self.assertEqual(html.prop_to_html(), case_string)
                
        except Exception as e:
            print(e)


if __name__ == "__main__":
    unittest.main()