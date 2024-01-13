

import requests
from flask import request, jsonify
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams
from qdrant_client.http.models import PointStruct
from qdrant_client.http.models import Filter, FieldCondition, MatchValue


def create_collection():
    try:
        client = QdrantClient("localhost", port=6333)

        if "test_collection" not in client.get_collections():
            client.create_collection(
                collection_name="test_collection",
                vectors_config=VectorParams(size=4, distance=Distance.DOT),
            )

        print("collection created or already exists")

        operation_info = client.upsert(
            collection_name="test_collection",
            wait=True,
            points=[
                PointStruct(id=1, vector=[0.05, 0.61, 0.76, 0.74], payload={"city": "Berlin"}),
                PointStruct(id=2, vector=[0.19, 0.81, 0.75, 0.11], payload={"city": "London"}),
                PointStruct(id=3, vector=[0.36, 0.55, 0.47, 0.94], payload={"city": "Moscow"}),
                PointStruct(id=4, vector=[0.18, 0.01, 0.85, 0.80], payload={"city": "New York"}),
                PointStruct(id=5, vector=[0.24, 0.18, 0.22, 0.44], payload={"city": "Beijing"}),
                PointStruct(id=6, vector=[0.35, 0.08, 0.11, 0.44], payload={"city": "Mumbai"}),
            ],
        )

        print('operation_info ===== ',operation_info)
        
        

       

        return jsonify(data="createCollection"), 200
    except requests.HTTPError as error:
        return jsonify(error=str(error)), 500

def query_collection():
    try:
        client = QdrantClient("localhost", port=6333)

        search_result = client.search(
            collection_name="test_collection", query_vector=[0.2, 0.1, 0.9, 0.7], limit=3
        )

        print('search_result ===== ',search_result)

        return jsonify(data=str(search_result)), 200
    except requests.HTTPError as error:
        return jsonify(error=str(error)), 500

def dynamic_query_collection():
    try:
        client =  QdrantClient("localhost", port=6333)

        search_result = client.search(
            collection_name="test_collection",
            query_vector=[0.2, 0.1, 0.9, 0.7],
            query_filter=Filter(
                must=[FieldCondition(key="city", match=MatchValue(value="London"))]
            ),
            with_payload=True,
            limit=3,
        )

        print('search_result  =====  ',search_result)

        return jsonify(data=str(search_result)), 200
    except requests.HTTPError as error:
        return jsonify(error=str(error)), 500
