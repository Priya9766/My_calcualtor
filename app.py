
from flask import Flask,request,render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    user_input=request.form
    print(user_input)
    A=int(user_input['a'])
    B=int(user_input['b'])

    result = A+B
   

    return render_template('index.html', calculate=result)
if __name__=='__main__':
    app.run(debug=True)