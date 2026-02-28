from flask import Flask, render_template, redirect, url_for
from quests_loader import load_quests

QUESTS = load_quests()


app = Flask(__name__)

@app.context_processor
def inject_quests():
    return dict(quests=QUESTS)


@app.route("/")
def index():
    return render_template("index.html", quests=QUESTS)


@app.route("/quest/<quest_id>/question/<int:question_id>")
def question(quest_id, question_id):
    quest = QUESTS.get(quest_id)

    if not quest:
        return redirect(url_for("index"))

    if question_id >= len(quest["questions"]):
        return redirect(url_for("result", quest_id=quest_id))

    return render_template(
        "question.html",
        quest=quest,
        quest_id=quest_id,
        question_id=question_id,
        question=quest["questions"][question_id]
    )


@app.route("/quest/<quest_id>/result")
def result(quest_id):
    quest = QUESTS.get(quest_id)

    if not quest:
        return redirect(url_for("index"))

    return render_template("result.html", quest=quest)



if __name__ == "__main__":
    app.run(debug=True)

# cd /var/www/uchitsya_veselo_history && git pull && sudo systemctl restart uchitsya_veselo