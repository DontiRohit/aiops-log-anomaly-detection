from elasticsearch import Elasticsearch

client = Elasticsearch(
    "http://localhost:9200"
)

INDEX = "application-logs"


def get_logs(size=50):
    query = {
        "size": size,
        "query": {
            "match_all": {}
        }
    }

    response = client.search(
        index=INDEX,
        body=query
    )

    logs = []

    for hit in response["hits"]["hits"]:
        logs.append(hit["_source"]["log"])

    return logs