import redis
import os
import threading

r = redis.Redis(host=os.environ.get("REDIS_HOST", "redis"), port=6379, decode_responses=True)

def handle_messages():
    pubsub = r.pubsub()
    pubsub.subscribe("notifications")

    print("📡 Subscribed to 'notifications' channel.")
    for message in pubsub.listen():
        if message['type'] == 'message':
            print(f"🔔 Notification received: {message['data']}")

if __name__ == '__main__':
    thread = threading.Thread(target=handle_messages)
    thread.start()

    print("✅ Flask Notification Service is running. Listening for Redis messages...")
