echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin

# Build Docker image
docker build -t "$DOCKER_USERNAME/$DOCKER_IMAGE_NAME:latest" .

# Push to Docker Hub
docker push "$DOCKER_USERNAME/$DOCKER_IMAGE_NAME:latest"