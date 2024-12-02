# Vertex AI Training Service

## Overview

This project demonstrates how to train machine learning models at scale using Google Cloud's Vertex AI Training Service. The notebook guides you through the process of moving from local training to cloud-based training, leveraging the managed infrastructure provided by Vertex AI.

## Objectives

1. Import and organize the data.
2. Organize your training code into a Python package.
3. Train your model using cloud infrastructure via Google Cloud Vertex AI Training Service.
4. (Optional) Learn how to run your training package using Docker containers and push training Docker images to a Docker registry.

## Introduction

In this notebook, we will transition from local training to cloud-based training using Google Cloud's [Vertex AI Training Service](https://cloud.google.com/vertex-ai/). Vertex AI Training Service is a managed service that allows the training and deployment of ML models without the need to provision or maintain servers. The managed service handles the infrastructure seamlessly for us.

## Prerequisites

- Google Cloud account
- Google Cloud SDK installed and configured
- Vertex AI API enabled
- BigQuery API enabled
- Cloud Storage bucket created

## Steps

### 1. Import and Organize the Data

- Load the necessary libraries.
- Set up the Google Cloud project, bucket, and region.
- Create BigQuery tables and export them as CSV files to Google Cloud Storage.

### 2. Organize Your Training Code into a Python Package

- Create a Python package directory.
- Move the existing code into a `model.py` file.
- Create a `task.py` file to handle command-line arguments and invoke the training function.

### 3. Train Your Model Using Cloud Infrastructure

- Test the training code locally.
- Package the code using `setuptools`.
- Upload the package to Google Cloud Storage.
- Submit a custom training job using the `gcloud` CLI or Vertex AI Python SDK.

### 4. (Optional) Run Your Training Package Using Docker

- Create a Dockerfile for the training package.
- Build and push the Docker image to a Docker registry.
- Submit a custom training job using the Docker image.

## Files

- `TRAINING_AT_SCALE_VERTEX.ipynb`: The main notebook containing the step-by-step guide.
- `taxifare/trainer/model.py`: The Python module containing the model code.
- `taxifare/trainer/task.py`: The Python module for handling command-line arguments and invoking the training function.
- `taxifare/setup.py`: The setup script for packaging the code.

## Usage

1. Follow the steps in the notebook to set up your environment and prepare the data.
2. Run the training code locally to ensure it works.
3. Submit a custom training job to Vertex AI using the `gcloud` CLI or Vertex AI Python SDK.
4. (Optional) Use Docker to containerize your training package and submit a custom training job using the Docker image.

## References

- [Vertex AI Documentation](https://cloud.google.com/vertex-ai/docs)
- [Google Cloud SDK](https://cloud.google.com/sdk)
- [BigQuery Documentation](https://cloud.google.com/bigquery/docs)
