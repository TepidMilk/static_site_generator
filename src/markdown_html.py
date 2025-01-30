import re
from markdown_blocks import *
from htmlnode import *
from textnode import *
from inline_markdown import text_to_textnodes

def markdown_to_html_node(markdown):
    child_nodes = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == "paragraph":
            node = ParentNode("p", text_to_children(block))
        elif block_type == "heading":
            header = block.lstrip("# ")
            i = (len(block) - len(block.lstrip("#")))
            node = ParentNode(f"h{i}", text_to_children(header))
        elif block_type == "quote":
            quote = block.lstrip("> ")
            node = ParentNode("blockquote", text_to_children(quote))
        elif block_type == "code":
            code = block[3:-3]
            node = ParentNode("pre", [ParentNode("code", text_to_children(code))])
        elif block_type == "unordered_list":
            list_nodes = []
            lines = block.split("\n")
            for line in lines:
                sub = re.sub(r"-\s|\*\s", "", line)
                list_nodes.append(ParentNode("li", text_to_children(sub)))
            node = ParentNode("ul", list_nodes)
        elif block_type == "ordered_list":
            list_nodes = []
            lines = block.split("\n")
            for line in lines:
                sub = re.sub(r"\d\.\s", "", line)
                list_nodes.append(ParentNode("li", text_to_children(sub)))
            node = ParentNode("ol", list_nodes)
        child_nodes.append(node)
    div_node = ParentNode("div", child_nodes)
    return div_node

def text_to_children(text):
    results = []
    node_list = text_to_textnodes(text)
    for node in node_list:
        results.append(text_node_to_html_node(node))
    return results