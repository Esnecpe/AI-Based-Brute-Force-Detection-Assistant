from probability4e import *

T, F = True, False

class BruteForceDiagnostics:
  # Define a Bayesian Network for estimating the probability of a brute-force login attack.
  def __init__(self):
        # Nodes: M=Multiple Failed Login Attempts, I=Repeated Attempts From Same IP, A=Attempts Across Many Accounts
        # O=Login Outside Normal Hours, G=Suspicious IP / Geolocation, S=Successful Login After Many Failures
        # L=Login Failure Pattern is High, C=Suspicious Login Context is High, B=Brute Force Attack
    self.BN = BayesNet([
        # node format: (variable name, parents name, cpt)
        # Root evidence nodes
        ('M', '', 0.30),
        ('I', '', 0.20),
        ('A', '', 0.15),
        ('O', '', 0.20),
        ('G', '', 0.15),
        ('S', '', 0.10),

        # intermediate node: Login Failure Pattern High
        ('L', ['M', 'I', 'A'], {
            (T, T, T): 0.95,
            (T, T, F): 0.80,
            (T, F, T): 0.85,
            (F, T, T): 0.70,
            (T, F, F): 0.45,
            (F, T, F): 0.40,
            (F, F, T): 0.50,
            (F, F, F): 0.05
        }),

        # intermediate node: Suspicious Login Context
        ('C', ['O', 'G'], {
            (T, T): 0.85,
            (T, F): 0.35,
            (F, T): 0.50,
            (F, F): 0.05
        }),

        # final diagnosis node: Brute Force Attack
        ('B', ['L', 'C', 'S'], {
            (T, T, T): 0.97,
            (T, T, F): 0.90,
            (T, F, T): 0.85,
            (T, F, F): 0.70,
            (F, T, T): 0.65,
            (F, T, F): 0.40,
            (F, F, T): 0.30,
            (F, F, F): 0.05
        })
    ])

  # Converts string inputs from the GUI interface to boolean T/F for Bayesian Network queries
  def true_false_to_bool(self, value):
    if value == "True":
      return T
    elif value == "False":
      return F
    else:
      return None

  def get_risk_level(self, probability):
    if probability < 0.40:
      return "Low"
    elif probability < 0.70:
      return "Medium"
    else:
      return "High"

  def diagnose(self, multiple_failed, same_ip, many_accounts, outside_hours, suspicious_ip, success_after_failures):
    evidence = {}

    # Converts string inputs from the GUI interface to boolean T/F for Bayesian Network queries
    M_value = self.true_false_to_bool(multiple_failed)
    I_value = self.true_false_to_bool(same_ip)
    A_value = self.true_false_to_bool(many_accounts)
    O_value = self.true_false_to_bool(outside_hours)
    G_value = self.true_false_to_bool(suspicious_ip)
    S_value = self.true_false_to_bool(success_after_failures)

    # Only add observed values to evidence
    if M_value is not None:
      evidence['M'] = M_value

    if I_value is not None:
      evidence['I'] = I_value

    if A_value is not None:
      evidence['A'] = A_value

    if O_value is not None:
      evidence['O'] = O_value

    if G_value is not None:
      evidence['G'] = G_value

    if S_value is not None:
      evidence['S'] = S_value

    # Query the Bayesian Network for:
    # P(B = True | evidence)
    # calls elimnation_ask() function from probability4e.py
    brute_force_distribution = elimination_ask('B', evidence, self.BN)

    brute_force_probability = brute_force_distribution[T]

    probability_percentage = round(brute_force_probability * 100, 2)
    risk_level = self.get_risk_level(brute_force_probability)

    return {
      "probability_decimal": brute_force_probability,
      "probability_percentage": probability_percentage,
      "risk_level": risk_level,
      "evidence": evidence
    }