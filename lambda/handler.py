import json
import boto3
import os

secrets_client = boto3.client('secretsmanager')

def get_secret(secret_name):
    response = secrets_client.get_secret_value(SecretId=secret_name)
    return json.loads(response['SecretString'])

def invoke_bedrock(prompt):
    # Placeholder for Amazon Bedrock logic
    # In reality, use boto3 client for bedrock-runtime
    return {
        "model": "bedrock",
        "response": f"Bedrock response to '{prompt}'"
    }

def invoke_azure(prompt, api_key):
    # Placeholder for Azure OpenAI call
    return {
        "model": "azure",
        "response": f"Azure response to '{prompt}' with API key {api_key[:5]}..."
    }

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        prompt = body.get("prompt")
        target_model = body.get("target_model")

        if not prompt or not target_model:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "prompt and target_model required"})
            }

        if target_model == "bedrock":
            response = invoke_bedrock(prompt)
        elif target_model == "azure":
            secret = get_secret(os.environ['AZURE_SECRET_NAME'])
            response = invoke_azure(prompt, secret['api_key'])
        else:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Unsupported model"})
            }

        return {
            "statusCode": 200,
            "body": json.dumps(response)
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
