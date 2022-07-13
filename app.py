from jina import Flow
from docarray import DocumentArray

docs = DocumentArray.from_csv('/home/aswin/data/wiki/promotional.csv')
def run():
    f = Flow().add(uses='jinahub://SimpleIndexer', size=100)
    # or load from Flow YAML
    # f = Flow.load_config('flow.yml')
    with f:
        da = f.post("/", docs, size=11)
        print(da.to_json())


if __name__ == '__main__':
    run()
    # or run in terminal:
    # $ jina flow --uses flow.yml
