from docarray import Document, DocumentArray
from jina import Flow

search_term = "How do I create a matrix?"
query = Document(text=search_term)

with flow:
  results = flow.search(query)
matches = results[0].matches

for match in matches:
  print(match.text)
answers = DocumentArray.from_csv("/home/aswin/Documents/workshops/stack_overflow/stack_overflow_a.csv")
answers.summary()

for match in matches:
  print(match.text)
  match_answers = answers.find({"tags__ParentId": {"$eq": match.tags["Id"]}})
  for answer in match_answers:
    print("---")
    print(answer.text)
  print("-----------")