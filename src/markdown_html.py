from markdown_blocks import *
from htmlnode import *
from textnode import *
from inline_markdown import text_to_textnodes

def markdown_to_html_node(markdown):
    child_nodes = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        child = text_to_children(block)
        if block_type == "paragraph":
            node = HTMLNode("p", None, child)
        if block_type == "heading":
            i = (len(block) - len(block.lstrip("#")))
            node = HTMLNode(f"h{i}", )
    
    dev_node = ParentNode("div", child_nodes)
    return dev_node

def text_to_children(text):
    results = []
    node_list = []
    lines = text.split("\n")
    for line in lines:
        node_list.extend(text_to_textnodes(line))
        print(node_list)
    for node in node_list:
        results.append(text_node_to_html_node(node))
    return results