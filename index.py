from jina import Flow
from docarray import Document, DocumentArray
input = DocumentArray.from_csv("/home/aswin/data/wiki/temp00.csv")
f = Flow().load_config("flow.yml")

with f:
    r = f.post('/index', size=11)
# #%%
# from docarray import Document, DocumentArray
# input = DocumentArray.from_csv("/home/aswin/Documents/example-knowledge-base-stackoverflow/data/small/Answers.csv")
# input[0].text
# # %%
