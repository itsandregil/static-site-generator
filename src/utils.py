from .text_node import TextType, TextNode
from typing import Literal
import re


Delimiter = Literal["**", "_", "`"]

# TODO: Build support nested inline elements
def split_node_delimiter(
    old_nodes: list[TextNode],
    delimeter: Delimiter,
    text_type: TextType,
) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)

        parts = node.text.split(sep=delimeter)
        if len(parts) % 2 == 0:
            raise Exception("Invalid markdown syntax")

        split_nodes = []
        for i, part in enumerate(parts):
            if not part:
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(part, TextType.TEXT))
            else:
                split_nodes.append(TextNode(part, text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)


def extract_markdown_links(text: str) -> list[tuple[str, str]]:
    return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)


def split_nodes_image(old_nodes: list[TextNode]):
    pass


def split_nodes_links(old_nodes: list[TextNode]):
    pass
