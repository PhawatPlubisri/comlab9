from flask import Flask
import RPi.GPIO as GPIO
LEDR = 18
LEDG = 15
app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LEDR, GPIO.OUT)
GPIO.setup(LEDG, GPIO.OUT)
@app.route('/<led>/<opt>')
def cal(led,opt):
    if led == 'led1':
      if opt == 'on':
        GPIO.output(LEDR,True)
      else :
        GPIO.output(LEDR,False)
    elif led == 'led2':
      if opt == 'on':
        GPIO.output(LEDG,True)
      else :
        GPIO.output(LEDG,False)
    else :
        return 'Can not do this task'  
    return f'result : {led} - {opt}'
 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')