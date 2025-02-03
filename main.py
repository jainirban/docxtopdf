import streamlit as st
from docx import Document
from pdf2image import convert_from_path
from PIL import Image
import tempfile
import os

# Function to convert DOCX to PDF
def docx_to_pdf(docx_path):
    # We will use LibreOffice to convert DOCX to PDF in the background
    os.system(f'libreoffice --headless --convert-to pdf {docx_path}')
    return docx_path.replace('.docx', '.pdf')

# Function to convert PDF to images (one image per page)
def pdf_to_images(pdf_path):
    images = convert_from_path(pdf_path)
    image_paths = []
    for idx, image in enumerate(images):
        temp_image = tempfile.NamedTemporaryFile(delete=False, suffix=f'.page{idx+1}.png')
        image.save(temp_image, 'PNG')
        image_paths.append(temp_image.name)
    return image_paths

# Streamlit app
def main():
    st.title("DOCX to Image Viewer")

    uploaded_file = st.file_uploader("Upload your DOCX file", type="docx")

    if uploaded_file:
        # Save the uploaded DOCX file to a temporary location
        with open("temp.docx", "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        # Convert DOCX to PDF
        pdf_path = docx_to_pdf("temp.docx")

        # Convert PDF to images
        image_paths = pdf_to_images(pdf_path)

        # Display each image in the app
        for image_path in image_paths:
            img = Image.open(image_path)
            st.image(img, caption=f"Page {image_paths.index(image_path) + 1}")

        # Clean up temporary files
        os.remove("temp.docx")
        for image_path in image_paths:
            os.remove(image_path)
        os.remove(pdf_path)

if __name__ == "__main__":
    main()
