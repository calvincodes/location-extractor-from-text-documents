import sklearn

from sklearn import svm, metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
import numpy as np
from constants import labels
from sklearn.metrics import classification_report, confusion_matrix
import pandas
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


def train_all_models(global_data_frames, global_test_data_frames):

    data_frame = pandas.DataFrame.from_records(global_data_frames, columns=labels)
    features = data_frame.columns[1:-1]

    test_data_frame = pandas.DataFrame.from_records(global_test_data_frames, columns=labels)
    test_features = test_data_frame.columns[1:-1]

    dict = {1:0.7, 0:0.3}
    decision_tree_classifier = DecisionTreeClassifier()
    # decision_tree_classifier = DecisionTreeClassifier(
        # class_weight={1: 0.3, 0: 0.7})
    # decision_tree_classifier = DecisionTreeClassifier(
    #     class_weight='balanced')
    decision_tree_classifier = DecisionTreeClassifier()
    decision_tree_scores = cross_val_score(
        decision_tree_classifier, data_frame[features], data_frame['Class'], cv=10)
    average_decision_tree_score = np.mean(decision_tree_scores)
    print("decision_tree_scores = " + str(average_decision_tree_score))

    random_forrest_classifier = RandomForestClassifier(n_jobs=2, random_state=0)
    random_forrest_scores = cross_val_score(
        random_forrest_classifier, data_frame[features], data_frame['Class'], cv=10)
    print("random_forrest_scores = " + str(sum(random_forrest_scores) / 10))

    svm_classifier = svm.SVC(kernel='linear', C=1)
    svm_classifier_scores = cross_val_score(
        svm_classifier, data_frame[features], data_frame['Class'], cv=10)
    print("svm_classifier_scores  = " + str(sum(svm_classifier_scores) / 10))

    linear_regression_classifier = LinearRegression()
    linear_regression_classifier_scores = cross_val_score(
        linear_regression_classifier, data_frame[features], data_frame['Class'], cv=10)
    print("linear_regression_classifier_scores = " + str(sum(linear_regression_classifier_scores) / 10))

    logistic_regression_classifier = LogisticRegression()
    logistic_regression_classifier_scores = cross_val_score(
        logistic_regression_classifier, data_frame[features], data_frame['Class'], cv=10)
    print("logistic_regression_classifier_scores = " + str(sum(logistic_regression_classifier_scores) / 10))

    decision_tree_classifier.fit(test_data_frame[test_features], test_data_frame['Class'])
    decision_tree_classifier_pred = decision_tree_classifier.predict(test_data_frame[test_features])
    print (sklearn.metrics.precision_score(test_data_frame['Class'], decision_tree_classifier_pred))
    print (sklearn.metrics.recall_score(test_data_frame['Class'], decision_tree_classifier_pred))
