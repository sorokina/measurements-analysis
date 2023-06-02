**_General Info_**

This repository is meant to be an app that makes 
data transformation and cleansing.
****
An app imports raw Data in CSV format and makes some Data manipulations. 
As an output app creates a CSV File with aggregated and analysed data. 

How to build and run the Docker image locally:

```
# docker build -t measurements-analysis .   
```   


```
# docker run -v $(PWD)/data:/mnt/data measurements-analysis
```