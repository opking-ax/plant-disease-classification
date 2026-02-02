# Plant Disease Classification

## Project Status
In Developement - Week 1: Data Engineering

## Overview
Machine learning system for classifying plant diseases from leaf images using the PlantVillage dataset.

## Datasets
- PlantVillage Dataset - [https://data.mendeley.com/datasets/tywbtsjrjv/1]
- Dataset Size - 54,000 images
- Dataset Classes: 38 different plant disease categories

## Setup Instructions
1. Clone repository: `git clone [URL]`
2. Create virtual environment
3. Install dependencies: `pip install -r requirements.txt`
4. Download data
5. Run EDA: Open `notebooks/01_eda.ipynb`

## Project Structure
```
plant-disease-classification/
    ├── data/
    │   ├── raw/              # Original dataset
    │   └── processed/        # Preprocessed data
    ├── notebooks/
    │   └── 01_eda.ipynb
    ├── src/
    │   └── data/
    │       ├── download.py
    │       └── preprocessing.py
    └──experiments/           # Analysis results
```
## Key Findings (Week 1)
- Total images: ~54,000+
- Classes: 38
- Image dimensions: mostly [224 x 224]

## Current Progress
- [x] Project setup
- [x] Data downloaded and organized
- [x] Data preprocessing pipeline built
- [x] Train/val/test splits created (70/15/15)

## Next Steps
- Build baseline CNN model
- Implement transfer learning
- Set up experiment tracking

