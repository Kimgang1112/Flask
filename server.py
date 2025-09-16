from flask import Flask

app = Flask(__name__)

# 홈 페이지
@app.route("/")
def home():
    return "Hello, Flask! 👋"

# 다른 경로 예제
@app.route("/about")
def about():
    return "This is the About page."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
