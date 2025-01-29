from textnode import *
from htmlnode import *
from enum import Enum

def main():
    item = TextNode("This is a text node", TextType.BOLD.value, "https://www.boot.dev")    
    item2 = HTMLNode("a", "This is a link", None, {"href": "https://www.google.com", "target": "_blank",})

main()