# CSV Header Description Generator  

This Python script reads the column headers from a CSV file and generates short, human-readable descriptions for each header using an open-source Hugging Face model.  

It reads the csv and exrtracts the headers.Then it uses an open source model to generate a description of the header name.Then it takes the output and Stores in an output file named output.txt.

To run this use command: 
```bash
python generate_descriptions.py input.csv
```
## Tech stack:
- Python
- Hugging Face
- PyTorch
- Model: GPT2
