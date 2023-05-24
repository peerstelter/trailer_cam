
from flask import Flask, render_template, Response
import io
import picamera

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def generate_video():
    with picamera.PiCamera() as camera:
        # Kamerakonfiguration
        camera.resolution = (960,540)
        camera.rotation = 0

        # Videoaufnahme und Streaming
        stream = io.BytesIO()
        for _ in camera.capture_continuous(stream, 'jpeg', use_video_port=True):
            stream.seek(0)
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + stream.read() + b'\r\n')
            stream.seek(0)
            stream.truncate()

@app.route('/video_feed')
def video_feed():
    return Response(generate_video(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False)
