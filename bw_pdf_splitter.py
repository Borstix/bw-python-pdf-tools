#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import string
import sys
import random
from pathlib import Path
import pdftotext
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger

"""Funktion zum Hinzufügen von Hintergründen (z.B. Briefpapier) zu einer PDF-Datei.
"""


def split_pdf(inputfile,
              split_after_pagecount,
              split_after_keywords,
              split_after_keywords_negative,
              tmp_path,
              split_after_keywords_limit = 0):

    # Trennungskriterien prüfen
    split_pages = False
    split_keywords = False
    split_keywords_negative = False
    split_keyword_list = []
    split_keyword_list_negative = []

    if split_after_keywords is not None and len(split_after_keywords) > 0:
        # Keywords sind gesetzt
        split_keywords = True
        split_keyword_list = split_after_keywords.split("||")

    if split_after_keywords_negative is not None and len(split_after_keywords_negative) > 0:
        # Keywords sind gesetzt
        split_keywords_negative = True
        split_keyword_list_negative = split_after_keywords_negative.split("||")

    if split_after_pagecount is not None and split_after_pagecount > 0:
        # Seitentrenner gesetzt
        split_pages = True

    created_files = list()
    pdf_document = inputfile
    pdf_document_orig = Path(pdf_document).stem

    print("input_file: {}".format(inputfile))
    if pdf_document.lower().endswith(".pdf"):
        output_filename_base = "{}.pdf".format(random_string(10))
        print("output_base: {}".format(output_filename_base))

        split_counter = 0
        page_counter = 0

        pdf = PdfFileReader(pdf_document)
        pdftotextsource = open(pdf_document, "rb")
        pdftxt = pdftotext.PDF(pdftotextsource)





def random_string(string_length=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(string_length))