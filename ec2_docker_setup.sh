sudo yum update -y
sudo amazon-linux-extras install docker -y
sudo service docker start
sudo usermod -a -G docker ec2-user

# Clone your repository
git clone <your-repository-url> /home/ec2-user/app
cd /home/ec2-user/app

# Run Docker build and push
export DOCKER_USERNAME="process.env.DOCKER_USERNAME"
export DOCKER_PASSWORD="process.env.DOCKER_PASSWORD"
export DOCKER_IMAGE_NAME="visualize-backend"

chmod +x build_and_push.sh
./build_and_push.sh