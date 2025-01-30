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

"""Generates a webpage. 
Takes contents from from_path and inserts them into template_path.
Then writes it to dest_path to be generated."""
def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as f:
        content = f.read()
    
    print(content)