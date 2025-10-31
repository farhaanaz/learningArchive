data "aws_ami" "amiID" {
  most_recent = true
  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"]
  }
  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
  owners = ["099720109477"] # Canonical
}

output "ami_id" {
  description = "The ID of the selected AMI"
  value       = data.aws_ami.amiID.id
}