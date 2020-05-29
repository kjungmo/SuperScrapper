from flask import Flask, render_template, request, redirect
from scrapper import get_jobs
app = Flask("SuperScrapper")

@app.route("/")
def home():
  return render_template("potato.html")

@app.route("/report")
def report():
  word = request.args.get('word')
  if word:
    word = word.lower() #대문자 입력해도 소문자로 전환해줌
    jobs = get_jobs(word)
    print(jobs)
  else:   #문자 입력이 안된다면 처음으로 돌아가게끔
    return redirect("/")  #redirect를 import 해줘야 한다 잊지말자
  return render_template("report.html", searchingBy=word)


app.run(host="0.0.0.0")