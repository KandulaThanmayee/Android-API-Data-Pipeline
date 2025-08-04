from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))
api_endpoints = ['telephony', 'media', 'mtp', 'hardware', 'nfc']

def generate_log():
    return {
        'timestamp': time.time(),
        'endpoint': random.choice(api_endpoints),
        'violation': random.choice(['None', 'Permission', 'RateLimit', 'MalformedRequest'])
    }

while True:
    log = generate_log()
    producer.send('api_violation_logs', log)
    print(f"Produced: {log}")
    time.sleep(1)
