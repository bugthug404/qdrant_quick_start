
import requests
from flask import request, jsonify
from qdrant_client import models, QdrantClient
from sentence_transformers import SentenceTransformer
from .data import documents

encoder = SentenceTransformer("all-MiniLM-L6-v2")

def add_books():
    try:
        print("addBooks ==== got the request", documents)

        client = QdrantClient("localhost", port=6333);

        client.recreate_collection(
          collection_name="my_books",
          vectors_config=models.VectorParams(
              size=encoder.get_sentence_embedding_dimension(),  # Vector size is defined by used model
              distance=models.Distance.COSINE,
          ),
        )

        uploaded =  client.upload_records(
                      collection_name="my_books",
                      records=[
                          models.Record(
                              id=idx, vector=encoder.encode(doc["description"]).tolist(), payload=doc
                          )
                          for idx, doc in enumerate(documents)
                      ],
                    )

        print("addBooks ==== uploaded the records", uploaded)

        return jsonify(data=str(uploaded)), 200
    except Exception as error:
        print("addbook error === ", error)
        return jsonify(error=str(error)), 500
      

def search_books():
    try:
        print("searchBooks ==== got the request", request.args)
        print("query == ", request.args.get("query"))

        client = QdrantClient("localhost", port=6333);

        search_result = client.search(
            collection_name="my_books",
            query_vector=encoder.encode(request.args.get("query")).tolist(),
            limit=3,
        )

        print("searchBooks ==== got the result", search_result)
        # convert search_result to json
        
        
        return jsonify(data=str(search_result)), 200
    except Exception as error:
        print("searchBooks error === ", error)
        return jsonify(error=str(error)), 500