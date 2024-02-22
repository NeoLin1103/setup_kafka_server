from kafka import KafkaConsumer

consumer = KafkaConsumer('my_topic', bootstrap_servers='localhost:9092')

print("Gonna start listening")
while True:
    for message in consumer:
        print("Here is a message..")
        print (message)