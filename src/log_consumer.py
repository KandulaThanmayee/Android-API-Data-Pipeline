from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'api_violation_logs',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

with open('violations_processed.txt', 'a') as f:
    for message in consumer:
        log = message.value
        print(f"Consumed: {log}")
        if log['violation'] != 'None':
            f.write(json.dumps(log) + '\n')
