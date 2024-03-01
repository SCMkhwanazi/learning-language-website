from flask import Flask,render_template


app = Flask(__name__)
LANGUAGES = [
  {
  'id': 1,
  'title': 'English',
},
  {
  'id': 2,
  'title': 'Sepedi',
  },
  {
  'id': 3,
  'title': 'Zulu',
  },
]
@app.route('/')
def hello_world():
  return render_template('home.html',languages = LANGUAGES)
  
if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)