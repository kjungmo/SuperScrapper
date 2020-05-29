from flask import Flask

app = Flask("SuperScrapper")

@app.route("/")
def home():
  return "<h1>Job Search</h1><form><input placeholder='What job do you want?' required/><button>Search</button>"



app.run(host="0.0.0.0")