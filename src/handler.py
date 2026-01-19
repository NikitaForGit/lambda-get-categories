"""
Lambda function: Get Categories
Returns available content categories.
"""
from config import CATEGORY_CONFIG
from utils import create_response, get_http_method


def handler(event, context):
    """
    Lambda handler for getting categories.
    
    GET /categories
    Returns list of available content categories
    """
    # Handle OPTIONS for CORS
    if get_http_method(event) == 'OPTIONS':
        return create_response(200, {})
    
    categories = [
        {
            'id': cat_id,
            'name': config['name'],
            'description': config['description'],
        }
        for cat_id, config in CATEGORY_CONFIG.items()
    ]
    
    return create_response(200, {'categories': categories})
