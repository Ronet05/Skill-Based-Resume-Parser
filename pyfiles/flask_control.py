from flask import Flask, render_template, request, url_for
from werkzeug import secure_filename
import requests
from pdfreader import PDFReader
import csv
from ranking import  Ranker


app = Flask(__name__)
app.config['UPLOAD_FOLDER']="/home/ronet/Documents/Deloitte_Hackathon/pyfiles"
@app.route('/')
@app.route('/upload')
def upload():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ["GET","POST"])
def upload_file():
   if request.method == 'POST':
      f = request.files['zipfile']
      f.save(secure_filename(f.filename))
      #job_desc=request.form.get("jobdesc")
      #num_rank=request.form.get("rank")
      #req_details=[job_desc,num_rank]
      jd_skills=request.form.get("skills")
      c_sep_skills=jd_skills.split(',')
      final_skills=[]
      for skill in c_sep_skills:
         skill=skill.strip()
         skill=skill.replace(" " ,"_")
         final_skills.append(skill)
      
      reader=PDFReader()
      allresumes=reader.extract_resumes(f.filename)
      resumes_scores = {}
      #Initialize the headers by writing in to the csv, later we just append it.
      #row columns: id, filename, name, score, rank
      with open('cv_list.csv','w') as csvFile:
         writer=csv.writer(csvFile)            
         writer.writerow(["ID","filename","Name","Score","Rank"])
      csvFile.close()

      for index in range(len(allresumes[0])):
         
         analysed_list=reader.analyze_resume(allresumes[0][index], allresumes[1][index], index + 1, final_skills)
         resume_score = analysed_list[0]
         name=analysed_list[1]
         resumes_scores[allresumes[1][index]] = resume_score
         
         row=[index+1,allresumes[1][index],name,resume_score]
         
         with open('cv_list.csv','a') as csvFile:
            writer=csv.writer(csvFile)            
            writer.writerow(row)
         csvFile.close()
      
      ranker=Ranker()
      ranked_list=ranker.rank_csv()


      return render_template('printresult.html', scores=resumes_scores, title="View Scores",skills=final_skills, ranked_list=ranked_list)
#def print_result():
#    return render_template('printresult.html', transfer=pdfreader)
		
if __name__ == '__main__':
   app.run(debug = True)



