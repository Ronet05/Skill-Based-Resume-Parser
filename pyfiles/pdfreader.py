from zipfile import ZipFile
import PyPDF2
import re
import os
import csv
import requests
#We will need to use flask to take the correct zipfile name. 
#The "files" list here is basically a container for objects.
class PDFReader:
    def extractandread(zipname):








        
zipname = "resumes.zip"
with ZipFile(zipname,'r') as zip:
    zip.extractall()
    files = zip.infolist()

#openfiles is a list of already open pdf files, 
# ready to be fed into the pdffilereader fn.

filenames = []
zipf = zipname[:zipname.find('.')]
foldername = zipf + "/"
#print(foldername)
for i in range(0, len(files)):
    if(files[i].filename == foldername):
        continue
    else:
        if(files[i].filename.endswith(".pdf")):
            read_file = files[i]
            filenames.append(read_file.filename)
        else:
            continue

#create an array of open files for pdf reader to directly access
openfiles=[]
for i in range(len(filenames)):
    openfiles.append(open(filenames[i],'rb'))


index=0
ID=1
for f in openfiles:
    print("\nFile: {} \n".format(filenames[index]))
    #pdfFile=f
    reader = PyPDF2.PdfFileReader(f)
    sentence=' '
    words=[]
    for i in range(reader.numPages):
        text = reader.getPage(i)
        pageText = text.extractText()
        pageText=pageText.replace('\n','')
        for word in pageText.split():
            if re.findall('\s|\xc2|\xb7|[|]',word): continue
            words.append(word)
    
    sentence=sentence.join(words)
    
    name=words[0]+" "+words[1]
    row=[ID,filenames[index],name,sentence]
    with open('cv_list.csv','a') as csvFile:
        writer=csv.writer(csvFile)
        
        writer.writerow(row)
    
    
    index+=1
    ID+=1
    csvFile.close()   