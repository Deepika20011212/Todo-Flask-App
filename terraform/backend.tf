terraform {
  backend "s3" {
    bucket         = "flask-app-terraform"
    key            = "flask-app/terraform.tfstate"
    region         = "ap-south-1"
  }
}