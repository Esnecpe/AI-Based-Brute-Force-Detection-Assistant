from bruteForceDiagnostic import BruteForceDiagnostics
from llm_explainer import BruteForceLLMExplainer

def main():
    # Test the values for all inputs
    evidence = {
        "multiple_failed": "True",
        "same_ip": "False",
        "many_accounts": "True",
        "outside_hours": "False",
        "suspicious_ip": "False",
        "success_after_failures": "False"
    }

    # Step 1: Python Bayesian Network calculates probability
    # Instantiate the BruteForceDiagnostics class
    # Call the diagnose method
    bn = BruteForceDiagnostics()
    bn_result = bn.diagnose(
        multiple_failed=evidence["multiple_failed"],
        same_ip=evidence["same_ip"],
        many_accounts=evidence["many_accounts"],
        outside_hours=evidence["outside_hours"],
        suspicious_ip=evidence["suspicious_ip"],
        success_after_failures=evidence["success_after_failures"]
    )

    # Step 2: Display the raw Bayesian Network result
    print("\nBayesian Network Result")
    print("-----------------------")
    print(
        f"Probability of brute-force attack: "
        f"{bn_result['probability_percentage']}% ({bn_result['risk_level']})"
    )

    # Step 3: LLM explains the result
    explainer = BruteForceLLMExplainer()
    explanation = explainer.explain_result(bn_result, evidence)

    print("\nLLM Explanation and Recommendation")
    print("----------------------------------")
    print(explanation)

if __name__ == "__main__":
    main()