variable "aws_region" {
  description = "The AWS region to deploy resources in."
  type        = string
  default     = "us-east-1"
}

variable "ssh_key_name" {
  description = "The name of the SSH key pair to use for the EC2 instance."
  type        = string
  default     = "n8n-key" # Make sure this matches your key name in AWS
}