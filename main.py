from flask import Flask, render_template, request, redirect, send_file
from scrapper import get_jobs
from exporter import save_to_file

app = Flask("SuperScrapper")

db = {}

@app.route("/")
def home():
    return render_template("potato.html")


@app.route("/report")
def report():
  word = request.args.get('word')
  if word:
    word = word.lower()  #대문자 입력해도 소문자로 전환해줌
    existingjobs = db.get(word)
    if existingjobs:
      jobs = existingjobs
    else:
      jobs = get_jobs(word)
      db[word] = jobs

  else:  #문자 입력이 안된다면 처음으로 돌아가게끔
    return redirect("/")  #redirect를 import 해줘야 한다 잊지말자
  return render_template(
    "report.html", searchingBy=word, resultsNumber=len(jobs), jobs=jobs)




@app.route("/export")
def export():
  try:
    word = request.args.get('word')
    if not word:
      raise Exception();
    word = word.lower()
    jobs = db.get(word)
    if not jobs:
      raise Exception();
    save_to_file(jobs)
    return send_file("jobs.csv")
  except:
    return redirect("/")
  


app.run(host="0.0.0.0")
