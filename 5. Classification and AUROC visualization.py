from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_predict
from sklearn.pipeline import Pipeline
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
array = read_csv("FCFB-Wrapper.csv")
array.replace("Positive",1, inplace=True)
array.replace("Negative",0, inplace=True)
array.to_csv("Embedded.csv", index=False)
array = read_csv("Embedded.csv").values
array = read_csv("FCFB.csv")
array.replace("Positive",1, inplace=True)
array.replace("Negative",0, inplace=True)
array.to_csv("Classification.csv", index=False)
array = read_csv("Classification.csv").values
X = array[:,:-1]
Y = array[:,-1]
estimators = []
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
estimators.append(('lda', LinearDiscriminantAnalysis()))
lda = Pipeline(estimators)
estimators = []
from sklearn.svm import LinearSVC
estimators.append(('svm', LinearSVC()))
svm = Pipeline(estimators)
estimators = []
estimators.append(('nb', MultinomialNB()))
nb = Pipeline(estimators)
estimators = []
estimators.append(('knn', KNeighborsClassifier()))
knn = Pipeline(estimators)
seed = 7
kfold = KFold(n_splits=10, random_state=seed)
results_lda = cross_val_predict(lda, X, Y, cv=kfold)
results_svm = cross_val_predict(svm, X, Y, cv=kfold)
results_nb = cross_val_predict(nb, X, Y, cv=kfold)
results_knn = cross_val_predict(knn, X, Y, cv=kfold)
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
scores_lda = confusion_matrix(results_lda, Y)
scores_svm = confusion_matrix(results_svm, Y)
scores_nb = confusion_matrix(results_nb, Y)
scores_knn = confusion_matrix(results_knn, Y)
print("===============Linear Discriminant Analysis======================")
list = []
for i in scores_lda[0]:
    list.append(i)
for i in scores_lda[1]:
    list.append(i)
l = ["True Positive", "False Negative", "False Positive", "True Negative"]
print(l)
print(list)
print("Confusion Matrix:",scores_lda)
accuracy = accuracy_score(results_lda, Y)*100
print("Accuracy:",accuracy)
from sklearn.metrics import matthews_corrcoef
print("Matthew's Correlation Coefficient:",matthews_corrcoef(results_lda,Y))
from sklearn import metrics
print("Mean Absolute Error:",metrics.mean_absolute_error(results_lda,Y))
print("Mean Squared Error:",metrics.mean_squared_error(results_lda,Y))
print("AUC:",metrics.roc_auc_score(results_lda,Y))
print("F-Score:",metrics.f1_score(results_lda,Y))
err = ((list[1]+list[2])/(list[0]+list[1]+list[2]+list[3]))
print("Error Rate:",err)
print("True Positive/Sensitivity:",list[0]/(list[0]+list[1]))
print("True Negative/Specificity:",list[3]/(list[3]+list[2]))
print("Positive Predictive Value/Precision:",list[0]/(list[0]+list[2]))
print("False Positive Rate:",list[2]/(list[2]+list[3]))
print("===============Support Vector Machines======================")
list = []
for i in scores_svm[0]:
    list.append(i)
for i in scores_svm[1]:
    list.append(i)
l = ["True Positive", "False Negative", "False Positive", "True Negative"]
print(l)
print(list)
print("Confusion Matrix:",scores_svm)
accuracy = accuracy_score(results_svm, Y)*100
print("Accuracy:",accuracy)
from sklearn.metrics import matthews_corrcoef
print("Matthew's Correlation Coefficient:",matthews_corrcoef(results_svm,Y))
from sklearn import metrics
print("Mean Absolute Error:",metrics.mean_absolute_error(results_svm,Y))
print("Mean Squared Error:",metrics.mean_squared_error(results_svm,Y))
print("AUC:",metrics.roc_auc_score(results_svm,Y))
print("F-Score:",metrics.f1_score(results_svm,Y))
err = ((list[1]+list[2])/(list[0]+list[1]+list[2]+list[3]))
print("Error Rate:",err)
print("True Positive/Sensitivity:",list[0]/(list[0]+list[1]))
print("True Negative/Specificity:",list[3]/(list[3]+list[2]))
print("Positive Predictive Value/Precision:",list[0]/(list[0]+list[2]))
print("False Positive Rate:",list[2]/(list[2]+list[3]))
print("===============Naive Bayes======================")
list = []
for i in scores_nb[0]:
    list.append(i)
for i in scores_nb[1]:
    list.append(i)
l = ["True Positive", "False Negative", "False Positive", "True Negative"]
print(l)
print(list)
print("Confusion Matrix:",scores_nb)
accuracy = accuracy_score(results_nb, Y)*100
print("Accuracy:",accuracy)
from sklearn.metrics import matthews_corrcoef
print("Matthew's Correlation Coefficient:",matthews_corrcoef(results_nb,Y))
from sklearn import metrics
print("Mean Absolute Error:",metrics.mean_absolute_error(results_nb,Y))
print("Mean Squared Error:",metrics.mean_squared_error(results_nb,Y))
print("AUC:",metrics.roc_auc_score(results_nb,Y))
print("F-Score:",metrics.f1_score(results_nb,Y))
err = ((list[1]+list[2])/(list[0]+list[1]+list[2]+list[3]))
print("Error Rate:",err)
print("True Positive/Sensitivity:",list[0]/(list[0]+list[1]))
print("True Negative/Specificity:",list[3]/(list[3]+list[2]))
print("Positive Predictive Value/Precision:",list[0]/(list[0]+list[2]))
print("False Positive Rate:",list[2]/(list[2]+list[3]))
print("===============K-Nearest Neighbor======================")
list = []
for i in scores_knn[0]:
    list.append(i)
for i in scores_knn[1]:
    list.append(i)
l = ["True Positive", "False Negative", "False Positive", "True Negative"]
print(l)
print(list)
print("Confusion Matrix:",scores_knn)
accuracy = accuracy_score(results_knn, Y)*100
print("Accuracy:",accuracy)
from sklearn.metrics import matthews_corrcoef
print("Matthew's Correlation Coefficient:",matthews_corrcoef(results_knn,Y))
from sklearn import metrics
print("Mean Absolute Error:",metrics.mean_absolute_error(results_knn,Y))
print("Mean Squared Error:",metrics.mean_squared_error(results_knn,Y))
print("AUC:",metrics.roc_auc_score(results_knn,Y))
print("F-Score:",metrics.f1_score(results_knn,Y))
err = ((list[1]+list[2])/(list[0]+list[1]+list[2]+list[3]))
print("Error Rate:",err)
print("True Positive/Sensitivity:",list[0]/(list[0]+list[1]))
print("True Negative/Specificity:",list[3]/(list[3]+list[2]))
print("Positive Predictive Value/Precision:",list[0]/(list[0]+list[2]))
print("False Positive Rate:",list[2]/(list[2]+list[3]))
from sklearn.metrics import roc_curve, auc
from matplotlib import pyplot as plt
fpr, tpr, thresholds = roc_curve(results_lda, Y)
roc_auc = auc(fpr, tpr)
lw=2
plt.figure()
plt.plot(fpr, tpr, color='darkorange', lw=1, label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic')
plt.legend(loc="lower right")
plt.show()
