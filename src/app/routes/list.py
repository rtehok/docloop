import os

from flask import Blueprint
from flask import render_template, current_app

list_bp = Blueprint('list', __name__)


@list_bp.route('')
def list_files():
    uploaded_files = []
    try:
        upload_folder = current_app.config['UPLOAD_FOLDER']
        all_files = os.listdir(upload_folder)
        pdf_files = [file for file in all_files if file.endswith('.pdf')]
        uploaded_files = pdf_files
    finally:
        return render_template('list.html', files=uploaded_files)
