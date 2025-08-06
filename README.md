# ✅ Flask Todo App — DevOps Project

A complete end-to-end DevOps project demonstrating:

- A **Flask-based Todo App**
- **Infrastructure as Code** using Terraform
- **CI/CD with GitHub Actions** (self-hosted runner on EC2)
- **Containerization** using Docker
- **Static code analysis** with SonarQube
- **Image vulnerability scanning** using Trivy
- **Secure deployment** to AWS EC2 from ECR

---

## 📸 Screenshot

![App Screenshot](screenshot.png)

> 💡 Upload a file named `screenshot.png` to the repo root to show the UI here.

---

## 🚀 Tech Stack

| Layer         | Tool/Service                           |
|---------------|----------------------------------------|
| Frontend      | HTML, Jinja2 (via Flask templates)     |
| Backend       | Flask (Python)                         |
| Container     | Docker                                 |
| IaC           | Terraform                              |
| CI/CD         | GitHub Actions (self-hosted EC2 runner)|
| Security Scan | SonarQube, Trivy                       |
| Cloud Infra   | AWS (EC2, ECR, VPC, S3)                |

---

## 🧱 Architecture Overview

```text
GitHub Repo (main branch)
     |
     | GitHub Actions (on push)
     |   ↳ SonarQube Scan
     |   ↳ Trivy Scan
     |   ↳ Build Docker Image
     |   ↳ Push to Amazon ECR
     |   ↳ Deploy to EC2 (via Docker)
     |
EC2 Runner ↔ Pulls from ECR ↔ Runs Flask App


cd /home/ubuntu/actions-runner
./config.sh --url https://github.com/Deepika20011212/Todo-Flask-App --token <your_token> --labels self-hosted
sudo ./svc.sh install
sudo ./svc.sh start

🤖 Register Self-Hosted GitHub Runner and install aws in Ec2 

cd /home/ubuntu/actions-runner
./config.sh --url https://github.com/Deepika20011212/Todo-Flask-App --token <your_token> --labels self-hosted
sudo ./svc.sh install
sudo ./svc.sh start

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


🔐 Set GitHub Secrets
Add secrets
| Name                    | Description                                                        |
| ----------------------- | ------------------------------------------------------------------ |
| `AWS_ACCESS_KEY_ID`     | IAM user's access key                                              |
| `AWS_SECRET_ACCESS_KEY` | IAM user's secret key                                              |
| `ECR_REGISTRY`          | ECR URL (`<aws_id>.dkr...`)                                        |
| `SONAR_TOKEN`           | Token from your SonarQube                                          |
| `SONAR_HOST_URL`        | SonarQube URL ([http://localhost](http://localhost) or public URL) |

