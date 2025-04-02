from kafka.admin import KafkaAdminClient, NewTopic



admin_client = KafkaAdminClient(
    bootstrap_servers='localhost:9092',
)


topics = ["pizza_orders","order_updates"]

new_topics = [NewTopic(name=topic, num_partitions=3, replication_factor=1) for topic in topics]


try:
    admin_client.create_topics(new_topics)
    print(f"✅ Topics {topics} created successfully!")
except Exception as e:
    print(f"❌ Failed to create topics: {e}")
    
    
admin_client.close()
# The above code creates two Kafka topics: "pizza_orders" and "order_updates".
# Each topic has 3 partitions and a replication factor of 1.
# The replication factor indicates how many copies of the data will be stored across the Kafka cluster.
# The code uses the kafka-python library to create the topics.
# It first creates an admin client to connect to the Kafka cluster.
# Then, it defines the topics to be created and their configurations.
# Finally, it attempts to create the topics and prints a success or failure message.
# The code also closes the admin client after creating the topics.
# Note: The code assumes that a Kafka broker is running locally on port 9092.