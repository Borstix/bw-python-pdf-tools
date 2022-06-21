#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import string
import sys
import random
import pathlib
from typing import BinaryIO

from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger

"""Funktion zum Hinzufügen von Hintergründen (z.B. Briefpapier) zu einer PDF-Datei.
"""


def add_pdf_background(inputfile, background_file_first, background_file_following=""):

    if not os.path.exists(inputfile):
        print("Fehler: Eingabedatei {} nicht gefunden".format(inputfile))
        return False

    if not os.path.exists(background_file_first):
        print("Fehler: Hintergrunddatei {} nicht gefunden.".format(background_file_first))
        return False

    if len(background_file_following) > 0 and not os.path.exists(background_file_following):
        print("Fehler: Hintergrunddatei {} nicht gefunden.".format(background_file_following))
        return False

    pdf_reader = PdfFileReader(inputfile)

    reader_bg_first = PdfFileReader(background_file_first)
    bg_first = reader_bg_first.getPage(0)

    if len(background_file_following) > 0:
        reader_bg_following = PdfFileReader(background_file_following)
        bg_following = reader_bg_following.getPage(0)

    random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    destination_path = pathlib.Path(inputfile).parent.resolve()
    temp_file_name = "{}/{}.pdf".format(destination_path, random_string)

    pdf_writer = PdfFileWriter()

    for page in range(pdf_reader.getNumPages()):
        current_page = pdf_reader.getPage(page)
        if page == 0:
            current_page.mergePage(bg_first)
        else:
            if len(background_file_following) > 0:
                current_page.mergePage(bg_following)

        pdf_writer.addPage(current_page)

        with open(temp_file_name, "wb") as out:
            pdf_writer.write(out)

        os.replace(temp_file_name, inputfile)


argcount = len(sys.argv)
if argcount < 3:
    print("Usage: add_pdf_background input_file background_file_first background_file_following")
    exit()
else:
    t_inputfile = sys.argv[1]
    t_background_file_first = sys.argv[2]
    if len(sys.argv) == 4:
        t_background_file_following = sys.argv[3]
    else:
        t_background_file_following = ""
    add_pdf_background(t_inputfile, t_background_file_first, t_background_file_following)
