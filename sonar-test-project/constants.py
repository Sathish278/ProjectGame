import os

# Read secrets from environment for safer defaults in CI
# Do not include a default token in source; read from environment only
API_TOKEN = os.getenv('API_TOKEN')
# DB_SECRET read from environment to avoid embedding secrets in source
DB_SECRET = os.getenv('DB_SECRET', None)
SERVICE_URL = os.getenv('SERVICE_URL', 'http://internal.service.local')

