import os

from PyPDF2 import PdfReader
from flask import Blueprint, send_from_directory
from flask import current_app
from flask import render_template
from pdf2image import convert_from_path

view_bp = Blueprint('view', __name__)


@view_bp.route('/<filename>')
def view_pdf(filename):
    file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
    pdf = PdfReader(file_path)

    pdf_text = ""
    for page in pdf.pages:
        pdf_text += page.extract_text()

    images = convert_from_path(file_path)
    image_names = []

    for count, image in enumerate(images):
        image_name = f'{filename}_{count}.jpg'
        image_path = os.path.join(current_app.config['IMAGES_FOLDER'], image_name)

        if not os.path.isfile(image_path):
            image.save(image_path, 'JPEG')

        image_names.append(image_name)

    return render_template('view.html', filename=filename, file_path=file_path, pdf_text=pdf_text, images=image_names)


@view_bp.route('/images/<image_name>')
def uploaded_image(image_name):
    image_folder = f"../{current_app.config['IMAGES_FOLDER']}"
    return send_from_directory(image_folder, image_name)
