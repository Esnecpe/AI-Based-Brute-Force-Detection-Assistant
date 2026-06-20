# Cybersecurity Threat Intelligence Assistant

## Overview

The Cybersecurity Threat Intelligence Assistant is an AI-powered cybersecurity tool that analyzes suspicious IP addresses, URLs, and domains. The system combines real-world threat intelligence sources, Bayesian Network reasoning, and Large Language Model (LLM) explanations to help users identify potential cybersecurity threats and receive actionable recommendations.

This project was developed as part of an Artificial Intelligence course and demonstrates the integration of probabilistic reasoning, threat intelligence, and AI-generated explanations.

---

## Features

* Analyze suspicious IP addresses
* Analyze suspicious URLs
* Analyze suspicious domains
* Bayesian Network threat assessment
* Risk level classification
* Threat score generation
* AI-generated explanations
* Security recommendations
* Graphical User Interface (GUI)

---

## System Architecture

```text
User Input (IP / URL / Domain)
            ↓
Threat Intelligence APIs
(VirusTotal, AbuseIPDB, URLhaus)
            ↓
Bayesian Network
(Probabilistic Reasoning)
            ↓
LLM Explanation Layer
            ↓
Risk Assessment Report
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
https://suspicious-login-verification.com
```

### Domain

```text
malicious-domain.net
```

---

## Example Output

```text
Diagnosis:
Brute Force Attack

Probability:
82.00%

Risk Level:
HIGH

Threat Score:
91%

Explanation:
The submitted IP address appears in multiple
threat intelligence reports and exhibits
behavior commonly associated with brute-force
attacks.

Recommended Actions:
- Block the IP address
- Review authentication logs
- Enable multi-factor authentication
- Monitor for additional attempts
```

---

## Technologies Used

* Python
* Tkinter
* Bayesian Networks
* OpenAI API / LLM APIs
* VirusTotal API
* AbuseIPDB API
* URLhaus API

---

## Project Goals

The goal of this project is to demonstrate how Artificial Intelligence techniques can be applied to cybersecurity investigations. By combining threat intelligence, Bayesian reasoning, and language models, the system provides both automated threat assessment and human-readable explanations.

---

## Authors

Adrian Hernandez &
Peter Sarmiento

California State University, Fullerton

Computer Science
