import re
from textnode import TextNode, TextType

#Takes a list of TextNodes in markdown and converts them to a list of TextNodes with appropriate text typing.
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    results = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            results.append(node)
            continue
        split_nodes = []
        split_text = node.text.split(delimiter)
        for i in range(len(split_text)):
            if split_text[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(split_text[i], TextType.NORMAL))
            else:
                split_nodes.append(TextNode(split_text[i], text_type))
        results.extend(split_nodes)
    return results

#extracts a tuple of the alt text and image link
def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((http|ftp|https:\/\/[\w_-]+(?:(?:\.[\w_-]+)+)[\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])\)", text)
    return matches

#extracts a tuple of the anchor text and link
def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((http|ftp|https:\/\/[\w_-]+(?:(?:\.[\w_-]+)+)[\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])\)", text)
    return matches

def split_nodes_images(old_nodes):
    results = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            results.append(node)
            continue
        split_nodes = []
        split_text = re.split(r'(?=!\[)|(?<=[\)])', node.text)
        for i in range(len(split_text)):
            if split_text[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(split_text[i], TextType.NORMAL))
            else:
                image = extract_markdown_images(split_text[i])
                split_nodes.append(TextNode(image[0][0], TextType.IMAGES, image[0][1]))
        results.extend(split_nodes)
    return results

def split_nodes_links(old_nodes):
    results = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            results.append(node)
            continue
        split_nodes = []
        split_text = re.split(r'(?=[\[])|(?<=[\)])', node.text)
        if len(split_text) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(split_text)):
            if split_text[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(split_text[i], TextType.NORMAL))
            else:
                links = extract_markdown_links(split_text[i])
                split_nodes.append(TextNode(links[0][0], TextType.LINKS, links[0][1]))
        results.extend(split_nodes)
    return results

def text_to_textnodes(text):
    node = TextNode(text, TextType.NORMAL)
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)
    new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)
    new_nodes = split_nodes_images(new_nodes)
    new_nodes = split_nodes_links(new_nodes)
    return new_nodes
