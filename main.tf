variable "vpc_id" {
  description = "VPC ID for the resources"
  type        = string
}

provider "aws" {
  region = "us-east-1"  # Change this to your desired region
}

# Create a security group with separate ingress rules
resource "aws_security_group" "main_sg" {
  name        = "main_security_group"
  description = "Security group for EC2 instance"
  vpc_id      = var.vpc_id  # Replace with your VPC ID
}

# Ingress rule allowing traffic from a CIDR block
resource "aws_security_group_rule" "allow_http_from_cidr" {
  type              = "ingress"
  from_port         = 80
  to_port           = 80
  protocol          = "tcp"
  security_group_id = aws_security_group.main_sg.id
  cidr_blocks       = ["0.0.0.0/0"]  # Allows traffic from any IPv4 address (adjust as needed)
}

# Define the EC2 instance
resource "aws_instance" "web_server" {
  ami           = "ami-0c55b159cbfafe1f0"  # Amazon Linux 2 AMI (replace as needed)
  instance_type = "t2.micro"
  key_name      = "deploy-server-keys"     # Replace with your key pair name

  # Attach the security group to the instance
  vpc_security_group_ids = [aws_security_group.main_sg.id]

  # Use user data to run commands on instance start-up
  user_data = file("ec2_docker_setup.sh")

  tags = {
    Name = "Terraform-EC2"
  }
}

output "instance_public_ip" {
  value = aws_instance.web_server.public_ip
  description = "The public IP of the web server instance"
  region = "us-east-1"
}
