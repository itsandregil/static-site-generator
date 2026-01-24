from collections.abc import Callable

from src.inline_markdown import text_to_textnodes
from src.markdown_blocks import BlockType, block_to_blocktype, markdown_to_blocks
from src.nodes.html_node import HTMLNode
from src.nodes.parent_node import ParentNode
from src.nodes.text_node import TextNode, TextType, text_node_to_html_node


def markdown_to_html_node(markdown: str) -> HTMLNode:
    block_nodes = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_blocktype(block)
        html_node = blocktype_to_html_node(block, block_type)
        block_nodes.append(html_node)
    return ParentNode("div", block_nodes)


def blocktype_to_html_node(block: str, block_type: BlockType) -> ParentNode:
    if block_type == BlockType.HEADING:
        num_of_hashtags, text = block.split(maxsplit=1)
        children = text_to_children(text)
        return ParentNode(f"h{len(num_of_hashtags)}", children)
    if block_type == BlockType.QUOTE:
        text = get_block_text(block, get_cleaned_lines)
        children = text_to_children(text)
        return ParentNode("blockquote", children)
    if block_type == BlockType.CODE:
        text = get_block_text(block, get_codeblock_lines, "\n")
        text_node = TextNode(text, TextType.CODE)
        html_node = text_node_to_html_node(text_node)
        return ParentNode("pre", [html_node])
    if block_type == BlockType.OLIST:
        return ParentNode("ol", get_list_children(block))
    if block_type == BlockType.ULIST:
        return ParentNode("ul", get_list_children(block))
    if block_type == BlockType.PARAGRAPH:
        text = get_block_text(block, get_text_lines)
        children = text_to_children(text)
        return ParentNode("p", children)


def get_block_text(
    block: str, cb: Callable[[str], list[str]], sep: str | None = None
) -> str:
    if sep is not None:
        return f"{sep}".join(cb(block)) + sep
    return " ".join(cb(block))


def get_text_lines(block: str) -> list[str]:
    """Returns a list of block lines."""
    lines = []
    for line in block.split("\n"):
        line = line.strip()
        if line == "":
            continue
        lines.append(line)
    return lines


def get_cleaned_lines(block: str) -> list[str]:
    lines = get_text_lines(block)
    text_lines = [
        line.split(maxsplit=1)[1] for line in lines if len(line.split(maxsplit=1)) == 2
    ]
    return text_lines


def get_codeblock_lines(block: str) -> list[str]:
    return get_text_lines(block.strip("`"))


def get_list_children(block: str) -> list[HTMLNode]:
    children = []
    lines = get_cleaned_lines(block)
    for line in lines:
        line_children = text_to_children(line)
        children.append(ParentNode("li", line_children))
    return children


def text_to_children(text: str) -> list[HTMLNode]:
    children_nodes = []
    text_nodes = text_to_textnodes(text)
    for node in text_nodes:
        html_node = text_node_to_html_node(node)
        children_nodes.append(html_node)
    return children_nodes
