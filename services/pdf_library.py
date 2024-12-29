import os
import shutil

class PDFLibrary():

    @staticmethod
    def copy_pdfs(input_folder, output_folder):
        """
        Copies all PDFs from a folder and its subfolders to an output folder.
        
        Args:
            input_folder (str): Path to the input folder.
            output_folder (str): Path to the output folder.
        """

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        
        for root, _, files in os.walk(input_folder):
            for file in files:
                if file.lower().endswith('.pdf'):
                    source_path = os.path.join(root, file)
                    destination_path = os.path.join(output_folder, file)
                    
                    shutil.copy2(source_path, destination_path)
                    print(f"Copying: {source_path} -> {destination_path}")