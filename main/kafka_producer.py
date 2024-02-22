# -*- coding: utf-8 -*-
from kafka import KafkaProducer
from kafka.errors import KafkaError

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

# asynchronous by default
future = producer.send('my_topic', b'Hello world!')
print(future)

# block for 'synchronous' sends
try:
    record_metadata = future.get(timeout=10)
    print(record_metadata)
except KafkaError:
    # decide what to do if produce request failed...
    pass

# successful result returns assigned partition and offset
print(record_metadata.topic)
print(record_metadata.partition)
print(record_metadata.offset)