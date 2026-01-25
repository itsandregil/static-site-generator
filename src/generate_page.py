import os

from src.htmlparser import markdown_to_html_node
from src.markdown_blocks import markdown_to_blocks


def extract_markdown_title(markdown: str) -> str:
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block.startswith("# "):
            return block.strip("# ")
    raise Exception("Markdown content must have a title")


def replace_content(
    template_content: str, *, title: str, html: str, base_path: str
) -> str:
    return (
        template_content.replace("{{ Title }}", title)
        .replace("{{ Content }}", html)
        .replace('href="/', f"href={base_path}")
        .replace('src="/', f"src={base_path}")
    )


def generate_page(
    from_path: str, template_path: str, dest_path: str, base_path: str
) -> None:
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as file:
        markdown_content = file.read()
    with open(template_path, "r") as file:
        template_content = file.read()

    page_title = extract_markdown_title(markdown_content)
    html = markdown_to_html_node(markdown_content).to_html()
    html_content = replace_content(
        template_content,
        title=page_title,
        html=html,
        base_path=base_path,
    )

    if not os.path.exists(dest_path):
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w") as file:
        file.write(html_content)


def generate_pages_recursive(
    dir_content_path: str, template_path: str, dest_dir_path: str, base_path: str
) -> None:
    for file in os.listdir(dir_content_path):
        src_path = os.path.join(dir_content_path, file)
        dest_path = os.path.join(dest_dir_path, file)
        if not os.path.isdir(src_path) and not src_path.endswith(".md"):
            raise Exception(f"Content must have only markdown files: {src_path}")
        if os.path.isfile(src_path):
            dest_path = dest_path.replace(".md", ".html")
            generate_page(src_path, template_path, dest_path, base_path)
        else:
            generate_pages_recursive(src_path, template_path, dest_path, base_path)
