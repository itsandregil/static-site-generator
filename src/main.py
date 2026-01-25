import logging

from src.copystatic import copy_files_to_dir
from src.generate_page import generate_pages_recursive

logging.basicConfig(level=logging.INFO)


def main():
    copy_files_to_dir("static", "public")
    generate_pages_recursive("content", "template.html", "public")


if __name__ == "__main__":
    main()
