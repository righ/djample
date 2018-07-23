from .env import *  # NOQA

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_ACCESS_KEY_ID = os.environ['DJANGO_AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['DJANGO_AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = os.environ['DJANGO_AWS_STORAGE_BUCKET_NAME']
