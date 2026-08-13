# CICD_PipeLine_Project

This project implements an automated CI/CD pipeline for a Python Flask application using GitHub Actions.

The pipeline automatically:

1. Checks out source code
2. Set up Python
3. Installs Python dependencies
4. Runs pytest
5. Configure Source code
6. Configure AWS Credentials
7. Login to Amazon ECR
8.Set image tag
9. Builds a Docker image
10. Push Docker image to ECR
11.Deploy to EC2
12. Sends a success or failure email

## Project Structure

cicd-Pipeline-Project/
├── app.py
├── requirements.txt
├── Dockerfile
|── test_app.py
├── .github/
│   └── workflows/
│       └── cicdpipeline.yml
└── README.md

## Prerequisites

- GitHub account
- AWS account
- Amazon ECR repository
- Amazon EC2 instance
- Docker installed on EC2
- EC2 IAM role with ECR read permission
- GitHub Actions AWS credentials
- EC2 SSH private key
- Gmail SMTP App Password

## AWS Configuration

### ECR

Create an ECR repository named: cicdpipeline

<img width="940" height="382" alt="image" src="https://github.com/user-attachments/assets/6ae3b168-ce95-47b8-89d9-6a797e20b31c" />

### EC2

The EC2 instance must have:

- Docker installed
- Docker service running
- AWS CLI installed
- IAM role attached
- ECR read permission

<img width="940" height="190" alt="image" src="https://github.com/user-attachments/assets/3b8d9a23-3530-4818-9037-f7bb95fa893b" />

<img width="940" height="265" alt="image" src="https://github.com/user-attachments/assets/55ac9e26-566b-4b7d-8c28-37156a668690" />

<img width="940" height="375" alt="image" src="https://github.com/user-attachments/assets/01839635-f521-4028-921f-91c79c36a13c" />

<img width="940" height="425" alt="image" src="https://github.com/user-attachments/assets/7be9c8cf-a8aa-4597-a490-d0862bfaa9e3" />

<img width="940" height="200" alt="image" src="https://github.com/user-attachments/assets/15299993-90ab-4372-903d-0d8e2ea63af5" />

### IAM Role

The EC2 instance role requires ECR pull permission.

<img width="940" height="294" alt="image" src="https://github.com/user-attachments/assets/5fba3eec-dd33-4583-a938-8eefc1ba0d6f" />

## GitHub Secrets

Configure the following GitHub Actions secrets:

- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- EC2_HOST
- EC2_USER
- EC2_SSH_KEY
- SMTP_SERVER
- SMTP_PORT
- SMTP_USERNAME
- SMTP_PASSWORD
- NOTIFICATION_EMAIL

## Screenshots

1. Python, Docker Configuration File snap

<img width="1242" height="461" alt="image" src="https://github.com/user-attachments/assets/6d9c21e0-11be-4ad1-832d-7074e1440741" />

2. GitHub Actions successful pipeline

<img width="940" height="457" alt="image" src="https://github.com/user-attachments/assets/17d9d9cc-0013-448a-9ce6-79c056478f19" />

<img width="1365" height="460" alt="image" src="https://github.com/user-attachments/assets/32d19e54-d9a4-4689-9f9f-47a3d1c6bab5" />

3. ECR Image Output

<img width="940" height="356" alt="image" src="https://github.com/user-attachments/assets/4a177dec-c856-4b0c-be3b-ae1ad793b29f" />

4. EC2 Output

<img width="940" height="291" alt="image" src="https://github.com/user-attachments/assets/b16d56fc-c801-4168-b06f-0dad99e260eb" />

<img width="940" height="387" alt="image" src="https://github.com/user-attachments/assets/6315e24b-1f33-4091-93e1-f82baaa4f561" />

5. Success email

<img width="940" height="531" alt="image" src="https://github.com/user-attachments/assets/d4868caf-5634-4966-a532-b2a10f9aed04" />

6. Failed test

<img width="940" height="447" alt="image" src="https://github.com/user-attachments/assets/e6a030c9-d7d6-46db-b58b-0e6227ca3589" />

7. Failure email

<img width="940" height="534" alt="image" src="https://github.com/user-attachments/assets/7624b79c-6a04-4114-a647-3f75865721cc" />


