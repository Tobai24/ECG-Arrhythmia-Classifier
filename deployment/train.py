import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import mutual_info_classif
from sklearn.impute import SimpleImputer
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import xgboost as xgb
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import roc_curve, auc
from sklearn.preprocessing import label_binarize, LabelEncoder
from sklearn.metrics import accuracy_score, roc_auc_score


data_list = ["../data/INCART_Arrhythmia.csv", "../data/MIT-BIH Arrhythmia Database.csv", "../data/MIT-BIH Supraventricular Arrhythmia Database.csv", ]

dataframes = []

print("Joining the dataset")
for data in data_list:
    doc = pd.read_csv(data)
    dataframes.append(doc)

df = pd.concat(dataframes)

df.reset_index(drop=True)

y = df.type
X = df.drop(columns=['type', 'record'])


print("Spliting the dataset into train, val and test")
X_full_train, X_test, y_full_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

X_full_train = X_full_train.reset_index(drop=True)
y_full_train = y_full_train.reset_index(drop=True)

X_train, X_val, y_train, y_val = train_test_split(
    X_full_train, y_full_train, test_size=0.25, stratify=y_full_train, random_state=42
)

print("Removing outliner")
def detect_outliers_iqr(data, columns):
    outliers = {}
    for col in columns:
        Q1 = data[col].quantile(0.25)
        Q3 = data[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        outliers[col] = data[(data[col] < lower_bound) | (data[col] > upper_bound)]
    return outliers

columns_to_check = ['0_pre-RR', '0_post-RR', '1_pre-RR', '1_post-RR']

outliers = detect_outliers_iqr(X_train, columns_to_check)

# Display the number of outliers in each column
for col, outlier_data in outliers.items():
    print(f"{col}: {len(outlier_data)} outliers detected")

for col, outlier_data in outliers.items():
    X_train = X_train[~X_train.index.isin(outlier_data.index)]
    y_train = y_train[~y_train.index.isin(outlier_data.index)]

print("Encoding the dataset")
label_encoder = LabelEncoder()
y_train_encoded = label_encoder.fit_transform(y_train)
y_val_encoded = label_encoder.transform(y_val)

# Train a Logistic Regression model
print("Training the linear regression model")
logreg = LogisticRegression(max_iter=4000, multi_class='multinomial', solver='lbfgs', class_weight='balanced')
logreg.fit(X_train, y_train_encoded)

# Make predictions on the validation set
y_pred_encoded = logreg.predict(X_val)
logreg_probs = logreg.predict_proba(X_val)  # For probabilities

# Evaluate the model's performance
accuracy = accuracy_score(y_val_encoded, y_pred_encoded)
print(f"Accuracy: {accuracy:.4f}")

# Display detailed classification report
print("Classification Report:")
print(classification_report(y_val_encoded, y_pred_encoded))

# Calculate and display ROC AUC for multiclass
y_val_binarized = label_binarize(y_val_encoded, classes=list(range(5)))
auc_score = roc_auc_score(y_val_binarized, logreg_probs, average="macro", multi_class="ovr")
print(f"Multiclass ROC AUC Score: {auc_score:.4f}")
print("Done")


# Train a Random Forest model
print("Training the Random forest")
rf = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')
rf.fit(X_train, y_train_encoded)

# Make predictions on the validation set
y_pred_encoded = rf.predict(X_val)
rf_probs = rf.predict_proba(X_val)  # For probabilities

# Evaluate the model's performance
accuracy = accuracy_score(y_val_encoded, y_pred_encoded)
print(f"Accuracy: {accuracy:.4f}")

# Display detailed classification report
print("Classification Report:")
print(classification_report(y_val_encoded, y_pred_encoded))

# Calculate and display ROC AUC for multiclass
y_val_binarized = label_binarize(y_val_encoded, classes=list(range(5)))
auc_score = roc_auc_score(y_val_binarized, rf_probs, average="macro", multi_class="ovr")
print(f"Multiclass ROC AUC Score: {auc_score:.4f}")
print("Done")

# Create an XGBoost model instance
print("Training the XGBOOST model")
xgb_model = xgb.XGBClassifier(
    objective='multi:softprob',  
    num_class=5,                
    max_depth=10,                
    learning_rate=0.2,         
    n_estimators=200, 
    colsample_bytree= 0.8,
    subsample= 1.0,
    random_state=42
)

# Fit the model on the training data
xgb_model.fit(X_train, y_train_encoded)

# Make predictions on the validation set
y_pred_encoded = xgb_model.predict(X_val)
xgb_probs = xgb_model.predict_proba(X_val)  # For probabilities

# Evaluate the model's performance
accuracy = accuracy_score(y_val_encoded, y_pred_encoded)
print(f"Accuracy: {accuracy:.4f}")

# Display detailed classification report
print("Classification Report:")
print(classification_report(y_val_encoded, y_pred_encoded))

# Calculate and display ROC AUC for multiclass
y_val_binarized = label_binarize(y_val_encoded, classes=list(range(5)))
auc_score = roc_auc_score(y_val_binarized, xgb_probs, average="macro", multi_class="ovr")
print(f"Multiclass ROC AUC Score: {auc_score:.4f}")
print("done")

print("Saving the model")
with open('model.pkl', 'wb') as f_out:
    pickle.dump(xgb_model, f_out)


