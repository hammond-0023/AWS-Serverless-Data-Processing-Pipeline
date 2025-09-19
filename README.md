**Project Description**

A serverless data processing pipeline built with AWS services, demonstrating expertise in cloud architecture, infrastructure as code, and automated data processing workflows. This project showcases a scalable solution for processing files uploaded to S3, with automated Lambda function triggers and DynamoDB storage for processed results.

**Architecture**

<img width="1365" height="507" alt="image" src="https://github.com/user-attachments/assets/ea7aa50d-b6cf-4ea1-b9fe-502c5d096e56" />


**1. S3 Bucket**

Stores raw data files whenever an object is uploaded into the bucket, it riggers Lambda function on file upload
Configured with proper IAM permissions

**2.Lambda Function**

Processes files automatically
Stores results in DynamoDB
Includes comprehensive error handling

**3.DynamoDB Table**

Stores processed results

Uses pay-per-request billing model

Configured with appropriate IAM permissions

**4.IAM Configuration**

Role-based access control

Least privilege principle implementation

Secure resource access policies
