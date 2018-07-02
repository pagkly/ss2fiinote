import os
import time
import shutil
import subprocess
import argparse
import sys

def parse_args():
    # Create the arguments
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-pdir",
        "--pdfmdir",
        help="Loc of PDFs. Example: -pdir /home/user"
    )
    return parser.parse_args()


args = parse_args()

if args.pdfmdir :
    relevant_path=args.pdfmdir
    included_extensions = ['pdf']
    pdf_names = [fn for fn in os.listdir(relevant_path)
                      if any(fn.endswith(ext) for ext in included_extensions)]
    print(len(pdf_names))
    
    for i in range(0,len(pdf_names)):
        print(pdf_names[i])
        ##sys.exit()
        subprocess.call("python3 ~/Documents/Docs/Tech/Automate/FN35AOCV/startpdf2note.py -pdir \""+relevant_path+"\" -p \""+pdf_names[i]+"\" -d 100 -t 1 -nc 1" ,shell=True)
    
    
