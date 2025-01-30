from textnode import *
from htmlnode import *
from generate_page import copy_dir_to, generate_page

def main():
    copy_dir_to("static", "public")
    generate_page("content/index.md", "template.html", "public")

main()