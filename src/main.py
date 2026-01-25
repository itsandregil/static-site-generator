import logging
import sys

from src.copystatic import copy_files_to_dir
from src.generate_page import generate_pages_recursive

logging.basicConfig(level=logging.INFO)


def main():
    base_path = "/"
    if len(sys.argv) > 1:
        base_path = sys.argv[1]
    copy_files_to_dir("static", "docs")
    generate_pages_recursive("content", "template.html", "docs", base_path)


if __name__ == "__main__":
    main()
