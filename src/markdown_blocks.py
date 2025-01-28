import re

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    return list(map(lambda x: x.strip(), filter(None, blocks)))

def block_to_block_type(block):
    heading = r"^##?#?#?#?#?\s\w"
    quote = r">"
    unordered_list = r"-\s|\*\s"
    ordered_list = r"\d\.\s"
    code_start = r"^```"
    code_end = r"```$"
    lines = block.split("\n")
    if re.match(heading, block):
        return "heading"
    if re.match(quote, block):
        for line in lines:
            if re.match(quote, line) == None:
                return "paragraph"
        return "quote"
    if re.search(code_start, block) and re.search(code_end, block):
        return "code"
    if re.match(unordered_list, block):
        for line in lines:
            if re.match(unordered_list, line) == None:
                return "paragraph"
        return "unordered_list"
    if re.match(ordered_list, block):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return "paragraph"
            i +=1
        return "ordered_list"
    return "paragraph"
