import streamlit as st
import tempfile
import resume_reader as b



pdf_path = r"C:\Users\gopic\OneDrive\Documents\BDA RESUME.pdf"
vectorstore = b.load_pdf(pdf_path)


st.title("Resume Reader")

uploaded_file = st.file_uploader("Upload a PDF resume", type="pdf")
if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
        temp_file.write(uploaded_file.read())
        pdf_path = temp_file.name

    st.success("PDF uploaded successfully!")

    if st.button("Load Resume"):
        vectorstore = b.load_pdf(pdf_path)
        rag_chain = b.build_rag_chain(vectorstore)
        st.success("Resume loaded and ready for queries!")

    question = st.text_input("Ask a question about the resume:")
    if question and 'rag_chain' in locals():
        response = b.query_resume(rag_chain, question)
        st.write("Answer:", response['answer'])
        st.write("Sources:", response['sources'])

