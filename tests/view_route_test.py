import os

import pytest
from PyPDF2 import PdfWriter


@pytest.mark.usefixtures("client")
def test_view_pdf(client, app):
    test_pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], 'test.pdf')

    pdf_writer = PdfWriter()
    pdf_writer.add_blank_page(200, 200)  # Adjust the page size as needed
    with open(test_pdf_path, 'wb') as f:
        pdf_writer.write(f)

    response = client.get('/view/test.pdf')

    assert response.status_code == 200

    image_name = 'test.pdf_0.jpg'
    image_path = os.path.join(app.config['IMAGES_FOLDER'], image_name)

    assert os.path.exists(image_path)

    os.remove(test_pdf_path)
    os.remove(image_path)
