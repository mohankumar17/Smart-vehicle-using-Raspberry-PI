import time, datetime
import RPi.GPIO as GPIO
import telepot
from telepot.loop import MessageLoop
from flask import Flask
from flask import render_template, request
import RPi.GPIO as GPIO

def action(msg):
    chat_id = msg['chat']['id']
    print(chat_id)
    trail=chat_id
    command = msg['text']
    print 'Received: %s' % command     
                        
    if command=='linefollowing' or command == '1':
        linefolllowing()
        
    elif command == 'web interface' or command == '2':
        webcontrol()
        
    elif command == 'obstacleavoiding' or command=='3':
        ultrasonic()

    else:
        telegram_bot.sendMessage (trail, str("test string"))
        
                               
telegram_bot = telepot.Bot('523941593:AAFRkZ7Ue2ktbX0-ei6kxer7wvCHywHN7oA')
print (telegram_bot.getMe())
MessageLoop(telegram_bot, action).run_as_thread()
print 'Up and Running....'
def linefolllowing():
    IO.setwarnings(False)
    IO.setmode(IO.BCM)
    IO.setup(22,IO.IN)
    IO.setup(23,IO.IN)
    IO.setup(4,IO.OUT)
    IO.setup(25,IO.OUT)
    IO.setup(17,IO.OUT)
    IO.setup(18,IO.OUT)
    while 1:
        if(IO.input(22)==False and IO.input(23)==False):
            IO.output(4,True)
            IO.output(25,False)
            IO.output(17,True)
            IO.output(18,False)
        elif(IO.input(22)==False and IO.input(23)==True):
            IO.output(4,False)
            IO.output(25,True)
            IO.output(17,True)
            IO.output(18,False)
##      sleep(3)
        elif(IO.input(22)==True and IO.input(23)==False):
            IO.output(4,True)
            IO.output(25,False)
            IO.output(17,False)
            IO.output(18,False)
##        sleep(3)
        else:
            IO.output(4,True)
            IO.output(25,True)
            IO.output(17,True)
            IO.output(18,True)

def webcontrol():
    app = Flask(__name__)

m11=4
m12=25
m21=17
m22=18

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(m11, GPIO.OUT)
GPIO.setup(m12, GPIO.OUT)
GPIO.setup(m21, GPIO.OUT)
GPIO.setup(m22, GPIO.OUT)
GPIO.output(m11 , 0)
GPIO.output(m12 , 0)
GPIO.output(m21, 0)
GPIO.output(m22, 0)
print("Done")

a=1
@app.route("/")
def index():
    return render_template('index.html')

@app.route('/left_side')
def left_side():
    data1="LEFT"
    GPIO.output(m11 , 0)
    GPIO.output(m12 , 0)
    GPIO.output(m21 , 1)
    GPIO.output(m22 , 0)
    return 'true'

@app.route('/right_side')
def right_side():
    data1="RIGHT"
    GPIO.output(m11 , 1)
    GPIO.output(m12 , 0)
    GPIO.output(m21 , 0)
    GPIO.output(m22 , 0)
    return 'true'

@app.route('/up_side')
def up_side():
   data1="FORWARD"
   print data1
   GPIO.output(m11 , 1)
   GPIO.output(m12 , 0)
   GPIO.output(m21 , 1)
   GPIO.output(m22 , 0)
   return 'true'
@app.route('/down_side')
def down_side():
    data1="BACK"
    GPIO.output(m11 , 0)
    GPIO.output(m12 , 0)
    GPIO.output(m21 , 0)
    GPIO.output(m22 , 0)
    return 'true'

@app.route('/stop')
def stop():
    data1="STOP"
    GPIO.output(m11 , 0)
    GPIO.output(m12 , 1)
    GPIO.output(m21 , 0)
    GPIO.output(m22 , 1)
    return  'true'
if __name__ == "__main__":
    print "Start"
    app.run(host='localhost',port=5010)

    
def ultrasonic():
    GPIO.setmode(GPIO.BCM)                    #Set GPIO pin numbering
    GPIO.setup(4,GPIO.OUT)
    GPIO.setup(25,GPIO.OUT)
    GPIO.setup(17,GPIO.OUT)
    GPIO.setup(18,GPIO.OUT)
    TRIG = 26                                 #Associate pin 23 to TRIG
    ECHO = 19                                 #Associate pin 24 to ECHO

    print("Distance measurement in progress")

    GPIO.setup(TRIG,GPIO.OUT)                  #Set pin as GPIO out
    GPIO.setup(ECHO,GPIO.IN)                   #Set pin as GPIO in
    
    
    
    while True:
        GPIO.output(TRIG, False)                 #Set TRIG as LOW
        #print "Waitng For Sensor To Settle"
        time.sleep(1)                           

  GPIO.output(TRIG, True)                  #Set TRIG as HIGH
  time.sleep(0.00001)                      #Delay of 0.00001 seconds
  GPIO.output(TRIG, False)                 #Set TRIG as LOW

  while GPIO.input(ECHO)==0:               #Check whether the ECHO is LOW
      pulse_start = time.time()              #Saves the last known time of LOW pulse

  while GPIO.input(ECHO)==1:               #Check whether the ECHO is HIGH
      pulse_end = time.time()                #Saves the last known time of HIGH pulse 

  pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable
  
  distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
  distance = round(distance, 2)            #Round to two decimal points
  
  if distance > 2 and distance < 400:      #Check whether the distance is within range
      print "Distance:",distance - 0.5,"cm"  #Print distance with 0.5 cm calibration
      if (distance)<=20:
          GPIO.output(4,False)
          GPIO.output(25,True)
          GPIO.output(17,True)
          GPIO.output(18,False)
      else:
          GPIO.output(4,True)
          GPIO.output(25,False)
          GPIO.output(17,True)
          GPIO.output(18,False)
      else:
          print "Out Of Range"                   #display out of range

