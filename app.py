from flask import Flask, render_template
import xml.etree.ElementTree as ET

app = Flask(__name__)

# 모델 데이터를 XML 파일에서 읽어오는 함수
def parse_xml():
    tree = ET.parse('static/model_results.xml')
    root = tree.getroot()

    models = []
    
    # XML 파일에서 모델 데이터를 추출
    for model in root.findall('model'):
        name = model.get('name')
        target_variable = model.find('Target_Variable').text
        independent_variables = model.find('Independent_Variables').text
        model_type = model.find('Model_Type').text
        r2 = float(model.find('R2').text)
        nse = float(model.find('NSE').text)
        rmse = float(model.find('RMSE').text)
        cpi = float(model.find('CPI').text)
        formula = model.find('Formula').text
        
        # 모델 정보를 딕셔너리로 저장
        models.append({
            'name': name,
            'target_variable': target_variable,
            'independent_variables': independent_variables,
            'model_type': model_type,
            'r2': r2,
            'nse': nse,
            'rmse': rmse,
            'cpi': cpi,
            'formula': formula
        })
        
    # 모델을 CPI 값 기준으로 오름차순 정렬
    models.sort(key=lambda x: x['cpi'])
    
    return models

# 홈 페이지 라우팅
@app.route('/')
def index():
    # XML 데이터 읽어오기
    models = parse_xml()
    
    # 모델 상세 정보를 상위 20개만 추출
    top_20_models = models[:20]
    
    # 상위 20개 모델을 HTML로 전달
    return render_template('index.html', models=top_20_models)

if __name__ == '__main__':
    app.run(debug=True)
