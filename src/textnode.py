from enum import Enum

#Enum handler for different inline text
class TextType(Enum):
    NORMAL_TEXT = "normal"
    BOLD_TEXT = "bold"
    ITALIC_TEXT = "italic"
    CODE_TEXT = "code"
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
    