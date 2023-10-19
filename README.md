# PDF Upload, List, and View App

This is a minimalistic Flask web application that allows you to upload, list, and view PDF files.

## Features

- **PDF Upload:** You can upload PDF files to the server using the web interface.

- **PDF List:** The app provides a list of uploaded PDF files, allowing you to see what's available.

- **PDF View:** You can click on a PDF file from the list to view its contents directly in your browser.

## Prerequisites

Before running the application, you need to have the following installed:

- Python 3.x with pip and venv installed
- poppler should be installed


    unix: sudo apt-get install poppler-utils
    macOS: brew install poppler
    windows: https://poppler.freedesktop.org/


## Installation

      git clone https://github.com/rtehok/docloop.git
      cd docloop
      python -m venv venv
      source venv/bin/activate
      pip install -r requirements.txt
      python src/app.py

The app will be available at http://localhost:5000.

## Running tests
    
    pip install -r test-requirements.txt
    PYTHONPATH=. pytest tests/

## Running the application with docker

    docker build -t docloop .
    docker run -p 5000:5000 docloop


## What's left to be done

- Configure file upload size via reverse proxy when running with gunicorn
- Use proper file storage (CDN)
- Manage duplicates
- Authentication / user management
- Handle deletion
- Handle multiple pages PDF