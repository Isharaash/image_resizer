from flask import Flask, render_template, request, send_file
from PIL import Image
import os
from io import BytesIO

app = Flask(__name__)

# Directory to save uploaded files
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/resize', methods=['POST'])
def resize():
    try:
        # Get the uploaded file
        file = request.files['image']
        if not file:
            return "No file uploaded!", 400

        # Get the desired dimensions
        width = int(request.form['width'])
        height = int(request.form['height'])

        # Open the image
        image = Image.open(file)

        resized_image = image.resize((width, height))

        image_io = BytesIO()
        resized_image.save(image_io, format=image.format)
        image_io.seek(0)

        # Send the resized image back to the user
        return send_file(
            image_io,
            mimetype=f'image/{image.format.lower()}',
            as_attachment=True,
            download_name=f'resized_{file.filename}'
        )
    except Exception as e:
        return str(e), 500
    

@app.route('/rapid_resizer')
def rapid_resizer():
    return render_template('rapid_resizer.html')

@app.route('/rapid_resize', methods=['POST'])
def rapid_resize():
    try:
        # Get the uploaded file
        file = request.files['image']
        if not file:
            return "No file uploaded!", 400

        # Open the image
        image = Image.open(file)

        # Fixed width
        width = 2500

        # Get the aspect ratio
        aspect_ratio = image.width / image.height

        # Calculate the height based on the aspect ratio and fixed width
        height = int(width / aspect_ratio)

        # If the calculated height exceeds 1800px, adjust it
        if height > 1800:
            height = 1800
            width = int(height * aspect_ratio)

        # Resize the image with the new width and height
        resized_image = image.resize((width, height))

        # Save the resized image to memory
        image_io = BytesIO()
        resized_image.save(image_io, format=image.format)
        image_io.seek(0)

        # Send the resized image back to the user
        return send_file(
            image_io,
            mimetype=f'image/{image.format.lower()}',
            as_attachment=True,
            download_name=f'rapid_resized_{file.filename}'
        )
    except Exception as e:
        return str(e), 500



if __name__ == '__main__':
    app.run(debug=True)
