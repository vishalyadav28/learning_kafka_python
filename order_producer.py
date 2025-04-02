from kafka import KafkaProducer
import json
import time

# Create a Kafka producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Sample pizza order data
orders = [
    {
    "order_id": 11,
    "customer_id": 111,
    "customer_name": "Alice",
    "pizza": "Margherita",
    "quantity": 1,
    "status": "Order Placed"
},
{
    "order_id": 12,
    "customer_id": 112,
    "customer_name": "Bob",
    "pizza": "Pepperoni",
    "quantity": 3,
    "status": "Order Placed"
},
{
    "order_id": 13,
    "customer_id": 113,
    "customer_name": "Charlie",
    "pizza": "BBQ Chicken",
    "quantity": 2,
    "status": "Order Placed"
},
{
    "order_id": 14,
    "customer_id": 114,
    "customer_name": "Diana",
    "pizza": "Veggie",
    "quantity": 1,
    "status": "Order Placed"
},
{
    "order_id": 15,
    "customer_id": 115,
    "customer_name": "Eve",
    "pizza": "Hawaiian",
    "quantity": 4,
    "status": "Order Placed"
}
]

def send_order_updates(order):
    producer.send('pizza_orders', value=order)  # Send individual order
    print(f"Order update sent: {order}")
    producer.flush()

# Simulate sending order updates
for order in orders:  # Iterate over each order
    send_order_updates(order)  # Send each order individually
    time.sleep(5)  # Sleep for a while before sending the next order

producer.close()
# The above code creates a Kafka producer that sends pizza order updates to the "pizza_orders" topic.
# The producer connects to a Kafka broker running on localhost:9092.
# It serializes the order data as JSON before sending it to the topic.
# The code defines a list of sample pizza orders and a function to send order updates.
# The function sends the updated order data to the Kafka topic and prints a confirmation message.
# The code then enters an infinite loop, sending order updates every 5 seconds.
# Finally, it closes the producer when done.
# Note: The code assumes that the Kafka topic "pizza_orders" has already been created.