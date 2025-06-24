import json
import os
import boto3
import logging
import urllib3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

secrets_client = boto3.client("secretsmanager")
http = urllib3.PoolManager()

# Fetch secrets once outside the handler for better performance
SECRET_NAME = os.environ.get("SECRET_NAME", "Assessment_AWS")
GITHUB_TOKEN_KEY = os.environ.get("GITHUB_TOKEN_KEY", "token")

cached_secrets = None
def get_secret():
    global cached_secrets
    if cached_secrets is None:
        response = secrets_client.get_secret_value(SecretId=SECRET_NAME)
        cached_secrets = json.loads(response["SecretString"])
    return cached_secrets

def call_bedrock(prompt):
    # response to simulate Bedrock
    return {"response": f"Bedrock response to: {prompt}"}

def call_azure_openai(prompt):
    # Placeholder for Azure OpenAI integration
    return {"response": f"Azure OpenAI response to: {prompt}"}

def lambda_handler(event, context):
    try:
        body = json.loads(event["body"])
        prompt = body.get("prompt")
        target_model = body.get("target_model")

        if not prompt or not target_model:
            return {"statusCode": 400, "body": json.dumps({"error": "Missing prompt or target_model"})}

        if target_model == "bedrock":
            result = call_bedrock(prompt)
        elif target_model == "azure":
            result = call_azure_openai(prompt)
        else:
            return {"statusCode": 400, "body": json.dumps({"error": "Invalid target_model"})}

        return {
            "statusCode": 200,
            "body": json.dumps(result)
        }

    except Exception as e:
        logger.exception("Error handling request")
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}
