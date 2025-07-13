# Serverless Image Editor

A fast, secure, and scalable serverless image processing application built on AWS. Users can upload images via a modern web interface, and the system automatically resizes them using a fully managed backend.

*This project was developed by **Manar Aly Zahran** as part of the **Manara AWS Cloud Solution Architect Program**.*

[LinkedIn Profile](https://www.linkedin.com/in/manar-aly-/)
## Overview

This project demonstrates a complete serverless image processing architecture using Amazon Web Services. It features a static web frontend, secure image upload, automatic resizing, and easy access to the processed images.

The following diagram illustrates the system architecture:

<img width="1042" height="561" alt="Diagram" src="https://github.com/user-attachments/assets/cf4bfb73-00ef-4d97-836b-cb31dc3adbce" />

---

## Technology Stack

| Layer      | Services Used                                 | Purpose                                    |
| ---------- | --------------------------------------------- | ------------------------------------------ |
| Frontend   | HTML, CSS, JS, S3 Static Website Hosting      | User Interface for uploading & downloading |
| API        | Amazon API Gateway + Lambda                   | Generate pre-signed S3 URLs                |
| Processing | AWS Lambda (S3 Event Trigger)                 | Resize images on upload                    |
| Storage    | Amazon S3 (original-images, processed-images) | Secure image storage                       |
| Security   | IAM, CORS, S3 Bucket Policies                 | Least-privilege access and public read     |

---

## Workflow

1. User selects an image to upload from the static frontend.
2. Frontend calls an API Gateway endpoint (`GET /upload`) to retrieve a pre-signed S3 upload URL.
3. The image is uploaded directly to the `original-images` S3 bucket.
4. This upload triggers the `ResizeImageLambda` function.
5. Lambda resizes the image and stores it in the `processed-images` bucket.
6. A public download link is generated and shared back on the website.

---

## Demo

You can preview the app by opening the S3 static website URL hosting the HTML frontend:

**Live URL**: [http://static-web-hosting-manar.s3-website.eu-west-2.amazonaws.com/](http://static-web-hosting-manar.s3-website.eu-west-2.amazonaws.com/)

---

## Project Structure

```
serverless-image-editor/
│   README.md
│   architecture-diagram.png
│
├───Lambda/
│   ├───GeneratePresignedURL/
│   │   └── generate_presigned_url.py   # Generates secure pre-signed URLs
│   └───ResizeImage/
│       ├── Dockerfile                  # (Optional) Container for image processing
│       └── lambda_function.py         # Resizes uploaded images
│
└───WebPage/
    ├── favicon.ico
    ├── index.html                     # Simple image upload UI
    └── logo.png                       # App branding/logo
```

---

## Security & Access Control

* **Original Bucket**:

  * Accepts uploads via pre-signed URLs only
  * Enforces content type and size restrictions
* **Processed Bucket**:

  * Public read-only (for download only)
  * CORS configured for `GET` requests
* **IAM Roles**:

  * Lambda functions have limited, scoped permissions to specific buckets

---

## Presigned Upload Flow Example

```
GET https://{api-id}.execute-api.{region}.amazonaws.com/prod/upload?filename=my-image.jpg

Response:
{
  "url": "https://your-bucket.s3.amazonaws.com/",
  "fields": {
    "key": "original/my-image.jpg",
    "Content-Type": "image/jpeg",
    "acl": "private"
  }
}
```

Frontend then uploads the file using an HTML form and these fields.

---

## Learning Outcomes

* Event-driven development using S3 + Lambda
* Using API Gateway for secure frontend/backend communication
* Designing scalable and cost-effective serverless architectures
* Applying IAM best practices and bucket policy restrictions

---

## Author

**Manar Aly Zahran**
[LinkedIn](https://www.linkedin.com/in/manar-aly-/)

This project was created as part of the **Manara AWS Cloud Solution Architect Program**, and showcases the power of AWS services to build fully managed, scalable applications with minimal infrastructure overhead.

---

## Resources

* [AWS Lambda Documentation](https://docs.aws.amazon.com/lambda/)
* [Amazon S3 Presigned URLs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/PresignedUrlUploadObject.html)
* [API Gateway REST APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-rest-api.html)

---

Upload → Resize → Download — All in a few seconds with zero servers to manage!
