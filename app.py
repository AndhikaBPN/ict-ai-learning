from questions import QUESTIONS
from flask import Flask, render_template, request, redirect, url_for, session
import joblib
import time


app = Flask(__name__)
app.secret_key = "ict_ai_secret_key"
model = joblib.load("model.pkl")

def analyze_learning_style(score, duration):
    if score >= 80 and duration <= 10:
        return "Cepat dan Mandiri"
    elif score >= 80:
        return "Teliti dan Analitis"
    elif score < 60 and duration <= 10:
        return "Perlu Pendampingan"
    else:
        return "Kesulitan Konseptual"

MATERIAL_RECOMMENDATION = {
    "Pemula": "Pelajari kembali materi dasar, konsep fundamental, dan gunakan video pengantar.",
    "Menengah": "Latih pemahaman dengan soal latihan tambahan dan contoh studi kasus.",
    "Lanjutan": "Eksplorasi materi lanjutan, proyek mandiri, dan sumber belajar tambahan."
}

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/quiz", methods=["POST"])
def quiz():
    subject = request.form.get("subject")
    selected_subject = QUESTIONS.get(subject)

    if not selected_subject:
        return redirect(url_for("index"))

    # SIMPAN WAKTU MULAI DI SESSION
    session["start_time"] = time.time()
    session["subject"] = subject

    return render_template(
        "quiz.html",
        subject_key=subject,
        subject_title=selected_subject["title"],
        questions=selected_subject["questions"],
    )

@app.route("/submit", methods=["POST"])
def submit():
    subject = session.get("subject")
    start_time = session.get("start_time")

    if not subject or not start_time:
        return redirect(url_for("index"))

    selected_subject = QUESTIONS.get(subject)
    questions = selected_subject["questions"]

    correct = 0

    for i, q in enumerate(questions, start=1):
        user_answer = request.form.get(f"q{i}")
        if user_answer == q["answer"]:
            correct += 1

    total_questions = len(questions)
    score = int((correct / total_questions) * 100)

    end_time = time.time()
    duration = max(1, int((end_time - start_time) / 60))  # menit (min 1)

    # =====================
    # AI ANALYSIS
    # =====================
    level = model.predict([[score, duration]])[0]

    # ANALISIS GAYA BELAJAR
    learning_style = analyze_learning_style(score, duration)

    # REKOMENDASI MATERI
    recommendation = MATERIAL_RECOMMENDATION.get(level, "-")

    # Bersihkan session
    session.pop("start_time", None)
    session.pop("subject", None)

    return render_template(
        "result.html",
        score=score,
        correct=correct,
        total=total_questions,
        duration=duration,
        level=level,
        learning_style=learning_style,
        recommendation=recommendation
    )

if __name__ == "__main__":
    app.run(debug=True)