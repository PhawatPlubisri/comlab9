from flask import Flask
 
app = Flask(__name__)
 
@app.route('/<opt>/<float:a>/<float:b>')
def cal(opt,a,b):
    if opt == 'add':
      ans = a+b
    elif opt == 'sub':
      ans = a-b
    elif opt == 'mul':
      ans = a*b
    elif opt == 'div':
      if b == 0 :
        return 'can not divided be zero'
      else :
        ans = a/b
    else :
        return 'It is invalid'  
    return f'<h3>{ans}</h3>'
 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port='80')