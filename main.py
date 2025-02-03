import streamlit as st
from spire.doc import *
from spire.doc.common import *
import os
import base64

def convert_to_pdf(docx_file):
    # Create word document
    document = Document()

    # Load a doc or docx file
    document.LoadFromFile(docx_file)

    # Save the document to PDF
    output_path = "output/converted_file.pdf"
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

    # Display the PDF file
    with open(pdf_path, "rb") as pdf_file:
        pdf_bytes = pdf_file.read()
        st.download_button(
            label="Download PDF",
            data=pdf_bytes,
            file_name="converted_file.pdf",
            mime="application/pdf"
        )
        st.write("Use the below link to view PDF:")

        # pdf_bytes = pdf_file.read()
        pdf_base64 = base64.b64encode(pdf_bytes).decode('utf-8')
        # st.write(f"""
        # <iframe src="data:application/pdf;base64,{pdf_bytes.decode()}" width="700" height="500" type="application/pdf"></iframe>
        # """, unsafe_allow_html=True)
        pdf_display = f"""
        <iframe src="data:application/pdf;base64,{pdf_base64}" width="700" height="900" type="application/pdf"></iframe>
        """
        st.markdown(pdf_display, unsafe_allow_html=True)

    # Remove the temporary files (optional)
    os.remove(temp_path)
    os.remove(pdf_path)
