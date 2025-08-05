output "ec2_public_ip" {
  value = aws_instance.flask.public_ip
}

output "ecr_repository_url" {
  value = aws_ecr_repository.flask_repo.repository_url
}

output "s3_bucket_name" {
  value = aws_s3_bucket.tf_state.id
}

output "vpc_id" {
  value = aws_vpc.main.id
}
