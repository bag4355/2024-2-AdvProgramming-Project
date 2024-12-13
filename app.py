from flask import Flask, render_template
import os

app = Flask(__name__)

# 홈 페이지 라우팅
@app.route('/')
def index():
    # model_results.xml 파일 경로 설정
    xml_file_path = os.path.join(app.root_path, 'static', 'model_results.xml')
    return render_template('index.html', xml_file=xml_file_path)

if __name__ == '__main__':
    app.run(debug=True)
