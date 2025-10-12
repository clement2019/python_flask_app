from flask import Flask,render_template
app = Flask(__name__)
 
@app.route('/')
def welcome():
   return "Welcome to Devops/cloud training!"

@app.route('/openings')
def openings():
    openings = ["Receptionist","Managers", "Help desk", "Engineers", "Technicians", "Developers", "Doctors"]
    return render_template("vaccant.html", openings=openings)
 
@app.route('/create')
def create():
   a=150
   b=50
   c=a*b
   return "This is the result " + str(c)
 
if __name__ == '__main__':
   app.run(host='127.0.0.1', port=3000, debug =True)