# Import necessary libraries
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# Access the variable
api_key = os.environ.get("CPSC481_API_KEY")

class BruteForceLLMExplainer:
  """Use an LLM to explain the Bayesian Network result."""
  def __init__(self):
    # Initialize the OpenAI client
    self.llm = OpenAI(
    api_key=api_key,
    base_url="https://ellm.nrp-nautilus.io/v1",
    )

  def explain_result(self, bn_result, original_inputs):
    probability = bn_result["probability_percentage"]
    risk_level = bn_result["risk_level"]

    # 1. Prompting the LLM
    self.model_context = f"""
    Role:
    You are a cybersecurity assistant explaining the result of a Bayesian Network

    Task:
    Explain the brute-force login attack diagnosis
    - Do not calculate a new probability.
    - Do not change the probability.
    - Do not change the risk level.
    - Do not mention CPT values.

    Context:
    A Python Bayesian Network has already calculated the following result:
    Probability of brute-force attack: {probability}%
    Risk level: {risk_level}

    Original User Evidence:
    - Multiple failed login attempts: {original_inputs["multiple_failed"]}
    - Repeated attempts from same IP: {original_inputs["same_ip"]}
    - Attempts across many accounts: {original_inputs["many_accounts"]}
    - Login outside normal hours: {original_inputs["outside_hours"]}
    - Suspicious IP or geolocation: {original_inputs["suspicious_ip"]}
    - Successful login after many failures: {original_inputs["success_after_failures"]}

    Output Format:
    Probability of brute-force attack: {probability}% ({risk_level})

    Explanation:
    [Write 2-4 sentences explaining why the evidence supports this risk level.]

    Recommended response action:
    [List 2-5 recommended actions appropriate for the risk level.]

    Rules:
    - Use the exact probability provided: {probability}%
    - Use the exact risk level provided: {risk_level}
    - Use cautious language such as "suggests", "may indicate", or "is consistent with"
    - Do not say the attack is confirmed
    """

    try:
      response = self.llm.chat.completions.create(
        model="gpt-oss",
        messages=[
                  {"role": "system", "content": "You explain Bayesian Network cybersecurity results clearly."},
                  {"role": "user", "content": self.model_context}
              ],
              temperature=0.1
      )

      return response.choices[0].message.content

    except Exception as e:
            return f"LLM explanation error: {str(e)}"