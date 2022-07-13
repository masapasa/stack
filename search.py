from jina import Client
from docarray import Document
from config import HOST
def search_by_text(input, server=HOST):
    client = Client(host=server)
    response = client.search(
        Document(text=input),
        # parameters={"limit": limit},
        return_results=True,
    )
    matches = response[0].matches
    for match in matches:
        print(match.text)
        print(match.tags["answer"])
        print(match.tags["source"])
        print(match.tags["url"])
        print("\n")
search_by_text("What is the COVID-19 pandemic?")
#%%
import pandas as pd
df = pd.read_csv('/home/aswin/data/goodread/GoodReads_100k_books.csv')
df.head()
# %%
df.desc[0]
# %%
