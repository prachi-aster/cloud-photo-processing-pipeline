def lambda_handler(event, context):
    print("New file uploaded to S3!")
    print("Event:", event)

    return {
        "statusCode": 200,
        "body": "Lambda executed successfully!"
    }

