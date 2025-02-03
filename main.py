import streamlit as st
from spire.doc import Document, FileFormat
import os
from streamlit_pdf_viewer import pdf_viewer

def convert_to_pdf(docx_file):
    # Create word document
    document = Document()

    # Load a doc or docx file
    document.LoadFromFile(docx_file)

    # Save the document to PDF
    output_path = "converted_file.pdf"
    document.SaveToFile(output_path, FileFormat.PDF)
    document.Close()
    return output_path

# Streamlit App
st.title("DOCX to PDF Converter")

uploaded_file = st.file_uploader("Upload a DOCX file", type=["doc", "docx"])

if uploaded_file:
    st.write("File uploaded successfully. Converting...")

    # Save the uploaded file to a temporary location
    temp_path = "temp_uploaded_document.docx"
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Convert the DOCX file to PDF
    pdf_path = convert_to_pdf(temp_path)
    st.write("File converted successfully!")

    # Read the PDF file as binary data
    with open(pdf_path, "rb") as pdf_file:
        pdf_bytes = pdf_file.read()

        # Use the pdf_viewer to display the PDF
        pdf_viewer(input=pdf_bytes, width=700)

        st.download_button(
            label="Download PDF",
            data=pdf_bytes,
            file_name="converted_file.pdf",
            mime="application/pdf"
        )

    # Optionally, remove the temporary files
    os.remove(temp_path)
    os.remove(pdf_path)
