from flask import Flask, request, render_template
from io import BytesIO
from base64 import b64encode
import qrcode

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def generate():
    mem = BytesIO()
    data = request.form.get('link')  # Get the link from the form
    image = qrcode.make(data)       # Generate the QR code
    image.save(mem, 'PNG')          # Save it as a PNG in memory
    mem.seek(0)

    # Convert the image to base64
    base_64_image = "data:image/png;base64," + b64encode(mem.getvalue()).decode('utf-8')
    return render_template('index.html', data=base_64_image)

if __name__ == '__main__':
    app.run(debug=True, port=5001)

