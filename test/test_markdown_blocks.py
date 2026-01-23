import unittest
from src.block_text import markdown_to_blocks, block_to_blocktype, is_heading_block, BlockType, is_code_block, is_quote_block

class TestMarkdownBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_is_heading_block(self):
        blocks = ["# Hello World", "### This is a smaller heading", "###### I'm almost a paragraph"]
        for block in blocks:
            with self.subTest(block):
                self.assertTrue(is_heading_block(block))
                self.assertEqual(block_to_blocktype(block), BlockType.HEADING)
    
    def test_is_not_heading(self):
        block = "######## I'm not a heading"
        self.assertFalse(is_heading_block(block))
        self.assertEqual(block_to_blocktype(block), BlockType.PARAGRAPH)

    def test_is_code_block(self):
        block = "```\nlet greeting = 'hello'\n```"
        self.assertTrue(is_code_block(block))
        self.assertEqual(block_to_blocktype(block), BlockType.CODE)

    
    def test_is_quote_block(self):
        block = "> To be or not to be"
        self.assertTrue(is_quote_block(block))
        self.assertEqual(block_to_blocktype(block), BlockType.QUOTE)