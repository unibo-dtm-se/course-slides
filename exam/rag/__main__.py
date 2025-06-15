from exam.rag import *
import sys


vector_store = sqlite_vector_store()


if any(arg == "--fill" for arg in sys.argv):
    loader = DoclingLoader(
        file_path=MARKDOWN_FILES,
        export_type=ExportType.DOC_CHUNKS,
        # chunker=SlideChunker(),
    )
    
    print(f"# vector store created at {FILE_DB}")

    for doc in loader.lazy_load():
        if not isinstance(source := doc.metadata['source'], str):
            doc.metadata['source'] = source = str(source)
        vector_store.add_documents([doc])
        print(f"# added {doc.page_content.count("\n") + 1} lines from {source} to vector store")
    print("# vector store filled successfully")
else:
    print(f"# vector store loaded successfully: it contains {vector_store.get_dimensionality()} embeddings.")
    while True:
        try:
            query = input("Enter your query (or 'exit' to quit):\n\t")
            if query.strip().lower() == 'exit':
                break
            results = vector_store.similarity_search(query)
            for doc in results:
                print(f"\t- from document: {doc.metadata['source']}")
                print("\t\t" + doc.page_content.replace("\n", "\n\t\t"))
                print("\t\t---")
        except (EOFError, KeyboardInterrupt):
            break
print("# goodbye")
