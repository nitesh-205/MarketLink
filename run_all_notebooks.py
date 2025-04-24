import os
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

# Path to your notebooks folder
notebook_folder = "Backend Algorithms"
output_folder = "executed_notebooks"

# Create output folder if not exists
os.makedirs(output_folder, exist_ok=True)

# Loop through all .ipynb files in the folder
for filename in os.listdir(notebook_folder):
    if filename.endswith(".ipynb") and "-checkpoint" not in filename:
        notebook_path = os.path.join(notebook_folder, filename)
        print(f"Running: {filename}")

        with open(notebook_path, encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=4)

        ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
        try:
            ep.preprocess(nb, {'metadata': {'path': notebook_folder}})
            # Save the executed notebook
            with open(os.path.join(output_folder, filename), 'w', encoding='utf-8') as f:
                nbformat.write(nb, f)
            print(f"Executed and saved: {filename}")
        except Exception as e:
            print(f"❌ Error in {filename}: {e}")
