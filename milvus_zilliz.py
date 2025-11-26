from pymilvus import MilvusClient

ZILLIZ_ENDPOINT = "https://in03-dfdb10f59f3b98f.serverless.aws-eu-central-1.cloud.zilliz.com"
ZILLIZ_API_KEY = "56fb200615a33caae920295319b84d4beff585e3a4f6cdce91c30e12119d06791b0c136a4e18cb3973316cf20128b194ae4e08a9"

COLLECTION_NAME = "company_policy"

client = MilvusClient(uri=ZILLIZ_ENDPOINT, token=ZILLIZ_API_KEY)

def setup_collection():
    collections = client.list_collections()

    if COLLECTION_NAME not in collections:
        print("🆕 Creating new collection in Zilliz Cloud...")

        client.create_collection(
            collection_name=COLLECTION_NAME,
            dimension=384,
            metric_type="L2",
            auto_id=True,           # 💥 IMPORTANT FIX
            primary_field="id",     # 💥 IMPORTANT FIX
        )

        print("✅ Collection created:", COLLECTION_NAME)
    else:
        print("ℹ️ Collection already exists:", COLLECTION_NAME)

    return client
