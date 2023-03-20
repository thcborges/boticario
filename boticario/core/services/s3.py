from io import BytesIO

import boto3
from decouple import config
from pandas import DataFrame

from boticario.logger import get_logging

logging = get_logging(__name__)


class S3:
    __s3 = boto3.resource('s3')
    __client = __s3.meta.client
    __buckets = {'load': config('S3_BUCKET_LOAD')}

    def __init__(self, bucket: str):
        self.bucket = bucket
        self.__bucket = self.__buckets.get(bucket)

    def upload_data_frame(self, data_frame: DataFrame, s3_key: str):
        logging.info(
            'Uploading data frame to %s on %s bucket', s3_key, self.bucket
        )
        buffer = BytesIO()
        data_frame.to_parquet(buffer, index=False)
        self.__client.put_object(
            Bucket=self.__bucket, Key=s3_key, Body=buffer.getvalue()
        )
        return f's3://{self.__bucket}/{s3_key}'
