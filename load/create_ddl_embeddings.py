from langchain.document_loaders import TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
import os
 
md_folder_path = "load/Metadata"
included_extensions = ['md']
# Load multiple files
text_loaders = [TextLoader(os.path.join(md_folder_path, fn)) for fn in os.listdir(md_folder_path) if any(fn.endswith(ext) for ext in included_extensions)]
all_mds = []
 
for loader in text_loaders:
    raw_md = loader.load()
 
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=20,
    )
    texts = text_splitter.split_documents(raw_md)
    all_mds.extend(texts)
 

embeddings = OpenAIEmbeddings(openai_api_key = "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")
docsearch = FAISS.from_documents(all_mds, embeddings)
 
docsearch.save_local("faiss_index")
