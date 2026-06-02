# Cloud Monitor Dashboard ☁️

A real-time AWS cloud monitoring dashboard built using Amazon EC2, CloudWatch, Lambda, API Gateway, and a custom frontend.

This project monitors live server metrics and displays them through a responsive dashboard with automatic updates and alert logic.

---

# Project Overview

Cloud Monitor Dashboard is a cloud monitoring Proof of Concept (POC) designed to visualize infrastructure health using AWS native monitoring services.

The dashboard displays:

* CPU Usage
* Memory Usage
* Disk Usage
* Server Status
* Alerts
* Last Updated Time (IST)

The project retrieves real metrics from AWS CloudWatch and displays them through a custom frontend built using HTML, CSS, and JavaScript.

---

# Architecture

## Architecture Diagram

![Architecture](Picture/Architecture%20Diagram.png)

---

# AWS Services Used

## Amazon EC2

Hosts the monitored server instance.

## Amazon CloudWatch

Collects infrastructure metrics.

## CloudWatch Agent

Publishes memory and disk metrics to CloudWatch.

## AWS Lambda

Fetches CloudWatch metrics and exposes them through an API.

## API Gateway

Provides secure API access to the frontend dashboard.

---

# Features

* ✅ Real-time monitoring
* ✅ Live CPU metrics
* ✅ Live Memory metrics
* ✅ Live Disk metrics
* ✅ Auto-refresh every 10 seconds
* ✅ Animated metric counters
* ✅ Alert and warning system
* ✅ Server health status
* ✅ Indian timezone (IST) support
* ✅ Responsive dark dashboard UI

---

# Dashboard Preview

## Healthy State

![Healthy Dashboard](Picture/Normal%20screen%20.png)

Example:

* Online 🟢
* No Alerts
* Normal CPU / Memory / Disk Usage

---

## Warning State

![Warning Dashboard](Picture/High%20CPU.png)

Example:

* Warning 🟡
* High CPU Alert
* Live spike detection

---

## CloudWatch CPU Metrics

![CPU Metrics](Picture/CPUUtilization%20Graph.png)

---

## Memory and Disk Metrics

![CWAgent Metrics](Picture/CWagent%20graph.png)

---

# Additional AWS Screenshots

## Lambda Dashboard

![Lambda Dashboard](Picture/Lambda%20Dashboard.png)

---

## API Gateway Deployment

![API Gateway](Picture/API%20Gateway%20Deploy%20.png)

---

## IAM Permissions

![IAM](Picture/IAM%20permissions.png)

---

# Project Workflow

1. CloudWatch Agent collects metrics from EC2
2. Metrics are pushed to CloudWatch
3. Lambda retrieves metrics using Boto3
4. API Gateway exposes the Lambda endpoint
5. Dashboard fetches and displays live data

---

# Technologies Used

## Frontend

* HTML
* CSS
* JavaScript

## Backend / Cloud

* AWS Lambda
* API Gateway
* Boto3
* CloudWatch
* CloudWatch Agent
* EC2

---

# AI-Assisted Development

This project was developed using GitHub Copilot as an AI coding assistant.

Copilot was used to accelerate frontend implementation and code refinement, while project architecture, AWS integration, monitoring setup, debugging, and validation were designed and implemented as part of the learning and development process.

---

# Testing and Validation

The monitoring system was tested using controlled resource spikes.

## CPU Testing

```bash
yes > /dev/null &
```

## Memory Testing

```bash
python3 -c "a=' ' * 500000000; input()"
```

## Disk Testing

```bash
fallocate -l 1G testfile.img
```

## Cleanup

```bash
pkill yes
pkill -f python3
rm -f testfile.img
```

These tests validated dashboard responsiveness and alert behavior.

---

# Future Improvements

* CloudWatch alarms integration
* Email / SNS alerts
* Multi-server monitoring
* Historical charts and analytics
* Authentication and secure dashboard access

---

# Learning Outcome

This project helped build practical understanding of:

* Cloud Monitoring
* Observability
* AWS Serverless Architecture
* CloudWatch Metrics
* API Integration
* Frontend + Cloud Integration

---

# Author

## Joyal B Biju

GitHub:
https://github.com/JoyalBBiju/aws-monitoring-dashboard

LinkedIn:
https://www.linkedin.com/feed/update/urn:li:activity:7467561110372519936/
