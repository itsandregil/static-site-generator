import logging
import os
import shutil

from src.htmlparser import markdown_to_html_node
from src.markdown_blocks import markdown_to_blocks

logging.basicConfig(level=logging.INFO)


def extract_markdown_title(markdown: str) -> str:
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block.startswith("# "):
            return block.strip("# ")
    raise Exception("Markdown content must have a title")


def generate_page(from_path: str, template_path: str, dest_path: str) -> None:
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as file:
        markdown_content = file.read()
    with open(template_path, "r") as file:
        template_content = file.read()

    page_title = extract_markdown_title(markdown_content)
    html = markdown_to_html_node(markdown_content).to_html()
    html_content = template_content.replace("{{ Title }}", page_title)
    html_content = template_content.replace("{{ Content }}", html)

    if not os.path.exists(dest_path):
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w") as file:
        file.write(html_content)


def copy_files(source: str, destination: str) -> None:
    for file in os.listdir(source):
        src_path = os.path.join(source, file)
        dst_path = os.path.join(destination, file)
        if os.path.isfile(src_path):
            shutil.copy(src_path, dst_path)
            logging.info(f"Copying file from {src_path} to {dst_path}")
        else:
            os.mkdir(dst_path)
            copy_files(src_path, dst_path)


def copy_files_to_dir(source: str, destination: str) -> None:
    if os.path.exists(destination):
        shutil.rmtree(destination)
    os.mkdir(destination)
    copy_files(source, destination)


def main():
    copy_files_to_dir("static", "public")
    generate_page("content/index.md", "template.html", "public/index.html")


if __name__ == "__main__":
    main()
