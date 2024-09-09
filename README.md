# Cronbach's_Alpha_Calculator
Cronbach's Alpha is a measure of internal consistency, or how closely related a set of items are as a group. It is commonly used to assess the reliability of a questionnaire or survey, especially when measuring a latent construct. The script `Cronbach-s_Alpha.py` is created based on the formula developed by Cronbach in 1951 [1] reads data from a CSV file and calculates Cronbach's Alpha for user-defined dimensions.
## Features
CSV Input: Reads data from a CSV file.

Custom Dimensions: Calculates Cronbach's Alpha for specified dimensions (groups of columns).

Variance Calculation: Computes variance for each item and total scores.

Cronbach's Alpha Formula: Implements the formula for Cronbach's Alpha to check internal consistency.

## How to Use
1. In the script, update the `file_path` variable with the path to your CSV file.
2. Update the dimnsions
3. Run the script

## CSV file
The CSV file should be structured as follows:
The first row contains headers (column names).
The subsequent rows contain numeric data for each item in the survey or questionnaire.

## References
1. Cronbach, L.J., 1951. Coefficient alpha and the internal structure of tests. psychometrika 16, 297–334 (https://doi.org/10.1007/BF02310555).

```bash
python Cronbach-s_Alpha.py
