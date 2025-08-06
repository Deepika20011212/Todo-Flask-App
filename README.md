# 📝 Todo-Flask-App

A simple **Flask-based To-Do list application** with full DevOps integration.  
It uses **Docker, Terraform, GitHub Actions**, and **AWS EC2 + ECR** to demonstrate a real-world CI/CD pipeline with secure cloud deployment.

---

## 🚀 Features

- 📋 Basic To-Do app with CRUD functionality
- 🐳 Dockerized for easy containerization
- 🤖 CI/CD with GitHub Actions (self-hosted runner on EC2)
- 🔐 Static and image security scanning via SonarQube and Trivy
- 📦 Docker image pushed to Amazon ECR
- 🔁 App auto-deployed to EC2 via Docker

---

## 🛠️ Technologies Used

- **Flask** (Python)
- **Docker**
- **GitHub Actions** (self-hosted runner on EC2)
- **Terraform** (for AWS infrastructure)
- **AWS** (EC2, ECR, VPC, S3)
- **SonarQube** (code quality)
- **Trivy** (image scanning)

---

## 📁 Project Structure

.
├── app.py # Flask app
├── Dockerfile # Container build file
├── requirements.txt # Python dependencies
├── templates/ # HTML templates
├── terraform/ # Terraform IaC files
└── .github/workflows/
└── cicd.yaml # GitHub Actions pipeline


---

## 🔧 Setup Instructions

### 1. 🛠️ Provision Infrastructure via Terraform

Ensure you have:

- Terraform installed
- Valid AWS credentials configured
- SSH key pair created

Then run:

```bash
terraform init
terraform apply
This will create:

VPC, subnet, Internet Gateway

EC2 instance (with Docker and GitHub Actions runner)

ECR repository

S3 bucket for Terraform remote state

2. 🤖 Register GitHub Actions Self-hosted Runner
SSH into your EC2 instance:

bash
Copy
Edit
ssh -i <your-key>.pem ubuntu@<EC2_PUBLIC_IP>
cd /home/ubuntu/actions-runner
Then register it:

bash
Copy
Edit
./config.sh --url https://github.com/Deepika20011212/Todo-Flask-App --token <your_registration_token> --labels self-hosted,aws-runner
sudo ./svc.sh install
sudo ./svc.sh start
3. Configure Aws in EC2
# Update packages
sudo apt update

# Install required tools
sudo apt install -y unzip curl

# Download the AWS CLI v2 installer
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"

# Unzip the installer
unzip awscliv2.zip

# Run the install script
sudo ./aws/install

4. 🔐 Configure GitHub Secrets
In GitHub → Repo → Settings → Secrets → Actions, add:

Secret Name	Description
AWS_ACCESS_KEY_ID	IAM user access key
AWS_SECRET_ACCESS_KEY	IAM user secret
ECR_REGISTRY	Your ECR repo URL (e.g., 123.dkr...)
SONAR_TOKEN	SonarQube project token
SONAR_HOST_URL	SonarQube server URL (e.g., http://...)
