# webscraping-and-ml

Problem 2:

1. Why did you choose the particular algorithm?
  The code uses XGBoost algorithm. XGBoost (Extreme Gradient Boosting) is a popular machine learning algorithm for classification and regression tasks. It was likely chosen for its effectiveness in handling a variety of data types and its ability to deliver high predictive accuracy. Some of the reasons for choosing XGBoost might include its robustness, ability to handle missing data, and its capacity to capture complex relationships within the data while preventing overfitting.

2. What are the different tuning methods used for the algorithm?
The code specifies several hyperparameters for the XGBoost classifier. These are parameters that can be tuned to optimize the model's performance. Here are the hyperparameters and their values used in the code:
   - `learning_rate`: 0.1
   - `min_child_weight`: 1
   - `gamma`: 0
   - `max_depth`: 5
   - `n_estimators`: 1000
   - `scale_pos_weight`: 1
   - `subsample`: 0.8
   - `colsample_bytree`: 0.8
   - `nthread`: 4

3. Did you consider any other choice of algorithm? Why or why not?

  Yes, I considered several other algorithms in addition to XGBoost for your classification task. Here's a brief overview of each of these algorithms and potential reasons for considering them:
  
  a. Kernel SVM (Support Vector Machine): Kernel SVM is a powerful algorithm for handling both linear and non-linear classification tasks. It was likely considered due to its flexibility in capturing complex decision boundaries.
  b. Logistic Regression: Logistic regression is a simple and interpretable algorithm, often used as a baseline model. It may have been considered to establish a baseline performance before trying more complex models.
  c. Naive Bayes: Naive Bayes is known for its efficiency and can be particularly useful when dealing with text or categorical data. It might have been considered if the dataset contained such features.
  d. Random Forest Classifier: Random Forest is an ensemble learning method that can handle both classification and regression tasks. It's robust and can handle high-dimensional data, making it a reasonable choice for many scenarios.
  e. Decision Tree Classifier: Decision trees are intuitive and interpretable models. They can be considered as a simple approach to classification, especially when you want to understand the decision-making process.
  f. K Neighbors Classifier (K-Nearest Neighbors): K-NN is a non-parametric algorithm that's easy to understand. It might have been chosen for its simplicity and suitability for some types of data.
  g. Support Vector Machine (SVM): You mentioned SVM again. SVMs are indeed versatile and might be considered due to their strong performance and ability to handle various types of data.

4. What is the accuracy?
   The accuracy is 91.35 % for XGBoost

5. What are the different types of metrics that can be used to evaluate the model?
   There are various metrics that can be used to evaluate the performance of a classification model like the XGBoost classifier. Some common metrics include:
   - Accuracy: Measures the proportion of correctly classified instances.
   - Precision: Measures the number of true positive predictions divided by the total number of positive predictions.
   - Recall: Measures the number of true positive predictions divided by the total number of actual positive instances.
   - F1 Score: Combines precision and recall into a single metric to balance the trade-off between false positives and false negatives.
   - ROC-AUC: Measures the area under the Receiver Operating Characteristic curve, which assesses the model's ability to distinguish between classes.
   - Confusion Matrix: Provides a breakdown of true positives, true negatives, false positives, and false negatives.
   - Log Loss (Cross-Entropy): Measures the uncertainty or information loss associated with the model's predictions.
