from enum import Enum
from htmlnode import LeafNode

#Enum handler for different inline text
class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINKS = "link"
    IMAGES = "image"

class TextNode():

    """construct TextNode with 
    text: string inline text content
    text_type: TextType  enum
    url: string url"""
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    #Checks 2 nodes for equivalence and returns true if no differences
    def __eq__(self, node2):
        if self.text != node2.text:
            raise Exception(f"{self.text} does not equal {node2.text}")
        elif self.text_type != node2.text_type:
            raise Exception(f"{self.text_type} does not equal {node2.text_type}")
        elif self.url != node2.url:
            raise Exception(f"{self.url} does not equal {node2.url}")
        return True
        
      
    #String representation of TextNode
    def __repr__(self):
        return (f"TextNode({self.text}, {self.text_type}, {self.url})")
    
def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.NORMAL:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINKS:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGES:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception("Invalid Text Type")