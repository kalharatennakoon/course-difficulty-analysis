# Setup Guide for Course Difficulty Analysis

This guide will help you set up the Course Difficulty Analysis project and upload it to GitHub.

## Prerequisites

- Python 3.7 or higher
- Git installed on your system
- GitHub account
- Jupyter Notebook or JupyterLab

## Local Setup

### 1. Clone or Download the Repository

If you have the project locally:
```bash
cd course-difficulty-analysis
```

### 2. Create Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Download the Dataset

#### Option A: Automatic Download (Recommended)
```bash
# Set up Kaggle API (one-time setup)
pip install kaggle

# Go to https://www.kaggle.com/account
# Click "Create New API Token"
# Save kaggle.json to ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json

# Download dataset
python download_dataset.py
```

#### Option B: Manual Download
1. Visit https://www.kaggle.com/datasets/adilshamim8/turkiye-student-evaluation
2. Click "Download" to get the CSV file
3. Create a `data` folder in the project directory
4. Place `TurkiyeStudentEvaluation.csv` in the `data` folder

### 5. Run the Analysis

```bash
# Start Jupyter Notebook
jupyter notebook course_difficulty_analysis.ipynb

# Or use JupyterLab
jupyter lab course_difficulty_analysis.ipynb
```

## GitHub Repository Setup

### 1. Create GitHub Repository

1. Go to [GitHub](https://github.com)
2. Click "New repository"
3. Name it `course-difficulty-analysis`
4. Choose "Public" or "Private"
5. Don't initialize with README (we already have one)
6. Click "Create repository"

### 2. Upload to GitHub

```bash
# Navigate to your project directory
cd course-difficulty-analysis

# Add GitHub remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/course-difficulty-analysis.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### 3. Verify Upload

1. Go to your GitHub repository
2. Check that all files are uploaded:
   - `README.md`
   - `course_difficulty_analysis.ipynb`
   - `requirements.txt`
   - `download_dataset.py`
   - `.github/workflows/test.yml`
   - `LICENSE`

## Repository Features

### Automated Testing
- GitHub Actions workflow tests the notebook
- Runs on every push and pull request
- Creates sample data for testing

### Documentation
- Comprehensive README with analysis overview
- Setup instructions and dependencies
- Usage examples and citation information

### Dataset Integration
- Kaggle API integration for automatic downloads
- Manual download instructions as fallback
- Sample data generation for testing

## Usage Instructions

### For Researchers
1. Clone the repository
2. Follow setup instructions
3. Download the real dataset using the provided script
4. Run the analysis notebook
5. Modify parameters and methods as needed

### For Students
1. Use as a template for similar educational research
2. Study the statistical methods implemented
3. Adapt the analysis for different datasets
4. Learn about validity, reliability, and normality testing

### For Educators
1. Use as teaching material for statistical analysis
2. Demonstrate proper research methodology
3. Show integration of multiple analytical techniques
4. Example of reproducible research practices

## Troubleshooting

### Common Issues

1. **Kaggle API not working**
   - Ensure kaggle.json is in ~/.kaggle/
   - Check file permissions: `chmod 600 ~/.kaggle/kaggle.json`
   - Verify API token is valid

2. **Missing dependencies**
   - Update pip: `pip install --upgrade pip`
   - Install requirements: `pip install -r requirements.txt`

3. **Notebook won't run**
   - Check Python version (3.7+)
   - Verify all packages are installed
   - Try creating fresh virtual environment

4. **Dataset not found**
   - Check data/TurkiyeStudentEvaluation.csv exists
   - Run download script: `python download_dataset.py`
   - Try manual download from Kaggle

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Citation

If you use this analysis in your research, please cite:

```
Course Difficulty Analysis: Validity, Reliability, and Normality Study
GitHub Repository: https://github.com/YOUR_USERNAME/course-difficulty-analysis
```

Original dataset citation:
```
Gunduz, N. & Fokoue, E. (2013). UCI Machine Learning Repository. 
University of California, Irvine, School of Information and Computer Sciences.
```
