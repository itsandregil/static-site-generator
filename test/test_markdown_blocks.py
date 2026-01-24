import unittest

from src.markdown_blocks import (
    BlockType,
    block_to_blocktype,
    is_code_block,
    is_heading_block,
    is_ordered_list_block,
    is_quote_block,
    is_unordered_list_block,
    markdown_to_blocks,
)


class TestMarkdownBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = "This is **bolded** paragraph\n\nThis is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line\n\n- This is a list\n- with items"
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
        markdown_heading_test_cases = [
            "# Hello World",
            "## This is a heading",
            "### This is a smaller heading",
            "#### Even smaller heading",
            "##### Almost there",
            "###### I'm almost a paragraph",
        ]

        for test_case in markdown_heading_test_cases:
            with self.subTest(test_case):
                self.assertTrue(is_heading_block(test_case))
                self.assertEqual(block_to_blocktype(test_case), BlockType.HEADING)

    def test_is_code_block(self):
        markdown_code_test_cases = [
            "```\nlet greeting = 'hello'\n```",
            "```\nfunction add(a, b) {\n  return a + b;\n}\n```",
            "```\nif (x > 0) {\n  console.log(x);\n}\n```",
            "```\n# This is not a heading\n- This is not a list\n```",
            "```\nprint('Hello, world!')\n```",
        ]
        for test_case in markdown_code_test_cases:
            with self.subTest(test_case):
                self.assertTrue(is_code_block(test_case))
                self.assertEqual(block_to_blocktype(test_case), BlockType.CODE)

    def test_is_quote_block(self):
        markdown_quote_test_cases = [
            "> This is a quote",
            "> Be yourself; everyone else is already taken.\n>\n> Oscar Wilde",
            "> First line of a quote\n> Second line continues the thought",
            "> Single-line quote with **bold** text",
            "> Quote with *italic* and `inline code`",
            "> Quote with a list-like line\n> - This is not a list, just text",
            "> Quote with numbering\n> 1. Still quoted text",
        ]
        for test_case in markdown_quote_test_cases:
            with self.subTest(test_case):
                self.assertTrue(is_quote_block(test_case))
                self.assertEqual(block_to_blocktype(test_case), BlockType.QUOTE)

    def test_is_paragraph_block(self):
        markdown_paragraph_test_cases = [
            "######## I'm not a heading",
            "This is a paragraph with **bolded** text",
            "A function is a piece of code that we can reuse defined by `def name()`",
            "Paragraph with *italic*, **bold**, and `inline code` mixed together",
            "A paragraph can include a [link](https://example.com) without becoming another block",
        ]
        for test_case in markdown_paragraph_test_cases:
            with self.subTest(test_case):
                self.assertFalse(is_heading_block(test_case))
                self.assertFalse(is_code_block(test_case))
                self.assertFalse(is_quote_block(test_case))
                self.assertFalse(is_ordered_list_block(test_case))
                self.assertFalse(is_unordered_list_block(test_case))
                self.assertEqual(block_to_blocktype(test_case), BlockType.PARAGRAPH)

    def test_is_unordered_list_block(self):
        markdown_ulist_test_cases = [
            "- Apple\n- Banana\n- Cherry",
            "- Single item",
            "- **Bold item**\n- *Italic item*\n- `Code item`",
        ]
        for test_case in markdown_ulist_test_cases:
            with self.subTest(test_case):
                self.assertTrue(is_unordered_list_block(test_case))
                self.assertEqual(block_to_blocktype(test_case), BlockType.ULIST)

    def test_is_ordered_list_block(self):
        markdown_olist_test_cases = [
            "1. Item with **bold**\n2. Item with *italic*\n3. Item with `code`",
            "1. Start\n2. Middle\n3. End",
            "1. Level one\n2. Level two\n3. Level three",
        ]
        for test_case in markdown_olist_test_cases:
            with self.subTest(test_case):
                self.assertTrue(is_ordered_list_block(test_case))
                self.assertEqual(block_to_blocktype(test_case), BlockType.OLIST)


if __name__ == "__main__":
    unittest.main()
