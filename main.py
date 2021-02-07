from flask import Flask, request, render_template
app = Flask('app')
import json
import requests
from waitress import serve
# ---------------------
#----------------------
#---------------------
#Add your keys accordingly
secret = 'Your Secret Key'#keep it secret ;)
clikey="Your Client Key"
#---------------------
#-----------------------------
#--------------------------------------------
@app.route('/')
def hello_world():
  return render_template("index.html", clikey=clikey)
@app.route('/', methods=['POST'])
def postindex():
  r = requests.post('https://www.google.com/recaptcha/api/siteverify', data = {'secret' : secret, 'response' : request.form['g-recaptcha-response']})
  google_response = json.loads(r.text)
  
  if google_response['success'] == True:
    return "Success!"
  elif google_response['success'] == False:
    return "Please redo the captcha" + render_template("index.html")
print('''Made by spacehold. By law, you are required to keep this credit.
You must first run this. Then get the web URL domain for this repl. Then when adding a domain to https://www.google.com/recaptcha/admin/create you must add it like Recaptcha.supergamer1.repl.co NOT https://Recaptcha.supergamer1.repl.co.
Then add the secret and clikey accordingly.

THIS WILL NOT WORK IN REPLITS PREVIEW TAB, CREATE A NEW TAB AND OPEN IT.





































READ ABOVE

_________________________________''')
serve(app)