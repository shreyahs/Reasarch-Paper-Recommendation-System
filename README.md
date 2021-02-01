# Research Paper Recommendation System

We have web scraped research papers from arxiv.org and generated three pickel files namely papers.pkl , student_mapping.pkl and students.pkl which consists of data related to papers,student mappings with papers and user data respectively.After getting the data, we have performed Data cleaning and removed missing values as well as duplicate values by dropping certain rows or columns.

The cleaned data is then used for building a recommendation system. In our recommendation system, we have concatenated summary and title of all the papers and then performed Hybrid recommendation method by first filtering the recommendatiuons using  collaborative filtering and then filtering them further using content-based filtering.

# Collaborative Filtering:
In collaborative filtering, as we have already have user mappings with their past referred papers, we can calculate the user similarity by using the mappings. The maximum of most common papers of a user1 with all other users is found and then the remaining papers from the user2 is recommended to user1.

For example ,The recommendations for a user with user id '621741617' can be seen below.
```
paper_id  11909 title  The Wall and The Ball: A Study of Domain Referent Spreadsheet Errors category  HC
paper_id  12333 title  HTTP Mailbox - Asynchronous RESTful Communication category  SE
paper_id  10724 title  CrashScope: A Practical Tool for Automated Testing of Android
  Applications category  SE
paper_id  9503 title  Hierarchical Variability Modeling for Software Architectures category  SE
paper_id  10156 title  Software Architecture Decision-Making Practices and Challenges: An
  Industrial Case Study category  SE
paper_id  9784 title  Service-Oriented Architecture in Industrial Automation Systems - The
  case of IEC 61499: A Review category  SE
paper_id  8844 title  Ontology for Mobile Phone Operating Systems category  SE
paper_id  8312 title  EuSpRIG 2006 Commercial Spreadsheet Review category  SE
paper_id  8823 title  Towards a better understanding of testing if conditionals category  SE
paper_id  8423 title  Software Components for Web Services category  SE
paper_id  8809 title  Examining the Impact of Platform Properties on Quality Attributes category  SE
```

# Content-Based Filtering:
In content based filtering , We have only considered summary of all the papers which can be used for recommendation.So, the data is tokenized in the form of words by removing stopwords and then performing stemming on the data. The resultant preprocessed data is then vectorized using TF-IDF vectorization and Tf, Idf vectors for all the papers are generated. The user query is also tokenized and Tf-Idf vector is generated. The similairty between user query and papers is then found by using cosine similarity between Tf-Idf vectors of user query and papers. In this way, Top-n papers are recommended based on the similarity scores of query and the papers in the data.

Top 10 recommendations when query is taken as 'Neural Network' is shown below.
```
0.22444918745810566 Node Splitting: A Scheme for Generating Upper Bounds in Bayesian
  Networks
0.15387485618504526 Fuzzy Knowledge Representation Based on Possibilistic and Necessary
  Bayesian Networks
0.09215785317293737 On Quantified Linguistic Approximation
0.09059282070553476 Fages' Theorem and Answer Set Programming
0.0874780245066129 Generalization of Clauses under Implication
0.07882219702547631 The Causal Topography of Cognition
0.07426812326231409 DES: a Challenge Problem for Nonmonotonic Reasoning Systems
0.07156792630093642 Vector-space Analysis of Belief-state Approximation for POMDPs
0.06582107431391004 Value-Directed Sampling Methods for POMDPs
0.054169332929043475 Scientific Collaborations: principles of WikiBridge Design
```

# Hybrid Recommendation system:

In Hybrid RS, The result from collaborative filtering is then fed to the content based filtering model as an argument. So, the recommendations from the collaborative filtering are further filtered using cosine similarity of the user query and the sumamry of the papers.

# Deep Learning Recommendation system:

In deep learning approach, the dataset is split into train and test model. The model learns hidden features from historic data and gives recommendations.
Top 10 recommendations when the query is 'Dynamic Benchmarking' is shown below:
```
2297 AI Plan Recognition in Stories and in Life
6470 NE Guided macro-mutation in a graded energy based genetic algorithm for protein structure prediction
11096 SE Efficiently Manifesting Asynchronous Programming Errors in Android Apps
8206 SE IceCube's Development Environment
1081 AI Decision-Theoretic Planning with non-Markovian Rewards
14552 DB Annex: Radon - Rapid Discovery of Topological Relations
1380 AI Methods for computing state similarity in Markov Decision Processes
6358 CV Comparisons of wavelet functions in QRS signal to noise ratio enhancement and detection accuracy
2922 AI An argumentation system for reasoning with conflict-minimal paraconsistent ALC
2674 AI A Computational Model of Two Cognitive Transitions Underlying Cultural Evolution
```

