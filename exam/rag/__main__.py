from exam.rag import *
import sys


vector_store = sqlite_vector_store()


if any(arg == "--fill" for arg in sys.argv):
    print(f"# vector store created at {FILE_DB}")

    for slide in all_slides():
        vector_store.add_texts(
            texts=[slide.content],
            metadatas=[{"source": slide.source, "lines": slide.lines, "index": slide.index}],
        )
        print(f"# added {slide.lines_count} lines of text from {slide.source} (slide {slide.index}, lines {'%d-%s' % slide.lines}) to vector store")
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
