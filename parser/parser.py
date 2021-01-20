import docx
import logging


class Parser:
    def __init__(self, file_path):
        """
        File path must be absolute
        """
        try:
            with open(file_path) as read_file:
                self.document = docx.Document(read_file)
        except FileNotFoundError:
            logging.error(f"Missing file at {file_path}")

    def paragraph_replace(self, old, new):
        for para in document.paragraphs:
            if old in para.text:
                print(para.text)

    def table_replace(self, old, new):
        for table in document.tables:
            for row in table.rows:
                for cell in row.cells:
                    for para in cell.paragraphs:
                        if old in para.text:
                            print(para.text)

    def heading_replace(self, old, new):
        for content in document.paragraphs:
            if content.style.name=='Heading 1' or content.style.name=='Heading 2' or content.style.name=='Heading 3':
                print(content.text)
