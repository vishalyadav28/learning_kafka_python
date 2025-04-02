# Kafka Python Learning

This project demonstrates the use of Kafka with Python for producing and consuming messages. It includes a producer that sends pizza orders to a Kafka topic and a consumer that processes these orders and updates their status.

## Prerequisites

1. **Kafka**: Apache Kafka 3.x or higher
2. **Python**: Python 3.6 or higher
3. **kafka-python**: Python client for Apache Kafka

## Project Structure

- `order_producer.py`: Sends pizza orders to the Kafka topic `pizza_orders`
- `order_consumer.py`: Consumes orders from `pizza_orders` topic and sends updates to `order_updates` topic

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd kafka-python-learning
```

2. Set up Python virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
pip install kafka-python
```

## Kafka Setup (KRaft mode)

1. Generate a Cluster ID:

```bash
bin/kafka-storage.sh random-uuid
```

2. Format the storage with your Cluster ID:

```bash
bin/kafka-storage.sh format -t <your-cluster-id> -c config/kraft/server.properties
```

3. Configure KRaft mode:
   - Open `config/kraft/server.properties`
   - Add or update the following line:

```properties
controller.quorum.voters=1@localhost:9093
```

4. Start Kafka server:

```bash
# Start in foreground
bin/kafka-server-start.sh config/kraft/server.properties

# Or start as background service
nohup bin/kafka-server-start.sh config/kraft/server.properties > kafka.log 2>&1 &
```

5. Monitor Kafka logs (optional):

```bash
tail -f kafka.log
```

## Usage

Run

```python
python3 order_producer.py
python3 order_consumer.py
```
