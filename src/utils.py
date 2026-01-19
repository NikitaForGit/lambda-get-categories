"""
Utility functions for Lambda function
"""
import json
from typing import Any, Dict


def create_response(status_code: int, body: Any, headers: Dict[str, str] = None) -> Dict:
    """Create a properly formatted API Gateway response."""
    default_headers = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Headers": "Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token",
        "Access-Control-Allow-Methods": "GET,POST,OPTIONS",
    }
    
    if headers:
        default_headers.update(headers)
    
    return {
        "statusCode": status_code,
        "headers": default_headers,
        "body": json.dumps(body, default=str),
    }


def get_http_method(event: Dict) -> str:
    """Get HTTP method from API Gateway event (supports both v1 and v2 formats)."""
    # v2 format
    if "requestContext" in event and "http" in event.get("requestContext", {}):
        return event["requestContext"]["http"].get("method", "GET")
    # v1 format
    return event.get("httpMethod", "GET")
