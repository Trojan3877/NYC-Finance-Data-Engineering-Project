provider "aws" {
  region = "us-east-1"
  alias  = "primary"
}

provider "aws" {
  region = "us-west-2"
  alias  = "secondary"
}

resource "aws_s3_bucket" "primary_bucket" {
  provider = aws.primary
  bucket   = "nyc-finance-primary"
}

resource "aws_s3_bucket" "secondary_bucket" {
  provider = aws.secondary
  bucket   = "nyc-finance-secondary"
}
