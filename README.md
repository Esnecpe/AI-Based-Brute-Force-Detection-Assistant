# AI-Based Brute Force Detection Assistant

## Overview

The AI-Based Brute Force Detection Assistant is a cybersecurity tool that uses Bayesian Networks and Artificial Intelligence techniques to estimate the probability of brute force attacks.

The system analyzes suspicious login-related indicators associated with IP addresses, URLs, and domains and applies probabilistic reasoning to determine whether brute force behavior is likely occurring. By combining cybersecurity evidence with Bayesian inference, the system provides risk assessments, explanations, and recommended mitigation actions.

This project was developed as part of an Artificial Intelligence course and demonstrates the practical application of Bayesian Networks in cybersecurity threat detection.

---

## Features

* Brute Force Attack Detection
* Bayesian Network Inference
* Probability-Based Risk Assessment
* Risk Level Classification
* Explainable AI Results
* Security Recommendations
* Graphical User Interface (GUI)
* IP Address Analysis
* URL Analysis
* Domain Analysis

---

## System Architecture

```text
User Input
(IP Address / URL / Domain)
            ↓

Evidence Collection

• Failed Login Attempts
• Login Frequency
• Multiple Username Attempts
• Suspicious Access Time
• IP Reputation

            ↓

Bayesian Network

(Probabilistic Reasoning)

            ↓

Brute Force Probability

            ↓

Risk Classification

(Low / Medium / High)

            ↓

Explanation Engine

            ↓

GUI Output
```

---

## Example Inputs

### IP Address

```text
185.220.101.5
```

### URL

```text
https://secure-login-check.com
```

### Domain

```text
suspicious-domain.net
```

---

## Example Output

```text
Target:
185.220.101.5

Threat Type:
Brute Force Attack

Brute Force Probability:
87%

Risk Level:
HIGH

Evidence:
- Failed Login Attempts: High
- Login Frequency: High
- Multiple Username Attempts: Yes
- Suspicious Access Time: Yes

Explanation:
The Bayesian Network estimates a high probability
of brute force activity based on repeated failed
authentication attempts and abnormal login patterns.

Recommended Actions:
- Block the source IP
- Enable Multi-Factor Authentication (MFA)
- Review authentication logs
- Configure account lockout policies
- Continue monitoring login activity
```

---

## Technologies Used

* Python
* Tkinter
* Bayesian Networks
* NumPy
* Pandas
* Large Language Models (LLMs)
* VirusTotal API (Optional)
* AbuseIPDB API (Optional)

---

## Bayesian Network Model

The Bayesian Network evaluates several cybersecurity indicators and combines them to estimate the likelihood of a brute force attack.

### Evidence Nodes

* Failed Login Attempts
* Login Frequency
* Multiple Username Attempts
* Suspicious Access Time
* IP Reputation

### Target Node

* Brute Force Attack Probability

The model uses probabilistic reasoning to calculate the likelihood that a brute force attack is occurring based on the collected evidence.

---

## Project Goals

The primary goal of this project is to demonstrate how Bayesian Networks can be used to detect brute force attacks through probabilistic reasoning.

The system evaluates multiple pieces of cybersecurity evidence and calculates the likelihood that a brute force attack is occurring. The project also provides explainable AI outputs and actionable security recommendations for analysts and system administrators.

---

## Authors

**Adrian Hernandez** &
**Peter Sarmiento**

---

**California State University, Fullerton**
Department of Computer Science
