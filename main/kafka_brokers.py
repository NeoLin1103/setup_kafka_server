# from kafka.cluster import ClusterMetadata

# metadata = ClusterMetadata(bootstrap_servers="localhost:666")

# print(f'Number of brockers: {len(metadata.brokers())}')

# for broker_metadata in metadata.brokers():
#     print()
#     print(broker_metadata)

from kafka import KafkaClient

kafka_client = KafkaClient(bootstrap_servers='localhost:59092')

clusterMetadata = kafka_client.cluster

print(clusterMetadata.brokers())