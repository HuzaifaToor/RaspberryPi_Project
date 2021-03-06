
from flask import Flask, render_template, Response, request, jsonify

from task1_motor_control.motor_controller import MotorController
'''from task2_sensor_control.sensor_controller import SensorController
from task3_opencv_control.opencv_controller import OpenCVController
from task3_opencv_control.camera import Camera

app = Flask(__name__)

motor_controller = MotorController()
opencv_controller = OpenCVController()
sensor_controller = SensorController()
should_stop_in_zone = False'''


@app.route('/')
def index():
    return render_template('index.html') 

'''def get_frame(camera):
    while True:
        frame = opencv_controller.get_frame(camera)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')            

@app.route('/video_feed')
def video_feed():
    return Response(get_frame(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')'''

@app.route('/start_motor')
def start_motor():
    # ...
    if not motor_controller.is_working():
        motor_controller.start_motor()
        return { 'success': True }

'''@app.route('/monitor')
def monitor():
    # ...
    return jsonify({
        "inZone": opencv_controller.is_in_zone(),
        "distance": sensor_controller.get_distance()
        })

@app.route('/stop_in_zone')
def stop_in_zone():
    # ...
    if opencv_controller.is_in_zone() == True:
        
        return { 'success': True }'''

if __name__ == '__main__':
    app.run(host='192.168.2.50',port='5000', debug = True)
    #app.run(host='0.0.0.0', debug=True)
