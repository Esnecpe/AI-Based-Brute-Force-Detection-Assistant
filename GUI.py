import tkinter as tk
from tkinter import ttk
#from cybersecurity_diagnostics import CyberSecurityDiagnostics


class CyberSecurityGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("AI Consultant")

        #self.diagnostic_system = CyberSecurityDiagnostics()

        title = tk.Label(
            root,
            text="AI-Based Brute Force Detection Assistant",
            font=("Arial", 18, "bold")
        )
        title.grid(row=0, column=0, columnspan=2, pady=(10, 15))

        ttk.Label(root, text="Input Type").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.input_type_var = tk.StringVar(value="IP Address")
        input_type_dropdown = ttk.Combobox(
            root,
            textvariable=self.input_type_var,
            values=["IP Address", "URL", "Domain"],
            state="readonly"
        )
        input_type_dropdown.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        ttk.Label(root, text="Suspicious IP / URL / Domain").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.target_var = tk.StringVar()
        target_entry = ttk.Entry(root, textvariable=self.target_var, width=45)
        target_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        analyze_button = ttk.Button(root, text="Analyze", command=self.run_analysis)
        analyze_button.grid(row=3, column=0, pady=10)

        self.textbox = tk.Text(root, height=16, width=70)
        self.textbox.grid(row=3, column=1, padx=10, pady=10)

        root.update_idletasks()
        width = root.winfo_reqwidth()
        height = root.winfo_reqheight()
        root.geometry(f"{width}x{height}")
        root.minsize(width, height)

    def run_analysis(self):
        result = self.diagnostic_system.analyze_threat(
            self.input_type_var.get(),
            self.target_var.get()
        )

        output_text = f"Target:\n{result['target']}\n\n"
        output_text += f"Diagnosis:\n{result['diagnosis']}\n\n"
        output_text += f"Threat Score:\n{result['threat_score']}%\n\n"
        output_text += f"Risk Level:\n{result['risk_level']}\n\n"
        output_text += f"Explanation:\n{result['explanation']}\n\n"
        output_text += "Recommended Actions:\n"

        for action in result["recommendations"]:
            output_text += f"- {action}\n"

        self.textbox.delete("1.0", tk.END)
        self.textbox.insert(tk.END, output_text)


if __name__ == "__main__":
    root = tk.Tk()
    app = CyberSecurityGUI(root)
    root.mainloop()
