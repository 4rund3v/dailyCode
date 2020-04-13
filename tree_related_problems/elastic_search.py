from elasticsearch import ElasticSearch

client = ElasticSearch('localhost:9200')

mappings = {
        "mappings": {
                "story_versions":  {
                            "properties": {
                                "story_id": {
                                    "type": "string",
                                    "index": "not_analyzed"
                                 },
                                "story_title": {
                                    "type": "string"
                                },
                                "description": {
                                    "type": "string"
                                    
                                }
    }
    }
    }
}

client.indices.create(index="stories", body=mappings)