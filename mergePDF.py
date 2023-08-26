"""Merge PDF utility."""

from abc import ABC
from pypdf import PdfWriter


class MergePDF(ABC):
    def __init__(self, ):
        """
        Initializes a new MergePDF instance.
        """

        self.writer = PdfWriter()
    
    def merge_files(self, files, output_file = "merged.pdf"):
        """
        Merges the given files.

        :param files: The list of files to merge.
        :param output_file: Output file.
        """

        for file in files:
            self.writer.append(file)

        self.writer.write(output_file)
        self.writer.close()
