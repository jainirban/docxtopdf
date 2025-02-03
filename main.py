import streamlit as st
import os
import tempfile
from weasyprint import HTML
from docx import Document

st.title("📄 DOCX to PDF Converter")

def convert_docx_to_pdf(input_path, output_path):
    """Convert DOCX to PDF using WeasyPrint."""
    output_pdf = output_path + ".pdf"
    HTML(input_path).write_pdf(output_pdf)
    return output_pdf

def save_uploaded_file(uploaded_file):
    """Save uploaded file to a temporary location."""
    with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp_file:
        tmp_file.write(uploaded_file.getbuffer())
        return tmp_file.name

uploaded_file = st.file_uploader("📂 Upload a DOCX file", type=["docx"])

if uploaded_file:
    temp_docx_path = save_uploaded_file(uploaded_file)
    output_pdf_path = temp_docx_path.replace(".docx", "")

    try:
        # Convert DOCX to PDF
        pdf_path = convert_docx_to_pdf(temp_docx_path, output_pdf_path)

        if os.path.exists(pdf_path):
            # Display download button
            with open(pdf_path, "rb") as pdf_file:
                st.download_button(label="📥 Download PDF", data=pdf_file, file_name="converted.pdf", mime="application/pdf")

            # Display PDF in Streamlit
            st.subheader("📑 Preview PDF")
            st.pdf(pdf_path)
        else:
            st.error("❌ PDF conversion failed.")
    except Exception as e:
        st.error(f"❌ Error: {e}")
