__version__ = '0.0.1'

import os
import fitz
from PIL import Image
from PyPDF2 import PdfFileReader, PdfFileWriter
from tabula import read_pdf
import tabula
import camelot
import numpy as np
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest
import io
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

class Table:
    def __init__(self,address):
        self._address = address


    def extractTableCsv(self):
        if 'extractedTablesCsv' in os.listdir():
            pass
        else:
            os.mkdir('extractedTablesCsv')
        try:
            tables = tabula.convert_into(self._address,"extractedTablesCsv/extractedCSVAll.csv",pages='all')
        except FileNotFoundError:
            print("[!] File not found Invalid address")
        except Exception as e:
            print(e)

    def extractTableJson(self):
        if 'extractedTablesJson' in os.listdir():
            pass
        else:
            os.mkdir('extractedTablesJson')
        try:
            tables = tabula.convert_into(self._address,"extractedTablesJson/extractedJsonAll.json",pages='all')
        except FileNotFoundError:
            print("[!] File not found Invalid address")
        except Exception as e:
            print(e)

    def extractTableHTML(self):
        if 'extractedTablesHTML' in os.listdir():
            pass
        else:
            os.mkdir('extractedTablesHTML')
        try:
            tables = camelot.read_pdf(self._address,pages='all')
            if len(tables)<1:
                print("[!] No Table Found")
                return
            tables.export("extractedTablesHTML/tablesHTMLAll.html", f="html")
        except FileNotFoundError:
            print("[!] File not found Invalid address")
        except Exception as e:
            print(e)

    def extractSpecPageTableHTML(self,page):
        if 'extractedTablesHTML' in os.listdir():
            pass        
        else:
            os.mkdir('extractedTablesHTML')
        try:
            tables = camelot.read_pdf(self._address,pages=str(page))
            if len(tables)<1:
                print("[!] No Table Found")
                return
            tables.export(f"extractedTablesHTML/tablesHTML{page}.html", f="html")
        except FileNotFoundError:
            print("[!] File not found Invalid address")
        except IndexError:
            print("[!] Page Not Found")
        except Exception as e:
            print(e)

    def extractSpecPageTableCsv(self,page):
        if 'extractedTablesCsv' in os.listdir():
            pass
       
        else:
            os.mkdir('extractedTablesCsv')
        try:
            tables = tabula.read_pdf(self._address,pages='all')
            if len(tables)<page:
                print('[!] Invalid Page Number')
                return
            tables = tabula.convert_into(self._address, f"extractedTablesCsv/OutputCsv{page}.csv", output_format="csv", pages=page)
        except FileNotFoundError:
            print("[!] File not found Invalid address")
        except Exception as e:
            print(e)
    def extractSpecPageTableJson(self,page):
        if 'extractedTablesJson' in os.listdir():
            pass
        else:
            os.mkdir('extractedTablesJson')
        try:
            tables = tabula.read_pdf(self._address,pages='all')
            if len(tables)<page:
                print('[!] Invalid Page Number')
                return
            tables = tabula.convert_into(self._address, f"extractedTablesJson/OutputJson{page}.json", output_format="json", pages=page)
        except FileNotFoundError:
            print("[!] File not found Invalid address")
        except TypeError:
            print('Please Enter a Page Number')
        except Exception as e:
            print(e)

class Image:
    def __init__(self,address):
        self._address = address

    def extractImageAll(self):
        if 'extractedImages' in os.listdir():
            pass
        else:
            os.mkdir('extractedImages')
        doc = fitz.open(self._address)
        for i in range(len(doc)):
            for img in doc.getPageImageList(i):
                if len(doc.getPageImageList(i))==0:
                    print(f'[!]No Image Found on {i}')
                print(type(img))
                xref = img[0] 
                pix = fitz.Pixmap(doc, xref)
                if pix.n < 5: 
                    pix.writePNG("extractedImages/p%s-%s.png" % (i, xref))
                else: 
                    pix1 = fitz.Pixmap(fitz.csRGB, pix)  
                    pix1.writePNG("extractedImages/p%s-%s.png" % (i, xref))
                    pix1 = None  
                pix = None  
    def extract_images(pdf, pages):
        threads = []
        for page in pages:
            temp = threading.Thread(target=extract_image, args=(pdf, page, ))
            temp.start()
            print(f"thread launched for page - {page}") 
        extract_images("PDF_Samples/AutoCad_Diagram.pdf", pages=list(range(19)))
    def extractImageSpecPage(self,page):
        if 'extractedImages' in os.listdir():
            pass
        else:
            os.mkdir('extractedImages')
        doc = fitz.open(self._address)
        if len(doc)<page:
            print("[!]Page Not Found")
            return
        for i in range(len(doc)):
            if i==page:
                if len(doc.getPageImageList(i))==0:
                    print('[!]No Image Found')
                    return
                for img in doc.getPageImageList(i):
                    xref = img[0]  
                    pix = fitz.Pixmap(doc, xref)
                    if pix.n < 5:  
                        pix.writePNG("extractedImages/p%s-%s.png" % (i, xref))
                    else:  
                        pix1 = fitz.Pixmap(fitz.csRGB, pix)  
                        pix1.writePNG("extractedImages/p%s-%s.png" % (i, xref))
                        pix1 = None  
                    pix = None 


