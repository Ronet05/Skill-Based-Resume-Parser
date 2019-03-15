from flask import Flask, render_template, request
from werkzeug import secure_filename
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
      job_desc=request.form["resume_filter"].get("jobdesc")
      num_rank=request.form["resume_filter"].get("rank")
      
      
      return 'file uploaded successfully'
		
if __name__ == '__main__':
   app.run(debug = True)



