### 📊 Dataset Overview

#### About the Dataset

This project uses a dataset sourced from Kaggle, which focuses on ECG signal features for arrhythmia classification. The original dataset was derived from the MIT-BIH Arrhythmia Dataset hosted on PhysioNet. It contains features extracted from two-lead ECG signals (lead II and lead V5), focusing on detecting cardiac arrhythmias. The dataset includes programmatically extracted features critical for distinguishing regular and irregular heartbeats.

#### 🔗 Dataset Sources

The dataset includes features from four ECG arrhythmia datasets:

1. MIT-BIH Supraventricular Arrhythmia Database
2. MIT-BIH Arrhythmia Database
3. St. Petersburg INCART 12-lead Arrhythmia Database
4. Sudden Cardiac Death Holter Database

> **Kaggle Dataset**: [ECG Arrhythmia Classification Dataset](https://www.kaggle.com/datasets/sadmansakib7/ecg-arrhythmia-classification-dataset/data)

> **Original PhysioNet Dataset**: [MIT-BIH Arrhythmia Dataset](https://physionet.org/content/mitdb/1.0.0/)

#### 🎯 Target Column

The `type` column classifies heartbeats into:

- **N**: Normal beats
- **S**: Supraventricular ectopic beats
- **V**: Ventricular ectopic beats
- **F**: Fusion beats
- **Q**: Unknown beats

#### 🧬 Column Descriptions

Below is a detailed description of the columns included in the dataset:

| Column Name           | Description                                                                                      |
| --------------------- | ------------------------------------------------------------------------------------------------ |
| record                | Unique identifier for each patient/subject.                                                      |
| Average RR            | Average R-to-R interval in milliseconds (ms).                                                    |
| RR                    | R-to-R interval in ms.                                                                           |
| Post RR               | Post R-to-R interval in ms.                                                                      |
| PQ Interval           | Time from onset of atrial depolarization to ventricular depolarization (ms).                     |
| QT Interval           | Time from the start of ventricular depolarization to the end of ventricular repolarization (ms). |
| ST Interval           | Duration of ventricular repolarization (ms).                                                     |
| QRS Duration          | Duration of ventricular depolarization (ms).                                                     |
| P peak                | Amplitude of the P wave.                                                                         |
| T peak                | Amplitude of the T wave.                                                                         |
| R peak                | Amplitude of the R wave.                                                                         |
| S peak                | Amplitude of the S wave.                                                                         |
| Q peak                | Amplitude of the Q wave.                                                                         |
| QRS morph feature 0–4 | Morphological features of the QRS complex.                                                       |

#### 🚀 Usage

This dataset is ideal for training machine learning models to classify cardiac arrhythmias. The consistent feature extraction across the datasets ensures comparability and robustness for predictive modeling.

#### 📚 Citation

1. **Original Dataset Paper**: [PhysioBank, PhysioToolkit, and PhysioNet: Components of a New Research Resource for Complex Physiologic Signals](http://ecg.mit.edu/george/publications/mitdb-embs-2001.pdf).
2. **Feature Extraction and Methodology Paper**: [Harnessing Artificial Intelligence for Secure ECG Analytics at the Edge for Cardiac Arrhythmia Classification](https://www.taylorfrancis.com/chapters/edit/10.1201/9781003028635-11/harnessing-artificial-intelligence-secure-ecg-analytics-edge-cardiac-arrhythmia-classification-sadman-sakib-mostafa-fouda-zubair-md-fadlullah).
