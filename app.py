from flask import Flask, render_template
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.route('/')
def index():
    # XML 파일 경로
    xml_file_path = 'static/model_results.xml'
    
    # XML 파일을 파싱하여 데이터 가져오기
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    models = []

    # XML에서 모델 정보 추출
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

        # 모델 정보를 리스트에 저장
        models.append({
            'name': name,
            'modelType': model_type,
            'targetVariable': target_variable,
            'independentVariables': independent_variables,
            'r2': r2,
            'nse': nse,
            'rmse': rmse,
            'cpi': cpi,
            'formula': formula
        })

    return render_template('index.html', models=models)

if __name__ == '__main__':
    app.run(debug=True)

