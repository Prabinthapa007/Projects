# Netflix Clustering And Recommendation System

## Introduction
Netflix is a subscription-based streaming service that offers a wide range of TV series, documentaries, feature films, and games. With over 200 million subscribers across 190+ countries, Netflix has become the leading streaming service globally. Originally launched in 1997 as a DVD rental service with a per-rental fee, Netflix transitioned to an online subscription service in 1999. By 2000, Netflix had implemented a personalized movie recommendation system, utilizing algorithms to predict individual movie preferences based on previous rental data. This project focuses on clustering Netflix data and developing a recommendation system.

## Methods
### Dataset
The dataset used contains 8,807 records with 12 attributes, aiming to build a recommendation system for similar content based on user preferences.

### Models Used
Three clustering models were employed:
- Partition Based Clustering
- Balanced Iterative Reducing and Clustering using Hierarchies (BIRCH)
- Agglomerative Hierarchical Clustering

## Findings
- **Exploratory Data Analysis (EDA):** Netflix offers more movies than TV shows. There was growth in content from 2013 to 2019, followed by a decline due to COVID-19. The USA has the most content, with peaks in content addition in July and December. Content is aimed at mature audiences, teenagers, and general audiences.
- **Data Cleaning:** Null values were addressed to ensure consistency and accuracy in the dataset.
- **Text Preprocessing:** Tokenization with TweetTokenizer and vectorization with TF-IDF Vectorizer were performed, along with Dimensionality Reduction capturing 3300 components.
- **Clustering:** 
  - Partition Based Clustering: Optimal number of clusters was 4, determined using elbow method and silhouette score analysis.
  - BIRCH: No clusters were found due to points being assigned to wrong clusters.
  - Agglomerative Hierarchical Clustering: Optimal number of clusters was 13, determined by visualizing the dendrogram.
- **Recommendation System:** A content-based recommendation system was developed using a similarity matrix based on cosine similarity. The system suggests 10 movies or TV shows similar to those the user has previously watched.

**Note:** For detailed implementation and results, refer to the project files.
