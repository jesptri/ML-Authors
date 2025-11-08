# Victorian Author Attribution using Machine Learning

**Authors:** Tom BOISSE & Jules ESPINOUX

---

## Project Overview

This project implements machine learning algorithms to predict authorship of text excerpts from Victorian-era novelists. Using the Gungor 2018 Victorian Author Attribution dataset, we train and evaluate various classifiers to identify which of 50 different authors wrote a given text passage.

The main challenge addressed is transforming unstructured text data into meaningful numerical representations while preserving linguistic patterns and stylistic features that characterize each author's writing.

---

## Objectives

- **Authorship Attribution:** Predict which author wrote a text excerpt from 50 Victorian-era novelists
- **Text Vectorization:** Compare different text representation methods (Bag-of-Words, TF-IDF)
- **Classification:** Evaluate multiple ML algorithms (Naive Bayes, SVM) for this multi-class classification problem
- **Author Analysis:** Extract and visualize statistical features of different authors writing styles

---

## Dataset

### Source
**Gungor, A. (2018).** *Fifty Victorian Era Novelists Authorship Attribution Data.* IUPUI University Library.  
DOI: [http://dx.doi.org/10.7912/D2N65J](http://dx.doi.org/10.7912/D2N65J)

---

## Project Structure

```
ML-Authors/
├── CR_be_ML_BOISSE_ESPINOUX.ipynb    # Main notebook with complete analysis
├── main.py                            # Quick model training script
├── tokenizer.py                       # Custom tokenization utilities
├── bow.py                             # Bag-of-Words implementation
├── stats.py                           # Generate author statistics
├── plot_stats.py                      # Visualize author statistics
├── dataset/                           # Data files
├── tokenizer.txt                      # Word-to-index mapping
├── stats.txt                          # Computed author statistics
├── Data Description.pdf               # Additional dataset documentation
└── README.md                          # This file
```

---


### Full Analysis

Open and run the Jupyter notebook for complete analysis:

```bash
jupyter notebook CR_be_ML_BOISSE_ESPINOUX.ipynb
```

The notebook includes:
- Data exploration and visualization
- Multiple vectorization methods (BoW, TF-IDF)
- Multiple classifier comparisons (Naive Bayes, SVM)
- Hyperparameter tuning
- Results analysis and discussion

---

## Methodology

### 1. Text Vectorization

We implemented and compared two approaches:

#### Bag-of-Words (BoW)
- Counts word occurrences in each text
- Creates sparse matrix representation
- Each dimension represents a unique word
- Custom implementation in `bow.py`
- Scikit-learn implementation via `CountVectorizer`

#### TF-IDF (Term Frequency - Inverse Document Frequency)
- Weights words by importance
- TF: frequency of word in document
- IDF: inverse frequency across all documents
- Implemented via `TfidfVectorizer`

### 2. Classification Algorithms

#### Naive Bayes (MultinomialNB)
- Probabilistic classifier
- Assumes feature independence
- Fast training and prediction
- Well-suited for text classification

#### Support Vector Machine (LinearSVC)
- Finds optimal hyperplane separating classes
- Effective in high-dimensional spaces
- Good generalization with proper regularization
- Hyperparameter: C (regularization strength)

---

### Key Findings
*(Based on typical performance patterns for this dataset)*

- TF-IDF generally outperforms simple BoW
- Linear SVC achieves competitive accuracy
- Proper hyperparameter tuning (C parameter) significantly impacts performance
- Some authors are easier to distinguish than others due to distinct writing styles

---

## 🔧 Technical Details

### Data Preprocessing
- Dataset is pre-normalized (no additional preprocessing needed)
- Text already cleaned and standardized
- Consistent 1000-word excerpts

### Feature Engineering
- Vectorizers trained on entire corpus for better vocabulary coverage
- Word frequency-based tokenization
- Sparse matrix representation for memory efficiency

### Implementation Highlights
- Scikit-learn pipelines for clean model composition
- Custom BoW implementation using `scipy.sparse.csr_matrix`
- Efficient word counting with `collections.Counter`

---