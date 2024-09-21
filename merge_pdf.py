import streamlit as st
from PyPDF2 import PdfMerger
from io import BytesIO

def merge_pdfs(pdf_files):
    pdf_merger = PdfMerger()
    for pdf in pdf_files:
        pdf_merger.append(pdf)

    merged_pdf_io = BytesIO()
    pdf_merger.write(merged_pdf_io)  
    pdf_merger.close()
    
    merged_pdf_io.seek(0)
    
    return merged_pdf_io

def main():
    st.title("PDF Merger")

    uploaded_files = st.file_uploader("Upload PDF files", type="pdf", accept_multiple_files=True)

    if uploaded_files:
        st.write(f"{len(uploaded_files)} files uploaded:")
        for file in uploaded_files:
            st.write(file.name)

        if st.button("Merge PDFs"):
            merged_pdf = merge_pdfs(uploaded_files)

            st.success("PDFs merged successfully!")
            st.download_button("Download Merged PDF", merged_pdf, "merged_output.pdf", "application/pdf")
    else:
        st.write("Please upload PDF files to merge.")

if __name__ == '__main__':
    main()
