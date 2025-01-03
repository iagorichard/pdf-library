import argparse
import sys
from services.pdf_library import PDFLibrary

def main():
    
    # Makes the parser of the PDF library
    parser = argparse.ArgumentParser(description="PDF Library Tool")
    parser.add_argument("--option", required=True, help="Operation to perform (e.g., copy_all)")
    parser.add_argument("--folder_in", help="Path to the input folder")
    parser.add_argument("--folder_out", help="Path to the output folder")
    parser.add_argument("--rename_files", help="Path to the output folder")

    # Parses the arguments from the command line and stores them in the 'args' object
    args = parser.parse_args()

    # Checks the validity of the provided arguments and performs the required operation
    if args.option == "copy_all":
        if not args.folder_in or not args.folder_out:
            raise ValueError("For 'copy_all', both '--folder_in' and '--folder_out' must be specified.")
        
        print(f"Executing 'copy_all' with input folder: {args.folder_in} and output folder: {args.folder_out}")
        
        if not args.rename_files:
            PDFLibrary.copy_pdfs(args.folder_in, args.folder_out)    
        else:
            PDFLibrary.copy_pdfs(args.folder_in, args.folder_out, args.rename_files) 
    else:
        raise ValueError(f"Unknown option: {args.option}. Supported options: 'copy_all'.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
