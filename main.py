import streamlit as st
import os
import tempfile
import pdfkit

st.title("DOCX to PDF Converter")

def convert_docx_to_pdf(input_path, output_path):
    """Convert DOCX to PDF using pdfkit."""
    output_pdf = output_path + ".pdf"
    pdfkit.from_file(input_path, output_pdf)
    return output_pdf

uploaded_file = st.file_uploader("Upload a DOCX file", type=["docx"])

if uploaded_file is not None:
    with tempfile.TemporaryDirectory() as tmpdirname:
        input_path = os.path.join(tmpdirname, uploaded_file.name)
        output_path = os.path.join(tmpdirname, "converted")

        # Save uploaded file
        with open(input_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Convert DOCX to PDF
        try:
            pdf_path = convert_docx_to_pdf(input_path, output_path)

            if os.path.exists(pdf_path):
                # Display download button
                with open(pdf_path, "rb") as pdf_file:
                    st.download_button(label="Download PDF", data=pdf_file, file_name="converted.pdf", mime="application/pdf")

                # Display PDF in Streamlit
                st.subheader("Preview PDF")
                st.pdf(pdf_path)
            else:
                st.error("PDF conversion failed.")
        except Exception as e:
            st.error(f"Error: {e}")
