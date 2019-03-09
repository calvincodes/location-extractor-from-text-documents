from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier

from constants import labels
import pandas
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


def train_all_models(global_data_frames):

    data_frame = pandas.DataFrame.from_records(global_data_frames, columns=labels)
    features = data_frame.columns[1:len(labels)]

    decision_tree_classifier = DecisionTreeClassifier()
    decision_tree_scores = cross_val_score(
        decision_tree_classifier, data_frame[features], data_frame['Class'], cv=10, scoring='roc_auc')
    print("decision_tree_scores = " + str(sum(decision_tree_scores) / 10))

    random_forrest_classifier = RandomForestClassifier(n_jobs=2, random_state=0)
    random_forrest_scores = cross_val_score(
        random_forrest_classifier, data_frame[features], data_frame['Class'], cv=10, scoring='roc_auc')
    print("random_forrest_scores = " + str(sum(random_forrest_scores) / 10))

    svm_classifier = svm.SVC(kernel='linear', C=1)
    svm_classifier_scores = cross_val_score(
        svm_classifier, data_frame[features], data_frame['Class'], cv=10, scoring='roc_auc')
    print("svm_classifier_scores  = " + str(sum(svm_classifier_scores) / 10))

    linear_regression_classifier = LinearRegression()
    linear_regression_classifier_scores = cross_val_score(
        linear_regression_classifier, data_frame[features], data_frame['Class'], cv=10, scoring='roc_auc')
    print("linear_regression_classifier_scores = " + str(sum(linear_regression_classifier_scores) / 10))

    logistic_regression_classifier = LogisticRegression()
    logistic_regression_classifier_scores = cross_val_score(
        logistic_regression_classifier, data_frame[features], data_frame['Class'], cv=10, scoring='roc_auc')
    print("logistic_regression_classifier_scores = " + str(sum(logistic_regression_classifier_scores) / 10))
