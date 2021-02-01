#!/usr/bin/env python
# coding: utf-8

# In[54]:


def function(query):
    import pickle
    import nltk
    from nltk.corpus import stopwords
    import string
    import csv
    import pandas as pd
    from nltk.corpus import stopwords
    from nltk.stem.porter import PorterStemmer
    from collections import OrderedDict
    
    with open('papers.pkl', 'rb') as f :
        data = pickle.load(f)
    cols = ['title']+ ['summary']
    df_jobs =data[cols]
    df_jobs.columns = ['title','summary']
    df=df_jobs[:1000]
    summary = df[:1000]["summary"]
    summary_tokens = []
    paper_list=[]
    
    
    porter_stemmer = PorterStemmer()
    
    def tokenize_query(q):
        summ = [char for char in q if char not in string.punctuation]
        summ = ''.join(summ)
        
        word=[word for word in summ.split() if word.lower() not in stopwords.words('english')]
        return [porter_stemmer.stem(word) for word in word]
    query1 = tokenize_query(query)
    
    def tokenize_summary(summary):
        summ = [char for char in summary if char not in string.punctuation]
        summ = ''.join(summ)
        
        word=[word for word in summ.split() if word.lower() not in stopwords.words('english')]
        return[porter_stemmer.stem(word) for word in word]
    
    
     
    for i in df['summary']:
        if len(i) > 10:
            summary_tokens.append(tokenize_summary(i))  
            
    df['summary_tokens'] = pd.Series(summary_tokens)
    diction = dict(zip(df.title, df.summary_tokens))
    
    
    for key,value in diction.items():
        for word in query1:
            if word in value:
                paper_list.append(key)
    
    final_list=list(OrderedDict.fromkeys(paper_list))
    final_list=final_list[:10]
    print("The papers with search query are")

    def opcsv(print_list):
        with open('search.csv', 'w') as csvfile:
            fieldnames = ['papers_title']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for title in print_list:
                writer.writerow({'papers_title': title})

    opcsv(final_list)
    return final_list

                


# In[55]:


function('boolean occasion return')


# In[ ]:




