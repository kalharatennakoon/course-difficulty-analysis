#!/usr/bin/env python3
"""
Dataset Download Script for Turkiye Student Evaluation Dataset

This script downloads the dataset from Kaggle and prepares it for analysis.
"""

import os
import sys
import subprocess

def install_kaggle():
    """Install kaggle package if not available"""
    try:
        import kaggle
        return True
    except ImportError:
        print("Installing Kaggle API...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "kaggle"])
            import kaggle
            return True
        except Exception as e:
            print(f"Failed to install Kaggle API: {e}")
            return False

def setup_kaggle_credentials():
    """Check and setup Kaggle API credentials"""
    kaggle_dir = os.path.expanduser("~/.kaggle")
    kaggle_json = os.path.join(kaggle_dir, "kaggle.json")
    
    if not os.path.exists(kaggle_json):
        print("Kaggle credentials not found!")
        print("\nTo set up Kaggle API:")
        print("1. Go to https://www.kaggle.com/account")
        print("2. Click 'Create New API Token'")
        print("3. Save the downloaded kaggle.json to ~/.kaggle/")
        print("4. Run: chmod 600 ~/.kaggle/kaggle.json")
        return False
    
    # Set permissions
    os.chmod(kaggle_json, 0o600)
    return True

def download_dataset():
    """Download the Turkiye Student Evaluation dataset"""
    
    # Create data directory
    os.makedirs('data', exist_ok=True)
    
    # Install kaggle if needed
    if not install_kaggle():
        return False
    
    # Setup credentials
    if not setup_kaggle_credentials():
        print("\nAlternative: Download manually from:")
        print("https://www.kaggle.com/datasets/adilshamim8/turkiye-student-evaluation")
        return False
    
    try:
        import kaggle
        
        print("Downloading Turkiye Student Evaluation dataset...")
        kaggle.api.dataset_download_files(
            'adilshamim8/turkiye-student-evaluation',
            path='data',
            unzip=True
        )
        
        # Verify download
        csv_file = 'data/TurkiyeStudentEvaluation.csv'
        if os.path.exists(csv_file):
            print(f"✓ Dataset downloaded successfully to {csv_file}")
            
            # Show basic info
            import pandas as pd
            df = pd.read_csv(csv_file)
            print(f"Dataset shape: {df.shape}")
            print(f"Columns: {list(df.columns)}")
            return True
        else:
            print("❌ Download completed but file not found")
            return False
            
    except Exception as e:
        print(f"❌ Download failed: {e}")
        print("\nManual download instructions:")
        print("1. Go to https://www.kaggle.com/datasets/adilshamim8/turkiye-student-evaluation")
        print("2. Click 'Download' to get the CSV file")
        print("3. Extract and place TurkiyeStudentEvaluation.csv in the 'data' folder")
        return False

if __name__ == "__main__":
    print("Turkiye Student Evaluation Dataset Download Script")
    print("=" * 50)
    
    if download_dataset():
        print("\n🎉 Setup complete! You can now run the analysis notebook.")
    else:
        print("\n⚠️  Please download the dataset manually and place it in the 'data' folder.")
