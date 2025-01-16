from textnode import *
from htmlnode import *
from enum import Enum

def main():
    item = TextNode("This is a text node", TextType.BOLD.value, "https://www.boot.dev")    
    item2 = HTMLNode("a", "This is a link", None, {"href": "https://www.google.com", "target": "_blank",})

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.NORMAL:
            return LeafNode()
        case TextType.BOLD:
            return LeafNode(text_node.text, "b")
        case TextType.ITALIC:
            return LeafNode(text_node.text, "i")
        case TextType.CODE:
            return LeafNode(text_node.text, "code")
        case TextType.LINKS:
            return LeafNode(text_node.text, "a", {"href": text_node.url})
        case TextType.IMAGES:
            return LeafNode("", "img", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception("Invalid Text Type")
        
main()