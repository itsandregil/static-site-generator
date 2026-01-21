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
            continue
        split_nodes = []
        sections = node.text.split(delimeter)
        if len(sections) % 2 == 0:
            raise Exception("Invalid markdown syntax")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)


def extract_markdown_links(text: str) -> list[tuple[str, str]]:
    return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)


def split_nodes_images(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        images = extract_markdown_images(node.text)
        if not images:
            new_nodes.append(node)
            continue
        split_nodes = []
        current_text = node.text
        for alt_text, url in images:
            before, after = current_text.split(f"![{alt_text}]({url})", 1)
            if before:
                split_nodes.append(TextNode(before, TextType.TEXT))
            split_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
            current_text = after
        if current_text:
            split_nodes.append(TextNode(current_text, TextType.TEXT))
        new_nodes.extend(split_nodes)
    return new_nodes


def split_nodes_links(old_nodes: list[TextNode]):
    new_nodes = []
    for node in old_nodes:
        links = extract_markdown_links(node.text)
        if not links:
            new_nodes.append(node)
            continue
        split_nodes = []
        current_text = node.text
        for text, url in links:
            before, after = current_text.split(f"[{text}]({url})", 1)
            if before:
                split_nodes.append(TextNode(before, TextType.TEXT))
            split_nodes.append(TextNode(text, TextType.LINK, url))
            current_text = after
        if current_text:
            split_nodes.append(TextNode(current_text, TextType.TEXT))
        new_nodes.extend(split_nodes)
    return new_nodes


def text_to_textnodes(text: str) -> list[TextNode]:
    node = TextNode(text, TextType.TEXT)
    new_nodes = split_node_delimiter([node], "**", TextType.BOLD)
    new_nodes = split_node_delimiter(new_nodes, "_", TextType.ITALIC)
    new_nodes = split_node_delimiter(new_nodes, "`", TextType.CODE)
    new_nodes = split_nodes_images(new_nodes)
    new_nodes = split_nodes_links(new_nodes)
    return new_nodes
