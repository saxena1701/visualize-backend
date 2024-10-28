provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "docker_builder" {
  ami                    = "ami-0c55b159cbfafe1f0"  
  instance_type          = "t2.micro"
  key_name               = "deploy-server-keys"         
  user_data              = file("${path.module}/ec2_docker_setup.sh")
  lifecycle {
    create_before_destroy = true
  }
}
