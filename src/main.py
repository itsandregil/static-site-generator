from src.htmlparser import markdown_to_html_node


def main():
    md = """
    This is **bolded** paragraph

    This is another paragraph with _italic_ text and `code` here
    This is the same paragraph on a new line

    - This is a list
    - with items
    """

    html_node = markdown_to_html_node(md)
    print(html_node.to_html())


if __name__ == "__main__":
    main()
