import re
from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown: str) -> list[str]:
    blocks = []
    sections = markdown.split("\n\n")
    for text in sections:
        text = text.strip()
        if text == "":
            continue
        blocks.append(text)
    return blocks


# TODO: Check detections of blocks
def block_to_blocktype(block: str) -> BlockType:
    if is_heading_block(block):
        return BlockType.HEADING
    elif is_code_block(block):
        return BlockType.CODE
    elif is_quote_block(block):
        return BlockType.QUOTE
    elif is_unordered_list_block(block):
        return BlockType.UNORDERED_LIST
    elif is_ordered_list_block(block):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH


def is_heading_block(block: str) -> bool:
    return re.match(r"^#{1,6}\s.*", block) is not None


def is_code_block(block: str) -> bool:
    return block.startswith("```\n") and block.endswith("```")


def is_quote_block(block: str) -> bool:
    return block.startswith("> ")


def is_unordered_list_block(block: str) -> bool:
    return all(line.strip().startswith("- ") for line in block.split("\n"))


# FIX: Not parsing the ordered list correctly
def is_ordered_list_block(block: str) -> bool:
    lines = block.split("\n")
    for i in range(len(lines)):
        if lines[i][0] != i + 1:
            return False
    return True
