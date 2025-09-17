terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "6.13.0"
    }
  }
}

resource "aws_s3_bucket" "data_bucket" {
  bucket = var.aws_s3_bucket_name


}

resource "aws_dynamodb_table" "results" {
  name           = "ResultsTable"
  billing_mode   = "PAY_PER_REQUEST"
  hash_key       = "id"

  attribute {
    name = "id"
    type = "S"
  }
}