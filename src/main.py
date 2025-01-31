from textnode import *
from htmlnode import *
import os
from generate_page import copy_dir_to, generate_page

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"

def main():
    copy_dir_to(dir_path_static, dir_path_public)
    generate_page(os.path.join(dir_path_content, "index.md"), template_path, os.path.join(dir_path_public, "index.html"))

main()