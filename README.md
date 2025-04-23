# cicddemo
# ci-cd-python - Commands to install Docker on EC2 
- Ensure port 80 is available
```
sudo yum update -y
sudo amazon-linux-extras install docker
sudo service docker start
sudo systemctl start docker
sudo service docker status
sudo groupadd docker
sudo usermod -a -G docker ec2-user
newgrp docker
docker --version

# create ECR with name: my-flask-app
aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin 881490110646.dkr.ecr.us-east-2.amazonaws.com
```
for ubuntu

sudo apt-get update -y
sudo apt install -y docker.io
sudo service docker start
sudo systemctl start docker
sudo service docker status
sudo groupadd docker
sudo usermod -a -G docker ubuntu
newgrp docker
docker --version

sudo su

curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
sudo apt-get install unzip.

unzip awscliv2.zip
sudo ./aws/install