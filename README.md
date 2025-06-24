# Multi-Cloud AI Service Pipeline

## Components

- **Lambda**: Invokes Bedrock or Azure model.
- **API Gateway**: Public HTTP endpoint.
- **Secrets Manager**: Stores API keys.
- **CodePipeline**: CI/CD.
- **CloudFormation**: IaC.

## Deployment Instructions

1. Create the secret in AWS Secrets Manager for GitHub PAT.
2. Deploy using AWS CLI:

```bash
aws cloudformation deploy \
  --template-file template.yaml \
  --stack-name MultiCloudAI \
  --capabilities CAPABILITY_NAMED_IAM \
  --parameter-overrides \
    GitHubRepo=user/repo \
    GitHubBranch=master \
    GitHubToken=ghp_xxxPATxxx
