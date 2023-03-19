COPY {table}
    FROM '{s3_path}'
    IAM_ROLE '{iam_role}'
    FORMAT PARQUET;