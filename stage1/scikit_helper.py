import sklearn

from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import confusion_matrix,  fbeta_score
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
import numpy as np
from constants import labels
import pandas
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

# Declare all models globally to use them across training and testing phase
logistic_regression_classifier = LogisticRegression()
linear_regression_classifier = LinearRegression()
decision_tree_classifier = DecisionTreeClassifier()
svm_classifier = svm.SVC(kernel='linear', C=1)
random_forrest_classifier = RandomForestClassifier(n_jobs=2, random_state=0)

# Declare all scores globally to use them across training and testing phase
decision_tree_scores, random_forrest_scores, svm_classifier_scores = 0, 0, 0
linear_regression_classifier_scores, logistic_regression_classifier_scores = 0, 0


def run_training_phase(global_data_frames):
    data_frame = pandas.DataFrame.from_records(global_data_frames, columns=labels)
    features = data_frame.columns[1:-1]

    global decision_tree_scores, random_forrest_scores, svm_classifier_scores
    global linear_regression_classifier_scores, logistic_regression_classifier_scores

    decision_tree_scores = cross_val_score(
        decision_tree_classifier, data_frame[features], data_frame['Class'], cv=10)
    decision_tree_classifier.fit(data_frame[features],
                                 data_frame['Class'])
    random_forrest_scores = cross_val_score(
        random_forrest_classifier, data_frame[features], data_frame['Class'], cv=10)

    svm_classifier_scores = cross_val_score(
        svm_classifier, data_frame[features], data_frame['Class'], cv=10)

    linear_regression_classifier_scores = cross_val_score(
        linear_regression_classifier, data_frame[features], data_frame['Class'], cv=10)

    logistic_regression_classifier_scores = cross_val_score(
        logistic_regression_classifier, data_frame[features], data_frame['Class'], cv=10)


def run_testing_phase(global_test_data_frames):
    test_data_frame = pandas.DataFrame.from_records(global_test_data_frames, columns=labels)
    test_features = test_data_frame.columns[1:-1]

    # Prediction for Decision Tree

    print("\n\n************************Decision Tree Classifier*******************************\n")
    decision_tree_classifier.fit(test_data_frame[test_features], test_data_frame['Class'])
    decision_tree_classifier_pred = decision_tree_classifier.predict(test_data_frame[test_features])
    print("Decision_tree_scores = " + str(np.mean(decision_tree_scores)))
    print("Precision Score = " + str(
        sklearn.metrics.precision_score(test_data_frame['Class'], decision_tree_classifier_pred)))
    print(
        "Recall Score = " + str(sklearn.metrics.recall_score(test_data_frame['Class'], decision_tree_classifier_pred)))
    dTFScore = fbeta_score(test_data_frame['Class'], decision_tree_classifier_pred, beta= 0.5)
    print("Decision Tree F1 Score = " + str(dTFScore))
    CM = confusion_matrix(test_data_frame['Class'], decision_tree_classifier_pred)

    # Prediction for Random forest

    print("\n\n************************Random forest Classifier*******************************\n")
    random_forrest_classifier.fit(test_data_frame[test_features], test_data_frame['Class'])
    random_forest_classifier_pred = random_forrest_classifier.predict(test_data_frame[test_features])
    print("Random forest scores = " + str(np.mean(random_forrest_scores)))
    print("Precision Score = " + str(sklearn.metrics.precision_score(
        test_data_frame['Class'], random_forest_classifier_pred)))
    print(
        "Recall Score = " + str(sklearn.metrics.recall_score(test_data_frame['Class'],
                                                             random_forest_classifier_pred)))
    dTFScore = fbeta_score(test_data_frame['Class'],
                           random_forest_classifier_pred, beta=0.5)
    print("Random Forest F1 Score = " + str(dTFScore))

    # Prediction for SVM classifier score
    print(
        "\n\n************************Support Vector Machine(SVM) Classifier*******************************\n")
    svm_classifier.fit(test_data_frame[test_features],
                       test_data_frame['Class'])
    svm_pred = svm_classifier.predict(
        test_data_frame[test_features])
    print("SVM scores = " + str(np.mean(svm_classifier_scores)))
    print("Precision Score = " + str(sklearn.metrics.precision_score(
        test_data_frame['Class'], svm_pred)))
    print(
        "Recall Score = " + str(sklearn.metrics.recall_score(test_data_frame['Class'],
                                                             svm_pred)))
    dTFScore = fbeta_score(test_data_frame['Class'],
                           svm_pred, beta=0.5)
    print("SVM F1 Score = " + str(dTFScore))

    # Prediction for linear regression classifier

    print(
        "\n\n************************Linear Regression Classifier*******************************\n")
    linear_regression_classifier.fit(test_data_frame[test_features],
                                     test_data_frame['Class'])
    linear_regression_pred = linear_regression_classifier.predict(
        test_data_frame[test_features])
    print("Linear Regression Classifier scores = " + str(np.mean(linear_regression_classifier_scores)))

    # Prediction for Logistic regression classifier

    print(
        "\n\n************************Logistic Regression Classifier*******************************\n")
    logistic_regression_classifier.fit(test_data_frame[test_features],
                                       test_data_frame['Class'])
    logistic_regression_pred = logistic_regression_classifier.predict(
        test_data_frame[test_features])
    print("Logistic Regression Classifier scores = " + str(np.mean(
        logistic_regression_classifier_scores)))

    # TN = CM[0][0]
    # FN = CM[1][0]
    # TP = CM[1][1]
    # FP = CM[0][1]
    #
    # print("False positive " + str(FP))
    # print("False negative " + str(FN))
    #
    # for i,prediction in enumerate(decision_tree_classifier_pred):
    #     if test_data_frame['Class'][i] != prediction and prediction==1:
    #         print(str(prediction) + " " + test_data_frame['Word'][i])
