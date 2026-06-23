# AI-Based Brute Force Detection Assistant

## Overview

The AI-Based Brute Force Detection Assistant is an Artificial Intelligence and Cybersecurity project that uses a Bayesian Network to estimate the probability of a brute force attack.

The system allows users to select evidence variables commonly associated with brute force attacks and then uses probabilistic reasoning to determine the likelihood that a brute force attack is occurring.

This project was developed as part of an Artificial Intelligence course at California State University, Fullerton and demonstrates the practical application of Bayesian Networks for cybersecurity threat detection.

---

## Features

* Bayesian Network-Based Brute Force Detection
* Evidence-Based Threat Assessment
* Probability-Based Risk Classification
* Explainable AI Results
* Graphical User Interface (GUI)
* Cybersecurity Decision Support
* Brute Force Attack Probability Estimation

---

## Evidence Variables

The Bayesian Network uses the following evidence nodes:

* Multiple Failed Logins
* Attempts From Same IP
* Attempts Across Many Accounts
* Login Attempts Outside Normal Hours
* Suspicious IP / Geolocation
* Successful Login After Failures

Each variable can be assigned one of the following values:

* True
* False
* NA (Unknown / Not Available)

These evidence variables are used by the Bayesian Network to estimate the probability of a brute force attack.

---

## System Architecture

```text
User Evidence Selection
        ↓

Evidence Nodes

• Multiple Failed Logins
• Same IP
• Many Accounts
• Outside Hours
• Suspicious IP
• Success After Failures

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

## Graphical User Interface

The GUI allows users to select cybersecurity evidence through dropdown menus.

Current GUI Components:

* Input Type (IP Address)
* Multiple Failed
* Same IP
* Many Accounts
* Outside Hours
* Suspicious IP
* Success After Failures
* Analyze Button
* Results Window

The Analyze button will trigger the Bayesian Network and display the final assessment inside the output panel.

---

## Example Scenario

### Selected Evidence

```text
Multiple Failed: True
Same IP: True
Many Accounts: True
Outside Hours: True
Suspicious IP: True
Success After Failures: False
```

### Expected Result

```text
Threat Type:
Brute Force Attack

Probability:
92%

Risk Level:
HIGH
```

---

## Technologies Used

* Python
* Tkinter
* Bayesian Networks
* NumPy
* Pandas

---

## Project Structure

```text
AI-Based-Brute-Force-Detection-Assistant/

│
├── GUI.py
├── diagnostic.py
├── bayesian_network.py
├── README.md
│
└── assets/
```

---

## File Descriptions

### GUI.py

Contains the graphical user interface built using Tkinter.

Responsibilities:

* Display evidence variables
* Collect user selections
* Display analysis results
* Provide interaction between the user and the Bayesian Network

### diagnostic.py

Handles the cybersecurity analysis workflow.

Responsibilities:

* Receive GUI inputs
* Process evidence variables
* Generate threat assessments
* Produce recommendations

### bayesian_network.py

Implements the Bayesian Network model.

Responsibilities:

* Define evidence nodes
* Define probability tables
* Perform Bayesian inference
* Calculate brute force attack probability

### README.md

Project documentation.

Responsibilities:

* Explain project goals
* Describe architecture
* Explain code structure
* Help other students understand the project

### assets/

Stores project screenshots, diagrams, and supporting images.

---

## Bayesian Network Design

Evidence Nodes:

* Multiple Failed Logins
* Attempts From Same IP
* Attempts Across Many Accounts
* Outside Hours
* Suspicious IP / Geolocation
* Successful Login After Failures

Target Node:

* Brute Force Attack

The Bayesian Network combines the evidence nodes and calculates the probability that a brute force attack is occurring.

---

## Project Goals

The goal of this project is to demonstrate how Bayesian Networks can be applied to cybersecurity threat detection.

The system uses evidence-based reasoning to estimate the likelihood of brute force attacks and provide understandable explanations for users.

---

## Authors

Adrian Hernandez
&
Peter Sarmiento

California State University, Fullerton

Department of Computer Science

