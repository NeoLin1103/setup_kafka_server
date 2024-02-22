from kafka.admin import KafkaAdminClient, NewTopic

admin_client = KafkaAdminClient(
    bootstrap_servers="localhost:9092", 
    client_id='test'
)

print(admin_client.list_topics())

# topic_list = []
# topic_list.append(NewTopic(name="example_topic", num_partitions=1, replication_factor=1))
# admin_client.create_topics(new_topics=topic_list, validate_only=False)

# print('New topic created: example_topic')

admin_client.delete_topics(topics=['example_topic'])

print('Topic deleted: example_topic')

print(admin_client.list_topics())
