from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"


def markdown_to_blocks(markdown: str) -> list[str]:
    blocks = []
    sections = markdown.split("\n\n")
    for text in sections:
        text = text.strip()
        if text == "":
            continue
        blocks.append(text)
    return blocks


def block_to_blocktype(block: str) -> BlockType:
    if is_heading_block(block):
        return BlockType.HEADING
    elif is_code_block(block):
        return BlockType.CODE
    elif is_quote_block(block):
        return BlockType.QUOTE
    elif is_unordered_list_block(block):
        return BlockType.ULIST
    elif is_ordered_list_block(block):
        return BlockType.OLIST
    return BlockType.PARAGRAPH


def is_heading_block(block: str) -> bool:
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return True
    return False


def is_code_block(block: str) -> bool:
    lines = block.split("\n")
    return len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```")


def is_quote_block(block: str) -> bool:
    for line in block.split("\n"):
        if not line.startswith(">"):
            return False
    return True


def is_unordered_list_block(block: str) -> bool:
    for line in block.split("\n"):
        if not line.startswith("- ") and line[2:] != "":
            return False
    return True


def is_ordered_list_block(block: str) -> bool:
    i = 1
    for line in block.split("\n"):
        if not line.startswith(f"{i}. ") and line[2:] != "":
            return False
        i += 1
    return True
