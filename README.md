# Multi-Cloud AI Service Pipeline

## 🧩 Architecture Diagram

```
GitHub (master)
   |
   v
CodePipeline (triggered on push)
   |
   v
CloudFormation deploys:
  - Lambda (AI Handler)
  - API Gateway
  - IAM roles
  - Secrets Manager access
   |
   v
HTTP Request --> API Gateway --> Lambda --> AI Services (Bedrock / Azure)
```

## 🚀 Deploying the Stack

### Prerequisites:
- AWS CLI configured
- PAT stored in AWS Secrets Manager under secret name: `Assessment_AWS`

### Deploy Manually (optional):
```bash
aws cloudformation deploy \
  --template-file template.yaml \
  --stack-name MultiCloudAIStack \
  --capabilities CAPABILITY_NAMED_IAM \
  --parameter-overrides GitHubRepo=vncharyhub/multi-cloud-ai-service-pipeline
```

Otherwise, just push code to `master` branch — CodePipeline will do the rest.

## 🧪 Testing the API

Once deployed, find your API Gateway endpoint in the stack output. Use `curl`:

```bash
curl -X POST https://<api-id>.execute-api.<region>.amazonaws.com/invoke \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Explain AI", "target_model": "bedrock"}'
```

Response:
```json
{
  "response": "Bedrock response to: Explain AI"
}
```

## 🔐 Security
- IAM roles follow least privilege
- Lambda accesses secrets via AWS Secrets Manager
- GitHub OAuth token not hardcoded (secure resolution from Secrets Manager)

---

## 🛠️ Notes
- `call_azure_openai()` is a placeholder for future expansion
- You can extend this to support logging, monitoring, CodeBuild, etc.

---
