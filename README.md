# Serverless Image Processing on AWS

## 📌 Project Overview
This project demonstrates a **serverless image processing pipeline** using AWS services.  
When a user uploads an image to an **S3 bucket**, an **AWS Lambda function** is triggered.  
The Lambda function resizes the image (or applies transformations like watermarking) and saves the processed image into another **S3 bucket**.

---

## 🏗️ Architecture
![Architecture Diagram](architecture.png)

**Workflow:**
1. User uploads an image to the **Input S3 Bucket**.
2. The upload event triggers an **AWS Lambda Function**.
3. Lambda processes the image (resize in this project).
4. Lambda stores the processed image in the **Output S3 Bucket**.

---

## 🛠️ AWS Services Used
- **Amazon S3** → Store input and output images.  
- **AWS Lambda** → Resize and process images.  
- **IAM Roles** → Secure permissions for Lambda to access S3.  
- **CloudWatch Logs** → Monitor function execution and debug errors.  
- **SNS (Optional)** → Send notifications on success/failure.

---

## 🚀 How to Deploy
1. Create two S3 buckets:
   - `input-images-bucket-YOURNAME`
   - `output-images-bucket-YOURNAME`

   **Best practices:**
   - Enable **SSE-S3 encryption**
   - Disable **public access**
   - Enable **versioning**

2. Create a new AWS Lambda function:
   - Runtime: **Python 3.9**
   - Attach IAM role with **S3 read/write permissions** and **CloudWatch Logs access**.

3. Add the provided Python code in `lambda_function.py`.

4. Configure an **S3 trigger** for the Input bucket:
   - Event type: **PUT (Object Created)**

5. Test the setup:
   - Upload an image to the Input bucket.
   - Processed image will appear in the Output bucket.

---

## 📂 Repository Structure
