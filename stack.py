
from docarray import DocumentArray
docs = DocumentArray.from_csv("/home/aswin/Documents/workshops/stack_overflow/stack_overflow_r_q.csv")
from jina import Flow

flow = Flow()
flow = flow.add(
    name="encoder",
    uses="jinahub+sandbox://SpacyTextEncoder/v0.4",
    uses_with={"model_name": "en_core_web_md"})
flow = flow.add(
    name="indexer",
    uses="jinahub://AnnLiteIndexer/0.3.0",
    uses_with={"dim": 300},  # we're using a 300 dimension model
    uses_metas={"workspace": "workspace"},  # this is where we'll store our data on disk
    install_requirements=True
)
with flow:
    docs = flow.index(docs)