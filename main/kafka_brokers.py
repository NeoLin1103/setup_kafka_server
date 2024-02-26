from kafka.cluster import ClusterMetadata

metadata = ClusterMetadata(bootstrap_servers="localhost:9092")

print(f'Number of brockers: {len(metadata.brokers())}')

for broker_metadata in metadata.brokers():
    print()
    print(broker_metadata)