import streamlit as st
from docx import Document
from PIL import Image, ImageDraw, ImageFont
import tempfile
import os

# Function to convert DOCX to images (simplified version)
def docx_to_images(docx_path):
    doc = Document(docx_path)
    image_paths = []
    
    for page_num, para in enumerate(doc.paragraphs):
        # Create an image for each paragraph (as a basic example)
        img = Image.new('RGB', (800, 600), color='white')
        draw = ImageDraw.Draw(img)
        font = ImageFont.load_default()
        draw.text((10, 10), para.text, fill="black", font=font)

        # Save image to a temporary file
        temp_image = tempfile.NamedTemporaryFile(delete=False, suffix=f'.page{page_num+1}.png')
        img.save(temp_image, 'PNG')
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

        # Convert DOCX to images (simplified approach)
        image_paths = docx_to_images("temp.docx")

        # Display each image in the app
        for image_path in image_paths:
            img = Image.open(image_path)
            st.image(img, caption=f"Page {image_paths.index(image_path) + 1}")

        # Clean up temporary files
        os.remove("temp.docx")
        for image_path in image_paths:
            os.remove(image_path)

if __name__ == "__main__":
    main()
