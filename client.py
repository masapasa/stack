from mmap import PROT_WRITE
from fastapi import Query
from jina import Flow
from docarray import Document, DocumentArray
f = Flow().load_config("flow.yml")
with f:
    r = f.search(query=Document(text="software"), return_results=True, size=10)
    print(r.to_json())