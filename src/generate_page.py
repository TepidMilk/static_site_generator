import os
import shutil
from pathlib import Path
from markdown_html import markdown_to_html_node, extract_title



#This function recursively copies files from source dir to destination dir
def copy_dir_to(source, destination):
    if not os.path.exists(source):
        raise Exception
    if os.path.isfile(source):
        return shutil.copy(source, destination)
    os.mkdir(destination)
    for file in os.listdir(source):
        log = copy_dir_to(os.path.join(source, file), os.path.join(destination, file))

# turns markdown(from_path) into html(template_path) and writes it at dest_path
def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as markdown:
        content = markdown.read()
    with open(template_path, "r") as temp:
        template = temp.read()
    html = markdown_to_html_node(content).to_html()
    title = extract_title(content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    with open(dest_path, "w") as to_file:
        to_file.write(template)
    

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if os.path.isfile(dir_path_content) and dir_path_content.endswith(".md"):
        return generate_page(dir_path_content, template_path, dest_dir_path)
    elif os.path.isfile(dir_path_content) and not dir_path_content.endswith(".md"):
        return
    for file in os.listdir(dir_path_content):
        if os.path.isfile(os.path.join(dir_path_content, file)):
            dest_path = Path(file).with_suffix(".html")
            generate_pages_recursive(os.path.join(dir_path_content, file), template_path, os.path.join(dest_dir_path, dest_path))
        generate_pages_recursive(os.path.join(dir_path_content, file), template_path, os.path.join(dest_dir_path, file))