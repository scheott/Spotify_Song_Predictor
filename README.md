# Spotify Song Predictor
## Introduction
I was looking for an interesting project to do and stumbled upon a dataset of 35,000 songs with multiple different features about each. I was immediatly hooked, I have a strong interest in music and listen to so many different kinds of music I just had to utilize this dataset. My goal for this project was to predict songs that I would enjoy using the feautres in this dataset based on my past liked songs. There is one main problem with this project and that is the dataset I built and the models I'm using would assume that I have listened to all 35,000 songs in the dataset due to my liked songs being a part of the dataset, this is untrue but for the sake of the project I kept even the songs I havn't listened to in the dataset

## Data Exploration / Feature Engineering
The first thing I did was get all my liked songs from spotify, and joined those songs with the data set. There wasn't anything too interesting going on in the data exploration portion of the project although it was interesting to see that a majority of my liked songs were lower and valence and lower in duration. Going along with this, there wasn't room for much feautre engineering as well due to each feature being distinct. I did drop most of the genres I would never listen too though. 

## Modeling
This was a binary classification problem and I wanted to see the results of multiple different models. I used Support Vector Classification, XGBoost, Gaussian Naive Bayes, Logistic Regression, Decision Tree, and Random Forest. XGBoost has the best accuracy, but I chose to go with Decision Tree due to the fact that it had higher cardinality in the predictions of new songs.

## Making the playlist
Predicting on the dataset of the 35,000 songs, I made a genre csv of the predicted like songs for my most listened to genres, Rap, Country, and Rock. I used Spotipy which is a Python library for the Spotify Web API, using this I coded a playlist for all three genres on my spotify account.

## Conclusion
In conlcusion, this project helped me gain a lot of confidence in classification and helped me find a lot of new songs I enjoy. In the future when I get my extended listening history, I'm going to come back and make the initial training dataset more accurate by putting only songs I have listened to in it. Below is what one of the playlist made looks like

![alt text](https://github.com/scheott/Spotify_Song_Predictor/blob/main/Screenshot%202023-02-05%20220729.png)

### Thanks for taking a look!
