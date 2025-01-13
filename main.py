import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "cancer_data.xlsx"  # Replace with your file path
data = pd.read_excel(file_path)

# Step 1: Inspect the Data
print("\nData Information:")
data.info()
print("\nData Description:")
print(data.describe())

# Step 2: Select Features
numerical_features = ["Age", "BMI", "TumorSize", "SurvivalMonths"]
categorical_features = ["Gender", "CancerType", "Stage", "TreatmentResponse"]

# Step 3: Visualizations
# Histograms
for feature in numerical_features:
    plt.figure(figsize=(8, 5))
    sns.histplot(data[feature], kde=True, bins=20, color='blue')
    plt.title(f"Distribution of {feature}")
    plt.xlabel(feature)
    plt.ylabel("Frequency")
    plt.savefig(f"{feature}_histogram.png")  # Save histogram
    plt.show()

# Scatter Plot: TumorSize vs. SurvivalMonths
plt.figure(figsize=(8, 6))
sns.scatterplot(data=data, x="TumorSize", y="SurvivalMonths", alpha=0.5, color="blue")
plt.title("Tumor Size vs. Survival Months")
plt.xlabel("Tumor Size")
plt.ylabel("Survival Months")
plt.savefig("scatter_plot_tumor_vs_survival.png")  # Save scatter plot
plt.show()

# Correlation Heatmap
correlation_matrix = data[numerical_features].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.savefig("correlation_plot.png")  # Save heatmap
plt.show()

# Save Analysis to Text File
with open("analysis.txt", "w") as f:
    f.write("### Data Analysis Report\n\n")
    f.write("#### Numerical Features:\n")
    f.write(f"{numerical_features}\n\n")
    f.write("#### Observations:\n")
    f.write("1. Distributions of Age, BMI, Tumor Size, and Survival Months were plotted.\n")
    f.write("2. Correlation analysis revealed relationships between numerical variables.\n")
    f.write("3. Scatter plots were used to explore trends between Tumor Size and Survival Months.\n")

