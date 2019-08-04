# ROBOT_CAR USING RASPBERRY PI , COMPUTER VISION(OPENCV) AND IOT

For a robot that performs autonomously, the communication between the person and the robot is the most important factor. 
A significant awareness has been observed regarding the usage of such a technology. This research has a trivial involvement
in the development of such robots. Robots that functions fully autonomously should not only complete the jobs that are desired
of them but also somehow establish a connection between themselves and the person operating them. A lot of research has been
done of these kinds of robot and a lot of work still needs to be done. Keeping this in mind, there should be a capacity in the 
robot to get information from the surroundings while perusing the required object. The primary goal of our work was to design 
and fabricate a robot that detects the road lanes, traffic signs and drive the motors to move the car accordingly. A small camera 
records the video and the processor processes it to extract the desired information from it. Protecting the robot from collision
with the object is another problem that needs to be tackled so in order to do this, an ultrasonic sensor is used. All the processing
is carried out by the microprocessor while the control of the motors is carried out by the controller.

# Components Required:
Raspberry Pi(with python and OpenCV installed),
Two IR sensors,
Ultrasonic Sensor,
Picam,
Jumper Wires,
Motor Driver(L293D or L293N),
DC Motors.
# Prerequisite
Install opencv : https://www.pyimagesearch.com/2017/09/04/raspbian-stretch-install-opencv-3-python-on-your-raspberry-pi/ ,
Install Picam library: https://projects.raspberrypi.org/en/projects/getting-started-with-picamera
# Robot car functions: 
A) Line following -Follows the black line
B) Manual control using telegram -Can be manually controlled using Telegram application
C) Object avoiding -Avoids objects and move accordingly
D) Lane detection with live streaming using OpenCV -Detects and moves according to lanes 
E) Traffic Sign detection(FORWARD,LEFT,RIGHT,STOP) using OpenCV with Live feed - Detects and moves according to signs
F) Web Control with Livefeed -Can be controlled using web
(refer https://circuitdigest.com/microcontroller-projects/web-controlled-raspberry-pi-surveillance-robot to get better understanding about the function and also install the libraries required) 

Road Lane and Sign detection is done using Hough Transform technique. The pi camera attached on the top of the car inputs the video frames to raspberry pi. Python code process the frames and detects the lanes and signs using Hough transform technique. 

The live feed integration through the pi-cam placed in the car. The motor driver module enables the motor according to the signal from raspberry pi.  Camera Module attached on the top of Car – Send the Video with 30 FPS
Raspberry Pi –
                        -Open CV code -detect the lanes and Traffic signs based on the Video frames
                        -Controlling the Motor Driver to drive motors 
                       
Road Lane detection and sign detection:
Hough Transform technique is used to detect the road lanes and traffic sign like STOP, FORWARD, LEFT,RIGHT. Hough Transform is a popular technique to detect any shape, if you can represent that shape in mathematical form. It can detect the shape even if it is broken or distorted a little bit. We will see how it works for a line. A line can be represented as y = mx+c or in parametric form, as \rho = x \cos \theta + y \sin \theta where \rho is the perpendicular distance from origin to the line, and \theta is the angle formed by this perpendicular line and horizontal axis measured in counter-clockwise.

So, this project ensures that can get an efficient car for which there are many applications Like it can be used as a spy car or if we attach a gas sensor to it then it can used to measure the toxic level of gases in mines and obstacle avoiding mechanism forms the base of self-driven autonomous cars. 

# Conclusion:
Self-driving cars uses the detection techniques to move the car accordingly. They have potential benefits include reduced costs, increased safety, increased mobility, increased customer satisfaction and reduced crime. Safety benefits include a reduction in traffic collisions, resulting in injuries and related costs, including for insurance. Automated cars are predicted to increase traffic flow; provide enhanced mobility for children, the elderly, disabled, and the poor; relieve travellers from driving and navigation chores; increase fuel efficiency of vehicle; significantly reduce needs for parking space; reduce crime; and facilitate business models for transportation as a service, especially via the sharing economy.
