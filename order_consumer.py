# filepath: /home/mobcoder/Desktop/kafka-python-learning/order_consumer.py
from kafka import KafkaConsumer, KafkaProducer
import json

# Create a Kafka consumer
consumer = KafkaConsumer(
    'pizza_orders',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))  # Proper deserialization
)

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

print("🚴‍♂️ Delivery Riders Waiting for Orders...")

# Process messages from the Kafka topic
for message in consumer:
    order = message.value  # Each message contains a single order (dictionary)
    print(f"📦 Rider picked up order: {order}")
    
    # Ensure `order` is a dictionary
    if isinstance(order, dict):
        # Simulate order processing
        order['status'] = 'Delivered'
        
        # Send the updated order to the Kafka topic
        producer.send('order_updates', value=order)
        producer.flush()

        print(f"✅ Order Delivered: {order}")
    else:
        print(f"❌ Unexpected message format: {order}")