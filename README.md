# lambda-get-categories

AWS Lambda function that returns available content categories for the AI Site Generator platform.

## API Endpoint

**GET** `/categories`

Returns list of available content categories.

### Response Example

```json
{
  "categories": [
    {
      "id": "facts",
      "name": "Facts",
      "description": "Interesting statistics and factual information"
    },
    {
      "id": "history",
      "name": "History",
      "description": "Historical background and evolution"
    }
  ]
}
```

## Structure

```
.
├── src/
│   ├── handler.py      # Lambda handler function
│   ├── config.py       # Category configurations
│   └── utils.py        # Helper functions (CORS, response formatting)
├── tests/              # Unit tests (if any)
├── .circleci/
│   └── config.yml      # CI/CD pipeline
├── requirements.txt    # Python dependencies
└── README.md
```

## Local Development

```bash
# Install dependencies (none required for this lambda)
pip install -r requirements.txt

# Run tests
pytest tests/ -v
```

## Deployment

### Automatic (via CircleCI)

Commits to `main` or `master` trigger:
1. **Lint & Test** - Code quality checks
2. **Build** - Creates deployment package
3. **Deploy** - Uploads to S3 and updates Lambda function

### Environment Variables (set in CircleCI)

- `AWS_ROLE_ARN` - IAM role for AWS CLI
- `AWS_REGION` - AWS region (e.g., us-east-1)
- `LAMBDA_ARTIFACTS_BUCKET` - S3 bucket for deployment artifacts
- `PROJECT_NAME` - Project name prefix
- `ENVIRONMENT` - Environment name (prod, staging)

## Configuration

Categories are defined in `src/config.py`:

```python
CATEGORY_CONFIG = {
    "facts": {
        "name": "Facts",
        "description": "Interesting statistics and factual information",
        "prompt_template": "..."
    },
    # ... more categories
}
```

To add a new category, simply add it to the `CATEGORY_CONFIG` dictionary.
