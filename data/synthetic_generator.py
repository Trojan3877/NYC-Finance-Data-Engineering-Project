from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

def stream_finance_data():
    while True:
        message = {
            "stock_price": round(random.uniform(90, 110), 2),
            "volume": random.randint(10000, 300000)
        }
        producer.send("nyc_finance_topic", message)
        time.sleep(1)

if __name__ == "__main__":
    stream_finance_data()
