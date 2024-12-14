from textnode import *
from htmlnode import *

def main():
    item = TextNode("This is a text node", TextType.BOLD_TEXT.value, "https://www.boot.dev")    
    item2 = HTMLNode("a", "This is a link", None, {"href": "https://www.google.com", "target": "_blank",})
    print(item)
    print(item2)

main()