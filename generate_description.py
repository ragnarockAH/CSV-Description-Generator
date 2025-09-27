"""
CSV Header Description Generator
--------------------------------
This script reads the column headers from a CSV file (provided as an argument)
and uses a small, offline Hugging Face model to generate
short, human-readable descriptions for each column.

Results are printed to the console and also saved into output.txt.

Usage:
    python generate_descriptions.py input.csv
"""

import os
import sys
import pandas as pd
from transformers import pipeline


def load_csv_headers(filepath: str):
    """
    Reads the headers (column names) from a CSV file.
    If the file does not exist, exit with an error.
    """
    if not os.path.exists(filepath):
        print(f"Error: File '{filepath}' not found.")
        sys.exit(1)

    df = pd.read_csv(filepath)
    return df.columns.tolist()


def generate_descriptions(headers, model_name="gpt2"):
    """
    Uses a Hugging Face text-generation model to create one-sentence
    descriptions for each header.
    """
    generator = pipeline("text-generation", model=model_name)
    descriptions = {}

    for header in headers:
        prompt = f"The data column named '{header}' represents"
        result = generator(prompt, max_new_tokens=40, num_return_sequences=1)[0]["generated_text"]

        # Keep only the first sentence
        sentence = result.split(".")[0].strip() + "."
        descriptions[header] = sentence.replace(prompt, "").strip().capitalize()

    return descriptions


def save_descriptions(descriptions, filepath="output.txt"):
    """
    Save the generated descriptions into a text file.
    """
    with open(filepath, "w", encoding="utf-8") as f:
        for column, desc in descriptions.items():
            line = f"{column} -> {desc}\n"
            print(line.strip())  # Print nicely to console
            f.write(line)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate_descriptions.py <input_csv_file>")
        sys.exit(1)

    csv_path = sys.argv[1]
    headers = load_csv_headers(csv_path)

    print("Generating column descriptions...\n")
    descriptions = generate_descriptions(headers, model_name="gpt2")

    save_descriptions(descriptions, filepath="output.txt")
    print("\nDescriptions saved to output.txt")
