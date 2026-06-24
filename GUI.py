import tkinter as tk
from tkinter import ttk
from bruteForceDiagnostic import BruteForceDiagnostics
from llm_explainer import BruteForceLLMExplainer


class CyberSecurityGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("AI Consultant")

        self.diagnostic_system = BruteForceDiagnostics()
        self.llm_explainer = BruteForceLLMExplainer()


        title = tk.Label(
            root,
            text="AI-Based Brute Force Detection Assistant",
            font=("Arial", 16, "bold")
        )
        title.grid(row=0, column=0, columnspan=2, pady=(12, 8))

        # ── Left panel frame 
        left = tk.Frame(root)
        left.grid(row=1, column=0, padx=(15, 8), pady=4, sticky="n")

        # Input Type
        ttk.Label(left, text="Input Type", font=("Arial", 10, "bold")).grid(
            row=0, column=0, sticky="w", pady=(0, 2))
        self.input_type_var = tk.StringVar(value="IP Address")
        input_type_dropdown = ttk.Combobox(
            left,
            textvariable=self.input_type_var,
            values=["IP Address"],
            state="readonly",
            width=22
        )
        input_type_dropdown.grid(row=1, column=0, columnspan=2, sticky="w", pady=(0, 10))

        # Evidence Variables label
        ttk.Label(left, text="Evidence Variables", font=("Arial", 10, "bold")).grid(
            row=2, column=0, columnspan=2, sticky="w", pady=(4, 6))

        evidence_vars = [
            ("Multiple failed",      "multiple_failed_var"),
            ("Same IP",              "same_ip_var"),
            ("Many accounts",        "many_accounts_var"),
            ("Outside hours",        "outside_hours_var"),
            ("Suspicious IP",        "suspicious_ip_var"),
            ("Success after failures","success_after_failures_var"),
        ]

        self.evidence_dropdowns = {}
        for i, (label, attr) in enumerate(evidence_vars):
            ttk.Label(left, text=label).grid(row=3 + i, column=0, sticky="w",
                                              padx=(0, 10), pady=4)
            var = tk.StringVar(value="NA")
            setattr(self, attr, var)
            cb = ttk.Combobox(
                left,
                textvariable=var,
                values=["True", "False"],
                state="readonly",
                width=10
            )
            cb.grid(row=3 + i, column=1, sticky="w", pady=4)
            self.evidence_dropdowns[attr] = cb

        # Analyze button
        analyze_button = ttk.Button(left, text="Analyze", command=self.run_analysis,
                                    width=22)
        analyze_button.grid(row=3 + len(evidence_vars), column=0, columnspan=2,
                            pady=(14, 4))

        self.textbox = tk.Text(root, height=22, width=48, wrap="word")
        self.textbox.grid(row=1, column=1, padx=(8, 15), pady=4, sticky="nsew")

        # Auto-size window to fit all widgets, then lock minimum size
        root.update_idletasks()
        w = root.winfo_reqwidth()
        h = root.winfo_reqheight()
        root.geometry(f"{w}x{h}")
        root.minsize(w, h)

    def run_analysis(self):
        original_inputs = {
            "multiple_failed": self.multiple_failed_var.get(),
            "same_ip": self.same_ip_var.get(),
            "many_accounts": self.many_accounts_var.get(),
            "outside_hours": self.outside_hours_var.get(),
            "suspicious_ip": self.suspicious_ip_var.get(),
            "success_after_failures": self.success_after_failures_var.get()
        }

        bn_result = self.diagnostic_system.diagnose(
            multiple_failed=original_inputs["multiple_failed"],
            same_ip=original_inputs["same_ip"],
            many_accounts=original_inputs["many_accounts"],
            outside_hours=original_inputs["outside_hours"],
            suspicious_ip=original_inputs["suspicious_ip"],
            success_after_failures=original_inputs["success_after_failures"]
        )

        llm_output = self.llm_explainer.explain_result(
            bn_result,
            original_inputs
        )

        output_text = "Bayesian Network Result:\n"
        output_text += f"Probability of brute-force attack: {bn_result['probability_percentage']}%\n"
        output_text += f"Risk Level: {bn_result['risk_level']}\n\n"
        output_text += "LLM Explanation and Recommendation:\n"
        output_text += llm_output

        self.textbox.delete("1.0", tk.END)
        self.textbox.insert(tk.END, output_text)


if __name__ == "__main__":
    root = tk.Tk()
    app = CyberSecurityGUI(root)
    root.mainloop()