class Text:
    def __init__(self,address):
        self._address = address


    def extractTextAll(self):
        extractedtext = ""
        if 'extractedTextAll' in os.listdir():
            pass
        else:
            os.mkdir('extractedTextAll')
        try:
            rsrcmgr = PDFResourceManager()
            retstr = io.StringIO()
            codec = 'utf-8'
            laparams = LAParams()
            device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
            fp = open(self._address, 'rb')
            interpreter = PDFPageInterpreter(rsrcmgr, device)
            password = ""
            maxpages = 0
            caching = True
            pagenos = set()

            for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages,password=password,caching=caching,check_extractable=True):
                interpreter.process_page(page)

            fp.close()
            device.close()
            extractedtext = retstr.getvalue()
            retstr.close()
            lines = extractedtext.split("\n")
            non_empty_lines = [line for line in lines if line.strip() != ""]
            string_without_empty_lines = ""
            for line in non_empty_lines:
                string_without_empty_lines += line + "\n"
            with io.open('extractedTextAll/extractText.txt','w',encoding='utf-8') as f:
                f.write(string_without_empty_lines)
                f.close()
            return string_without_empty_lines
        except FileNotFoundError:
            print("[!] No File Found ")
            return

    def extractTextSpecPage(self,page):
        extractedtext = ""
        if 'extractedTextAll' in os.listdir():
            pass
        else:
            os.mkdir('extractedTextAll')
        try:
            pdf = PdfFileReader(self._address)
        except FileNotFoundError:
            print("[!] No File Found ")
            return
        try:
            pageObj = pdf.getPage(page)
            lines = pageObj.extractText().split("\n")
            non_empty_lines = [line for line in lines if line.strip() != ""]
            extractedtext = ""
            for line in non_empty_lines:
                extractedtext += line + "\n"
            with io.open(f'extractedTextAll/extractTextPage{page}.txt','w',encoding='utf-8') as f:
                f.write(extractedtext)
                f.close()
        except IndexError:
            print('No page found ')
        except Exception as e:
            print(e)
        
        return extractedtext
class Summarize:
    def __init__(self,address):
        self._address=address  #address
        # try:
        #     nlp = spacy.load('en') #load 
        # except OSError:
        #     print('Downloading language model for the spaCy POS tagger\n'
        #     "(don't worry, this will only happen once)")
        #     from spacy.cli import download   #download    
        #     download('en')
        #     nlp = spacy.load('en')
    def summarizer(self):
        text = Text(self._address)  #text
        text = text.extractTextAll() #extract 
        if len(text) == 0:
            print('No text extraction available in pdf')
            exit(0)
        stopwords = list(STOP_WORDS) 
        stopwords.append(',')
        nlp = spacy.load('en_core_web_sm') #load en_core_Web_sm lib
        doc = nlp(text) #load all text in nlp
        tokens = [token.text for token in doc] #tokeniztion
        word_frequencies = {}
        for word in doc:
            if word.text.lower() not in stopwords:
                if word.text.lower() not in punctuation:
                    if word.text not in word_frequencies.keys():
                        word_frequencies[word.text] = 1
                    else:
                        word_frequencies[word.text]+=1

        max_frequency = max(word_frequencies.values())
        for word in word_frequencies.keys():
            word_frequencies[word] = word_frequencies[word]/max_frequency

        sentence_tokens = [sent for sent in doc.sents]

        sentence_scores = {}
        for sent in sentence_tokens:
            for word in sentence_tokens:
                for word in sent:
                    if word.text.lower() in word_frequencies.keys():
                            if sent not in sentence_scores.keys():
                                sentence_scores[sent] = word_frequencies[word.text.lower()]
                            else:
                                sentence_scores[sent] += word_frequencies[word.text.lower()]

        select_length = int(len(sentence_tokens)*0.3)

        summary = nlargest(select_length,sentence_scores,key=sentence_scores.get)

        final_summary = [word.text for word in summary]

        summary = ''.join(final_summary)
        if 'extractedPdfSummary' in os.listdir():
            pass
        else:
            os.mkdir('extractedPdfSummary')
        with io.open('extractedPdfSummary/extractedsummary.txt','w',encoding='utf-8') as f:
            if len(summary) != 0:
                f.write(summary)
            f.close