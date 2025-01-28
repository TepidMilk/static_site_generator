import unittest

from markdown_blocks import *


class TestMardownBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = """
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
"""
        test = markdown_to_blocks(markdown)
        self.assertListEqual(
            [
                "# This is a heading",
                "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
            ],
            test
        )

    def test_markdown_to_blocks_newline(self):
        markdown = """
# This is a heading



This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
"""
        test = markdown_to_blocks(markdown)
        self.assertListEqual(
            [
                "# This is a heading",
                "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
            ],
            test
        )

    def test_block_to_block_type(self):
        block = "This is a paragraph"
        test = block_to_block_type(block)
        self.assertEqual(test, "paragraph")

    def test_block_type_heading_1(self):
        block = "# This is a heading"
        test = block_to_block_type(block)
        self.assertEqual(test, "heading")

    def test_block_type_heading_2(self):
        block = "## This is a heading"
        test = block_to_block_type(block)
        self.assertEqual(test, "heading")

    def test_block_type_heading_3(self):
        block = "### This is a heading"
        test = block_to_block_type(block)
        self.assertEqual(test, "heading")

    def test_block_type_heading_4(self):
        block = "#### This is a heading"
        test = block_to_block_type(block)
        self.assertEqual(test, "heading")

    def test_block_type_heading_5(self):
        block = "##### This is a heading"
        test = block_to_block_type(block)
        self.assertEqual(test, "heading")

    def test_block_type_heading_6(self):
        block = "###### This is a heading"
        test = block_to_block_type(block)
        self.assertEqual(test, "heading")
    
    def test_block_type_code(self):
        block = "```This is a block of code```"
        test = block_to_block_type(block)
        self.assertEqual(test, "code")

    def test_block_type_almost_code(self):
        block = "```This is a block of code"
        test = block_to_block_type(block)
        self.assertNotEqual(test, "code")
    
    def test_block_type_quote(self):
        block = "> This is a quote"
        test = block_to_block_type(block)
        self.assertEqual(test, "quote")

    def test_block_type_unordered_list(self):
        block = "- this is an unordered list item - second item"
        test = block_to_block_type(block)
        self.assertEqual(test, "unordered_list")

    def test_block_type_ordered_list(self):
        block = "1. This is an ordered list2. second item 3. third item"
        test = block_to_block_type(block)
        self.assertEqual(test, "ordered_list")