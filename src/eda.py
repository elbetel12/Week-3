# src/eda.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def create_folder(path):
    """Create folder if it doesn't exist."""
    if not os.path.exists(path):
        os.makedirs(path)

# ----------------------------
# 1. Load Data
# ----------------------------
def load_data(filepath, sep="|"):
    """Load dataset with error handling."""
    try:
        df = pd.read_csv(filepath, sep=sep)
        print(f"Data loaded successfully. Shape: {df.shape}")
        return df
    except FileNotFoundError:
        print(f"Error: File {filepath} not found.")
        return None
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# ----------------------------
# 2. Basic Info
# ----------------------------
def basic_info(df):
    """Print basic info and numeric summaries."""
    print("Shape:", df.shape)
    print("\nData Types:\n", df.dtypes)
    print("\nMissing Values:\n", df.isnull().sum())
    
    numeric_cols = ['TotalPremium', 'TotalClaims', 'CustomValueEstimate', 
                    'SumInsured', 'CalculatedPremiumPerTerm', 
                    'cubiccapacity', 'kilowatts', 'Cylinders']
    
    # Keep only columns that exist in df
    for col in numeric_cols:
     if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    else:
        print("No numeric columns found for descriptive statistics.")

# ----------------------------
# 3. Univariate Analysis
# ----------------------------
def univariate_analysis(df, plot_dir="plots"):
    """Plot histograms for numeric columns."""
    create_folder(plot_dir)
    
    numeric_cols = ['TotalPremium', 'TotalClaims', 'CustomValueEstimate', 
                    'SumInsured', 'CalculatedPremiumPerTerm', 
                    'cubiccapacity', 'kilowatts', 'Cylinders']
    
    available_numeric_cols = [col for col in numeric_cols if col in df.columns]
    
    for col in available_numeric_cols:
        plt.figure(figsize=(7,4))
        sns.histplot(df[col].dropna(), kde=True)
        plt.title(f'Distribution of {col}')
        plt.savefig(f"{plot_dir}/{col}_hist.png")
        plt.close()

# ----------------------------
# 4. Bivariate Analysis
# ----------------------------
def bivariate_analysis(df, plot_dir="plots"):
    """Example bivariate analysis: Loss Ratio by Province."""
    create_folder(plot_dir)
    
    if 'TotalPremium' in df.columns and 'TotalClaims' in df.columns and 'Province' in df.columns:
        df['LossRatio'] = df['TotalClaims'] / df['TotalPremium']
        plt.figure(figsize=(12,6))
        sns.boxplot(data=df, x='Province', y='LossRatio')
        plt.xticks(rotation=45)
        plt.title("Loss Ratio by Province")
        plt.tight_layout()
        plt.savefig(f"{plot_dir}/lossratio_by_province.png")
        plt.close()
    else:
        print("Required columns for bivariate analysis not found.")

# ----------------------------
# 5. Correlation Heatmap
# ----------------------------
def correlation_heatmap(df, plot_dir="plots"):
    """Plot correlation heatmap for numeric columns."""
    create_folder(plot_dir)
    
    numeric_cols = ['TotalPremium', 'TotalClaims', 'CustomValueEstimate', 
                    'SumInsured', 'CalculatedPremiumPerTerm', 
                    'cubiccapacity', 'kilowatts', 'Cylinders']
    
    available_numeric_cols = [col for col in numeric_cols if col in df.columns]
    
    if available_numeric_cols:
        plt.figure(figsize=(10,8))
        sns.heatmap(df[available_numeric_cols].corr(), annot=True, cmap='coolwarm')
        plt.title("Correlation Heatmap")
        plt.tight_layout()
        plt.savefig(f"{plot_dir}/correlation_heatmap.png")
        plt.close()
    else:
        print("No numeric columns found for correlation heatmap.")
