import logging
import os

from flask import Blueprint
from flask import render_template, request, send_from_directory, current_app
from werkzeug.utils import secure_filename

upload_bp = Blueprint('upload', __name__)


@upload_bp.route('', methods=['POST'])
def upload():
    error_messages = []
    content_length = request.content_length
    if content_length is not None and content_length > current_app.config['MAX_CONTENT_LENGTH']:
        error_messages.append('File size exceeds the limit.')
        return render_template('index.html', error_messages=error_messages)

    uploaded_files = request.files.getlist("file")

    for uploaded_file in uploaded_files:
        if uploaded_file.filename == '':
            error_messages.append('No file selected.')
        elif not allowed_file(uploaded_file.filename):
            error_messages.append('Invalid file type.')

    if error_messages:
        return render_template('index.html', error_messages=error_messages)

    for uploaded_file in uploaded_files:
        file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], secure_filename(uploaded_file.filename))
        uploaded_file.save(file_path)

    return render_template('index.html', message='Files uploaded successfully.')


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() == "pdf"


def get_file_size(file):
    file.seek(0, os.SEEK_END)
    file_size = file.tell()
    file.seek(0)
    return file_size


@upload_bp.route('<filename>')
def uploaded_file(filename):
    upload_folder = f"../{current_app.config['UPLOAD_FOLDER']}"
    return send_from_directory(upload_folder, filename)
