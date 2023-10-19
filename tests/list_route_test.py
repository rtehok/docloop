import os

import pytest


@pytest.mark.usefixtures("client")
def test_list_files_route(client):
    with open(os.path.join(client.application.config['UPLOAD_FOLDER'], 'file1.pdf'), 'w') as f:
        f.write('PDF Content 1')

    with open(os.path.join(client.application.config['UPLOAD_FOLDER'], 'file2.pdf'), 'w') as f:
        f.write('PDF Content 2')

    response = client.get('/list')

    assert response.status_code == 200

    assert b'file1.pdf' in response.data
    assert b'file2.pdf' in response.data
