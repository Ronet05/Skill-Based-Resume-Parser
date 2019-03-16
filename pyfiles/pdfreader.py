from zipfile import ZipFile
import PyPDF2
import re
import os
import csv
import requests
from scoreclass import Calc_Score
import json
#We will need to use flask to take the correct zipfile name. 
#The "files" list here is basically a container for objects.
class PDFReader:
    def extract_resumes(self, zipname):
        with ZipFile(zipname,'r') as zip:
            zip.extractall()
            files = zip.infolist()
        filenames = []
        zipf = zipname[:zipname.find('.')]
        foldername = zipf + "/"
        #Check for PDF files
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
        return [openfiles,filenames]

    def extract_skills(self, sentence, file_name, ID):
        sentence=sentence.lower()
        sentence = re.sub(r',|:|\(|\)', "", sentence)
        sentence = re.sub(r'/|\\', " ", sentence)
        words=sentence.split(" ")

        start_words=['skill','skills','abilities','languages']
        stop_words=['accomplishments','accomplishment','experience','education','objective','qualifications','qualification','summary',
                'awards','hobbies','passion','highlights','research','honors','interest','interests','background','history','profile',
                'link','internships','internship','email']
        skills=[]
        start=0
        for word in words:
            if(start==0):
                if(word in start_words):
                    start=1
            else:
                if(word in stop_words):
                    start=0
                else:
                    if(word not in skills):
                        skills.append(word)
        #print(skills)
        #print("\n")
        
        name=words[0]+" "+words[1]
        row=[ID,file_name,name,sentence]
        with open('cv_list.csv','a') as csvFile:
            writer=csv.writer(csvFile)
            
            writer.writerow(row)
        csvFile.close()
        
        return skills
        
    def analyze_resume(self, resume_file, file_name, ID):
        scorer=Calc_Score()
        reader = PyPDF2.PdfFileReader(resume_file)
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
        #print(sentence)
        resume_skills = self.extract_skills(sentence, file_name, ID)
        
        with open("skills_data.json", "r") as jsonfile:
            data = json.loads(jsonfile.read())
        jsonfile.close()
        
        jd = ['python', 'deep_learning','machine_learning']
        priority_skills = [7, 4, 5]
        analysis_score = scorer.skillscore_update(resume_skills, jd, priority_skills, data)
        
        return analysis_score