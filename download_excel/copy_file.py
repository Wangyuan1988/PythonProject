from pathlib import Path
from shutil import copyfile
import os
import time
import random

for filename in Path(r'C:\Users\mark ya wang\Desktop\PythonScrapy\download_excel\PDF_new').glob('*.pdf'):
    print(filename)
    old_filename =str(filename).replace(".pdf","")
    old_filename = old_filename+"_old.pdf"

    os.rename(filename, old_filename)

    time.sleep(random.randint(10,120))

    copyfile(old_filename,filename)