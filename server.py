from flask import Flask, request, render_template
import pymysql


app = Flask(__name__)

# DB 연결 설정
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "q1w2e3",
    "database": "Study",
    "charset": "utf8mb4"
}

# 홈 페이지
@app.route("/")
def index():
    return render_template("index.html")

# 데이터 저장
@app.route("/submit", methods=["POST"])
def save_db():
    value = request.form.get("value")   # form 데이터 받기

    # DB 연결
    conn = pymysql.connect(**db_config)
    cursor = conn.cursor()

    # 값 추가 (numcount 테이블의 num 컬럼)
    sql = "INSERT INTO numcount (num) VALUES (%s)"
    cursor.execute(sql, (value,))

    conn.commit()
    conn.close()

    return f"DB에 값 {value} 저장 완료!"

# 데이터 조회
@app.route("/list")
def list_data():
    conn = pymysql.connect(**db_config)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM numcount")
    rows = cursor.fetchall()

    conn.close()

    return {"data": rows}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
