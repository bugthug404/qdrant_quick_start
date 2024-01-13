# import { Router } from "express";
# import {
#   createCollection,
#   dynamicQueryCollection,
#   queryCollection,
# } from "./qdrant.service";

# const qdrantData = Router();

# qdrantData.get("/create-collection", createCollection);
# qdrantData.get("/query-collection", queryCollection);
# qdrantData.get("/dynamic-query-collection", dynamicQueryCollection);

# export default qdrantData;
from flask import Blueprint
from .qdrant_service import create_collection, query_collection, dynamic_query_collection

qdrantData = Blueprint('qdrantData', __name__)

@qdrantData.route('/create-collection', methods=['GET'])
def create_collection_route():
    return create_collection()

@qdrantData.route('/query-collection', methods=['GET'])
def query_collection_route():
    return query_collection()

@qdrantData.route('/dynamic-query-collection', methods=['GET'])
def dynamic_query_collection_route():
    return dynamic_query_collection()