# Cronbach's_Alpha_Calculator
Cronbach's Alpha is a measure of internal consistency, or how closely related a set of items are as a group. It is commonly used to assess the reliability of a questionnaire or survey, especially when measuring a latent construct. The script `Cronbach-s_Alpha.py` is created based on the formula developed by Cronbach in 1951 [1] reads data from a CSV file and calculates Cronbach's Alpha for user-defined dimensions.
## Features
CSV Input: Reads data from a CSV file.

Custom Dimensions: Calculates Cronbach's Alpha for specified dimensions (groups of columns).

Variance Calculation: Computes variance for each item and total scores.

Cronbach's Alpha Formula: Implements the formula for Cronbach's Alpha to check internal consistency.

## How to Use
1. In the script, update the `file_path` variable with the path to your CSV file.
2. Update the dimensions
3. Run the script

## CSV file
The CSV file should be structured as follows:
The first row contains headers (column names).
The subsequent rows contain numeric data for each item in the survey or questionnaire.

## How to Cite
A DOI badge has been added to the README to reference this repository in academic publications and other documentation. This badge links directly to the Zenodo archive, providing a stable and citable DOI.
[![DOI](https://zenodo.org/badge/854681259.svg)](https://zenodo.org/doi/10.5281/zenodo.13824251)






## References
1. Cronbach, L.J., 1951. Coefficient alpha and the internal structure of tests. psychometrika 16, 297–334 .

```bash
python Cronbach-s_Alpha.py
