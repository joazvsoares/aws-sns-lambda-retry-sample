import json
import random
from datetime import datetime


def handler(event, context):
    # The event contains the SNS message
    message = event["Records"][0]["Sns"]["Message"]

    # Deserializing the SNS message
    message_data = json.loads(message)

    # Extracting the messageId from the parsed message
    message_id = message_data.get("messageId")

    # Your processing logic here
    print(f"Timestamp for MessageId '{message_id}': {datetime.utcnow().isoformat()}")

    # Randomly decide to throw an error
    if random.randint(0, 1) == 1:  # This gives a 50% chance to raise an error
        raise Exception("Random error for testing retry!")

    # Your processing logic here
    print(f"Successfull run for message with ID: {message_id}")
