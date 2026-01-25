import logging
import os
import shutil


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
