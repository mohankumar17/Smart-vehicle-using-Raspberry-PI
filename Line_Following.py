import RPi.GPIO as IO
IO.setwarnings(False)
IO.setmode(IO.BCM)

def linefollowing():
    IO.setup(22,IO.IN)
    IO.setup(23,IO.IN)
    IO.setup(4,IO.OUT)
    IO.setup(25,IO.OUT)
    IO.setup(17,IO.OUT)
    IO.setup(18,IO.OUT)
    while True:
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
        elif(IO.input(22)==True and IO.input(23)==False):
            IO.output(4,True)
            IO.output(25,False)
            IO.output(17,False)
            IO.output(18,False)
        else:
            IO.output(4,True)
            IO.output(25,True)
            IO.output(17,True)
            IO.output(18,True)
linefollowing()
