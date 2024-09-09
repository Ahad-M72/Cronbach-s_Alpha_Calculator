# Function to read CSV data into a list of lists and handle headers
def read_csv(file_path):
    data = []
    with open(file_path, 'r') as file:
        headers = next(file).strip().split(',')
        for line in file:
            data.append(list(map(float, line.strip().split(','))))
    return headers, data

# Function to calculate variance for a list of numbers
def variance(numbers):
    mean = sum(numbers) / len(numbers)
    return sum((x - mean) ** 2 for x in numbers) / (len(numbers) - 1)

# Function to calculate Cronbach's Alpha 
def cronbach_alpha(data, headers, dimension):
    indices = [headers.index(col) for col in dimension]
    items_variances = []
    total_scores = [0] * len(data)
    
    # Calculate total scores and variances for each item
    for i in range(len(data)):
        for index in indices:
            total_scores[i] += data[i][index]
        for index in indices:
            column = [row[index] for row in data]
            if i == 0:  # Calculate variances only once
                items_variances.append(variance(column))
    
    # Total variance of summed scores
    total_variance = variance(total_scores)
    sum_variances = sum(items_variances)
    
    # Number of items
    n_items = len(dimension)
    
    # Cronbach's Alpha formula
    alpha = (n_items / (n_items - 1)) * (total_variance - sum_variances) / total_variance
    return alpha

# Define dimensions (name the dimensions as your actual dimension names)
# you should change X_i and Y_i to your actual column headers
dimensions = {
    'DIMENSION X': ['X1', 'X2', 'X3'],
    'DIMENSION Y': ['Y1', 'Y2', 'Y3']
}

# Load data from CSV file
file_path = 'path_to_your_file.csv'  # Update to your actual path
headers, data = read_csv(file_path)

# Calculate and print Cronbach's Alpha for each dimension
for dimension, cols in dimensions.items():
    alpha = cronbach_alpha(data, headers, cols)
    print(f"{dimension}: Cronbach's Alpha = {alpha:.4f}")
