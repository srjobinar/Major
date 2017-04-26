import nltk
from nltk.corpus import wordnet as wn, stopwords
from nltk.tokenize import word_tokenize

def algorithm(sent,k):
    #print(wn.synsets("clef")[0].definition())
    text_words=word_tokenize(sent)
    stop_words=set(stopwords.words("english"))
    text_words =list(set(text_words) - set(stop_words))
    #print(text_words)
    #print(wn.synsets("car")[0].lemmas()[0].name())


            
    syn = []
    for i, val in enumerate(text_words):
        syn.extend(wn.synsets(val))
        
    syn_noun = []
    for i, val in enumerate(text_words):
        syn_noun.extend(wn.synsets(val, pos=wn.NOUN))   

    flag = 0
    output_lesk = {}
    context_words = []

    for i, val in enumerate(syn):
        words=word_tokenize(val.definition())    
        context_words.extend(words)

    context_words = list(set(context_words)-set(stop_words))

    for word in list(wn.all_lemma_names(lang='eng')):
        if len(word) == k and word.isalpha():
            sim = 0   
            for synset in list(wn.synsets(word)):
                def_words = word_tokenize(synset.definition())
                def_words = list(set(def_words)-set(stop_words))
                temp1=set(text_words).intersection(def_words)
                temp2=set(context_words).intersection(def_words)        
                temp1 = len(temp1)/len(text_words)
                temp2 = len(temp2)/len(context_words)
                t = 0.75*temp1 +0.25*temp2
                sim = max(t,sim)
            #if flag == 0:
            #print(sim)
            if sim > 0:
                output_lesk[word] = sim
                          
    lesk = list(sorted(output_lesk, key=output_lesk.__getitem__, reverse = True)) 

    return lesk[:50]
     



