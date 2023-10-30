import boto3
import json
import uuid
import os

# Initialize the SNS client
sns = boto3.client("sns")

# The ARN for your SNS topic
TOPIC_ARN = os.environ.get("TOPIC_ARN")


def handler(event, context):
    message_id = str(uuid.uuid4())

    # Your message payload (adjust this as per your needs)
    payload = {"messageId": message_id}

    # Convert the payload to a string format (JSON in this case)
    message_body = json.dumps(payload)

    sns.publish(
        TopicArn=TOPIC_ARN,
        Message=message_body,
        Subject="Your Subject Here",  # Optional: add a subject if needed
    )
    print(f"Sent message with ID {message_id}")

    return {"statusCode": 200, "body": json.dumps("Message sent successfully!")}
