from flask import Flask
from functions import load_candidates, get_by_skill, get_by_pk, get_all

app = Flask(__name__)


@app.route("/")
def index():
    results = "<br>"
    for candidate in load_candidates():
        results += "Имя кандидата - " + candidate["name"] + "<br>"
        results += "Позиция кандидата - " + candidate["position"] + "<br>"
        results += "Навыки: " + candidate["skills"] + "<br>"
        results += "<br>"
    return f"<pre> {results} <pre>"


@app.route("/candidates/<int:x>")
def candidate_page(x):
    candidate = get_by_pk(x)
    url = candidate["picture"]
    results = "<br>"
    results += "Имя кандидата - " + candidate["name"] + "<br>"
    results += "Позиция кандидата - " + candidate["position"] + "<br>"
    results += "Навыки: " + candidate["skills"] + "<br>"
    results += "<br>"
    return f"<img src='({url})'> <pre> {results} <pre>"


@app.route("/skills/<skill>")
def skill_search(skill):
    candidates = get_by_skill(skill)
    results = "<br>"
    for candidate in candidates:
        results += "Имя кандидата - " + candidate["name"] + "<br>"
        results += "Позиция кандидата - " + candidate["position"] + "<br>"
        results += "Навыки: " + candidate["skills"] + "<br>"
        results += "<br>"
    return f"<pre> {results} <pre>"


if __name__ == "__main__":
    app.run()
