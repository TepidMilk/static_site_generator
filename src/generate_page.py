import os
import shutil
from markdown_html import markdown_to_html_node, extract_title

#This function recursively copies files from source dir to destination dir
def copy_dir_to(source, destination):
    if not os.path.exists(source):
        raise Exception
    if os.path.isfile(source):
        return shutil.copy(source, destination)
    if os.path.exists(destination):
        shutil.rmtree(destination)
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