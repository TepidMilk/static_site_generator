from textnode import *

def main():
    item = TextNode("This is a text node", TextType.BOLD_TEXT.value, "https://www.boot.dev")    

    print(item.text_type)

main()