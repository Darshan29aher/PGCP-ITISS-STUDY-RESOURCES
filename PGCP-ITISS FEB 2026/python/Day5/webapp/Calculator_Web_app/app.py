from flask import Flask, request, jsonify, render_template

def calculator(features:list):
    op = features[-1]
    num1 = float(features[0])
    num2 = float(features[1])
    match(op):
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1*num2
        case '/':
            return num1 / num2



app = Flask(__name__)

#127.0.0.1:8080/
@app.route('/') #index or landing page of website
def home():
    return render_template('index.html')
# 127.0.0.1:8080/calc
@app.route('/calc',methods=['POST']) #post method is used to send parameters in http request
def calc():
    '''
    For rendering results on HTML GUI'''
    try:
        features = []
        for x in request.form.values():
            features.append(x)
        #features = [x for x in request.form.values()]
        print("Features are ", features, " No of features =", len(features))
        output = calculator(features)

    except:
        output = "Some Error while calculation"
    # output =10
    return render_template('index.html', output_number='Calculation Output is {}'
        .format(output))


if __name__ == "__main__":
    # app.run(host="0.0.0.0",port=8080) # EC2 on AWS
    app.run(host="127.0.0.1",port=8080) # local machine