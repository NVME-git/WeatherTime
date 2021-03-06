terraform {
    required_providers {
        aws = {
        source = "hashicorp/aws"
        }
    }
}

provider "aws" {
    region = "eu-west-1"
    shared_credentials_file = "AWS_credentials"
    profile = "WeatherTime"
}
