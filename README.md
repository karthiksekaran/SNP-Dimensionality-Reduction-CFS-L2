# SNP-Dimensionality-Reduction-CFS-L2

Single Nucleotide Polymorphism, pronounced as (SNIP's) are the genetic variations occurs in any species at any position in the genome. Recent studies revealed that the root cause of complex diseases such as cancer, psychiatric disorders and other heriditary diseases can be identified by tracing the pathyway of changes/mutation occured in some part of genome in a cell. This would be much helpful to diagnose the presence of the disease if the gene biomarkers are discovered. Association between the genetic causes and the growth of the disease provide us many insights to treat the patients with more personalized responsive medications.

The aim of the proposed framework is to identify the gene biomarkers of breast and thyroid cancer from SNP data. The main drawback in SNP data is in its dimension and the format. All the entries in an SNP dataset contains four string values such as {AA, AB, BB, NC (No Call)}. These represents the identity of the nucleotides. The missing values (or) unidentified entries recorded by the sequencing machine can be given as NC. The workflow of the system is briefly explained below.

The proposed work is divided into three modules

1. Preprocessing
  
  1.1 Data Encoding -> Transforming the dataset from {AA,AB,BB,NC} to {11,01,10,00}
  1.2 Redundant Data Elimination -> Removing the features with same column (feature) entries
  1.3 Missing Value Treatment -> Features with more than 10% NC entries are removed from the dataset
  1.4 Data Balancing -> Threshold of 1/3 (1/3 means AA,BB and AB}, if a feature contains entries less than 33%, then the feature is removed

2. Gene Biomarker Selection

  2.1 Correlation based Feature Selection -> Selecting the features with low correlation
  2.2 L2 (Tikhnov Regularization) -> Calculating the rank for the gene features based on the coefficient value of each.
  2.3 Thresholding (Error Rate) -> Choosing the candidate gene subset, where the coefficients are larger than the threshold value
  
3. Classification

  Standard machine learning classifiers (Linear Discriminant Analysis, Naive Bayes, Support Vector Machines and k-Nearest Neighbor)
  
File Information 

This system is developed with Python 3.6.2 (Pycharm + Anaconda Environment), Windows 10 Operating System
  
   1. Data Encoding and Redundancy Elimination.py
   2. Missing Value Treatment and Data Balancing.py
   3. Removal of Redundant Features.py
   4. CFS-L2-Regularization.py
   5. Classification and AUROC visualization.py
   6. SNP-Breast.csv (Identified Gene SNP Biomarkers of Breast Cancer and its chromosome positions)
  As the size of the SNP dataset exceeds the given limit, the link from where the data is scraped to conduct this experiment is given below:
  
  https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE16619
  
To simplify the process of running this code for other users, a basic GUI is developed using WxPython Library. Execute "0.Main_GUI.py" File to view the Components of the Interface
