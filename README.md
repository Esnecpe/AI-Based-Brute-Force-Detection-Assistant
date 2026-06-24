# AI-Based Brute Force Detection Assistant

## Authors

Adrian Hernandez
Peter Sarmiento

California State University, Fullerton
Department of Computer Science

CPSC 481 – Artificial Intelligence

---

# Project Overview

The AI-Based Brute Force Detection Assistant is an Artificial Intelligence and Cybersecurity project that uses a Bayesian Network to estimate the probability of a brute force login attack.

The system allows users to select cybersecurity evidence through a graphical user interface and then performs probabilistic reasoning to determine the likelihood that a brute force attack is occurring.

An LLM-based explanation module is also included to provide human-readable explanations and recommended response actions based on the Bayesian Network results.

---

# Project Goal

The goal of this project is to demonstrate how Bayesian Networks can be applied to cybersecurity threat detection under uncertainty.

Instead of relying on simple rule-based logic, the system evaluates multiple pieces of evidence and computes a probability that a brute force attack is occurring.

---

# Threat Focus

This project focuses on a single cybersecurity threat:

**Brute Force Login Attacks**

The scope was intentionally limited to one threat category in order to build a more focused and interpretable Bayesian Network.

---

# Evidence Variables

The Bayesian Network uses the following evidence variables:

* Multiple Failed Login Attempts
* Repeated Attempts From Same IP
* Attempts Across Many Accounts
* Login Outside Normal Hours
* Suspicious IP / Geolocation
* Successful Login After Many Failures

Each variable can be selected as:

* True
* False

The evidence is used to estimate the probability that a brute force attack is occurring.

---

# Bayesian Network Structure

Evidence Nodes:

* M = Multiple Failed Login Attempts
* I = Repeated Attempts From Same IP
* A = Attempts Across Many Accounts
* O = Login Outside Normal Hours
* G = Suspicious IP / Geolocation
* S = Successful Login After Many Failures

Intermediate Nodes:

* L = Login Failure Pattern
* C = Suspicious Login Context

Target Node:

* B = Brute Force Attack

The Bayesian Network combines the evidence variables and calculates:

P(Brute Force Attack | Evidence)

using variable elimination inference.

---

# System Architecture

User Input

↓

GUI Interface

↓

Evidence Variables

↓

Bayesian Network

↓

Probability Calculation

↓

Risk Classification

↓

LLM Explanation

↓

Output Window

---

# Graphical User Interface

The GUI was developed using Python Tkinter.

Features include:

* IP Address input type selection
* Evidence variable selection
* Analyze button
* Output display panel
* Bayesian Network integration
* LLM explanation generation

The GUI serves as the primary interface between the user and the diagnostic system.

---

# Example Output

Selected Evidence:

* Multiple Failed = True
* Same IP = True
* Many Accounts = True
* Outside Hours = True
* Suspicious IP = True
* Success After Failures = False

Possible Result:

Probability of brute-force attack: 92%

Risk Level: High

The LLM then provides:

* Explanation of the result
* Recommended response actions
* Human-readable cybersecurity guidance

---

# Technologies Used

* Python
* Tkinter
* Bayesian Networks
* Variable Elimination Inference
* NumPy
* OpenAI-Compatible LLM API
* AIMA Probability Library

---

# Repository Structure

```text
AI-Based-Brute-Force-Detection-Assistant/

├── GUI.py
├── bruteForceDiagnostic.py
├── llm_explainer.py
├── probability4e.py
├── utils4e.py
├── README.md
└── assets/
```

# File Descriptions

## GUI.py

Provides the graphical user interface.

Responsibilities:

* Collect user evidence
* Trigger analysis
* Display Bayesian Network results
* Display LLM explanations

---

## bruteForceDiagnostic.py

Contains the Bayesian Network implementation.

Responsibilities:

* Define network structure
* Define conditional probability tables
* Perform variable elimination inference
* Calculate brute force probabilities
* Determine risk levels

---

## llm_explainer.py

Provides AI-generated explanations.

Responsibilities:

* Convert Bayesian Network output into human-readable language
* Explain risk levels
* Generate cybersecurity recommendations

---

## probability4e.py

AIMA probability and Bayesian Network implementation.

Responsibilities:

* Bayesian Network data structures
* Variable elimination algorithms
* Probability distributions
* Inference methods

---

## utils4e.py

Utility functions required by the AIMA probability framework.

Responsibilities:

* Mathematical helpers
* Probability utilities
* Data structures
* General support functions

---

## README.md

Project documentation.

Responsibilities:

* Explain project goals
* Describe architecture
* Describe file structure
* Help users understand the implementation

---

# What Was Completed

Completed components:

* Bayesian Network design
* Evidence variables
* Conditional probability tables
* Variable elimination inference
* Tkinter GUI
* Risk level classification
* LLM explanation generation
* Project documentation
* Presentation materials

---

# Educational Purpose

This project was developed for educational purposes as part of CPSC 481 – Artificial Intelligence at California State University, Fullerton.

The project demonstrates how Artificial Intelligence techniques, specifically Bayesian Networks and probabilistic reasoning, can be applied to cybersecurity threat detection.
