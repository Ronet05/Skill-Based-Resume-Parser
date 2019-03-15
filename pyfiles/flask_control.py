from flask import Flask, render_template, request, url_for
from werkzeug import secure_filename
import requests

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
      job_desc=request.form.get("jobdesc")
      num_rank=request.form.get("rank")
      req_details=[job_desc,num_rank]
      
      
      return render_template('printresult.html', details=req_details)
#def print_result():
#    return render_template('printresult.html', transfer=pdfreader)
		
if __name__ == '__main__':
   app.run(debug = True)



