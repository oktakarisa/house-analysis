import subprocess
import os

# Directory containing problem scripts
src_dir = "src"

# Scripts to execute in order
scripts = [
    "problem1_load_dataset.py",
    "problem2_dataset_investigation.py",
    "problem3_checking_data.py",
    "problem4_missing_values.py",
    "problem5_distribution_terms.py",
    "problem6_distribution_analysis.py",
    "problem7_correlation_analysis.py",
]

def run_scripts():
    for script in scripts:
        script_path = os.path.join(src_dir, script)
        print(f"\n>>> Running {script_path} ...\n")
        try:
            subprocess.run(["python", script_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error while running {script}: {e}")
            break

if __name__ == "__main__":
    run_scripts()
