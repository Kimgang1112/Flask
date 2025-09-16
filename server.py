from flask import Flask, render_template

app = Flask(__name__)

# 홈 페이지 라우트
@app.route("/")
def home():
    return render_template("index.html")

# 소개 페이지 라우트
@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
