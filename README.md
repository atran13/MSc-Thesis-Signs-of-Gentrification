## Signs of Gentrification 
### Analyzing Amsterdam's Storefront Signage with Machine Learning and Street View Imagery
#### MSc Thesis - Master Information Studies: Data Science - University of Amsterdam
*Author: Anh Tran - Supervisor: MSc Tim Alpherts*

![frontman](https://github.com/atran13/MSc-Thesis-Signs-of-Gentrification/assets/117304103/f1619ad9-9bb1-4bf8-802a-be86b9b91758)

Gentrification refers to the process of a neighborhood changing as wealthier residents move in, bringing improvements but displacing existing residents due to rising prices and changing cultures. Studies have pointed out how storefront signage mirrors gentrification: as a communication medium with intentional designs, there are clear differences in signage on gentrified and non-gentrified facades. These qualitative studies, however, were labor-intensive and limited in generalizability, as they were conducted on a few selected neighborhoods, not city-wide. This paper explores the use of computer vision to overcome these limitations, and simultaneously detect gentrification in signage from unseen parts of the city. Trained on street view imagery of Amsterdam, the model learned a city-wide pattern of gentrification, with characteristics similar to what was described in past qualitative research. The model is able to distinguish between gentrified and non-gentrified signage with an F1-score of 0.69. Moreover, the model's output identifies cases where signs did not follow typical patterns - a nuance previous studies did not conclude on. Lastly, the model has the ability to detect the same aesthetics in other areas of the city. While the detection of (non-)gentrification from signage alone are not always accurate, being able to recognize the most prevailing characteristics provides an indication for further investigation.

**Repository content:**
* Code: Text extraction function, model iterations, visualization of classification results
* Data: StreetSwipe data, EDA, OpenStreetMap queries and preprocessing for supporting visualization
* Research report
