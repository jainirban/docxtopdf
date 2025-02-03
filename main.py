import streamlit as st
import tempfile
import os
import pypandoc
pypandoc.download_pandoc()

def convert_docx_to_pdf(input_path, output_path):
    """Convert DOCX to PDF using Pandoc."""
    output_pdf = output_path + ".pdf"
    pypandoc.convert_file(input_path, 'pdf', outputfile=output_pdf)
    return output_pdf

st.title("DOCX to PDF Converter")

uploaded_file = st.file_uploader("Upload a DOCX file", type=["docx"])

if uploaded_file is not None:
    with tempfile.TemporaryDirectory() as tmpdirname:
        input_path = os.path.join(tmpdirname, uploaded_file.name)

        # Save uploaded file
        with open(input_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Convert DOCX to PDF
        pdf_path = convert_docx_to_pdf(input_path, os.path.join(tmpdirname, "converted"))

        if os.path.exists(pdf_path):
            # Display the download button
            with open(pdf_path, "rb") as pdf_file:
                st.download_button(label="Download PDF", data=pdf_file, file_name="converted.pdf", mime="application/pdf")

            # Display the PDF in Streamlit
            st.subheader("Preview PDF")
            st.pdf(pdf_path)
        else:
            st.error("PDF conversion failed.")
