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

    #Returns true if all properties equal another TextNodes
    def __eq__(self, node2):
        if (self.text, self.text_type, self.url) == (node2.text, node2.text_type, node2.url):
            return True
        
    #String representation of TextNode
    def __repr__(self):
        return (f"TextNode({self.text}, {self.text_type.value}, {self.url})")
    