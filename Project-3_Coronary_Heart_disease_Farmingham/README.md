# 10-Year Risk of Future (CHD) Coronary Heart Disease
## For course fulfillment of Data Science and Machine Learning

### Introduction
Coronary Heart Disease is the condition where the major blood vessels supplying the heart are narrowed. The reduced blood flow can cause chest pain and shortness of breath. It is also called coronary artery disease (CAD) or ischemic heart disease. The coronary arteries are responsible for supplying oxygen-rich blood to the heart muscle. 

Risk factor for developing CHD include high blood pressure, high cholesterol, smoking, diabetes, obesity, a family history of CHD. CHD is usually caused by a condition called atherosclerosis, which is the buildup of fatty deposits on the inner walls of the coronary arteries. These plaques can restrict blood flow to the heart muscle, leading to CHD.

The result obtained from the studies showed that the choices of features and learning algorithm directly influences the accuracy and reliability of the proposed system. In this study I a going to test the algorithms accuracy and reliability. 

![alt text](image.png)

### Methods
#### Dataset
The data used in the data is from people of Framingham. The dataset includes over 4,240 records, 16 columns and 15 attributes. The goal of the dataset is to predict whether the patient has 10-year risk of future (CHD) coronary heart disease. Due to data imbalance I used upsampled method.

### Experiments with models
We have trained and tested multiple models on the dataset. We have used the following models:
- Logistic Regression
- Support Vector Classifier
- Random Forest Classifier


Most of the algorithm were sourced from popular open-source library, scikit-learn. I have tunned the hyperparameter using GridSearch.

### Results
The table below shows the report on various models we have tested on the dataset.

| Model Name               | Accuracy | Precision | Recall | F1-Score | TP | FP | TN | FN |
|--------------------------|----------|-----------|--------|----------|------|----|----|----|----|
| Logistic Regression      | 0.678     | 0.677      | 0.682  | 0.679  | 475 | 227 | 470 | 221 |
| Support Vector Classifier | 0.78   | 0.782      | 0.775   | 0.779   | 540 | 150 | 547 | 156 |
| Random Forest Classifier | 0.978    | 0.962     | 0.996   | 0.979   | 693 | 27 | 670 | 03 |

From the above table, we can see that, for the dataset, Random Forest Classifier is the best model to predict the Heart disease.
