# [Location Extractor from Text Documents](https://sites.google.com/view/data-science-project/home)

## Stage 1 WebPage 
[https://sites.google.com/view/data-science-project/home/stage-1](https://sites.google.com/view/data-science-project/home/stage-1)

## Approach
1. Collected 300 text documents containing well-formed sentences. Documents contain only plain text in English.
2. Decided LOCATIONs as the entity type which we will extract from these documents.
3. Marked up the mentions of locations in these documents using <loc> tags. Example <loc>WASHINGTON</loc>
4. Splitted the tagged set into a set I of 200 documents and a set J of the remaining 100 documents.
    * The set I is used for development (dev set), and 
    * the set J is used for reporting the accuracy of the extractor (the test set).
5. Performed cross-validation (CV) on the set I to select the best classifier M.
    * We considered the following classifiers: decision tree, random forest, support vector machine, linear regression, and logistic regression.
6. Improve the accuracy of M, and redo CV on set I to check if best classifier changes.
7. Let final resulting classifier be X. Apply X to the test set J to meet the accuracy requirement (90% P and 60% R).
8. (Not Applicable) Add rule-based postprocessing if required
9. Apply X and the postprocessing rules to the test set J and report its accuracy.


## Project Website
[https://sites.google.com/view/data-science-project/home](https://sites.google.com/view/data-science-project/home)

## Authors

* **[Anshu Verma](https://github.com/anshuv99)**
* **[Srujana](https://github.com/SrujanaN)**
* **[Arpit Jain](https://github.com/calvincodes)**