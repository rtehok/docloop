import io
import os

import pytest
from werkzeug.datastructures import FileStorage

from src.app.routes.upload import allowed_file


@pytest.mark.usefixtures("client")
def test_upload_file(client, app):
    test_pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], 'test.pdf')
    with open(test_pdf_path, 'wb') as f:
        f.write(b'Test PDF Content')

    test_pdf = open(test_pdf_path, 'rb')
    pdf_file = FileStorage(stream=test_pdf, filename='test.pdf')

    response = client.post('/upload', data={'file': pdf_file})

    assert response.status_code == 200
    assert b'Files uploaded successfully.' in response.data

    uploaded_file_path = os.path.join(app.config['UPLOAD_FOLDER'], 'test.pdf')
    assert os.path.exists(uploaded_file_path)

    os.remove(uploaded_file_path)


def test_allowed_file():
    assert allowed_file('test.pdf')
    assert not allowed_file('test.txt')


@pytest.mark.usefixtures("client")
def test_max_content_length(client, app):
    content = b'x' * (app.config['MAX_CONTENT_LENGTH'] + 1)
    test_file = io.BytesIO(content)
    test_file.filename = 'large.pdf'

    response = client.post('/upload', data={'file': (test_file, 'large.pdf')})

    assert b'File size exceeds the limit.' in response.data
    assert response.status_code == 200

    test_file.close()
