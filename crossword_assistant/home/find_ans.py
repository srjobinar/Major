import nltk
from nltk.corpus import wordnet as wn, stopwords
from nltk.tokenize import word_tokenize


def noun_fn(sent, k):
    text_words = word_tokenize(sent)
    stop_words = set(stopwords.words("english"))
    temp_words = list(set(text_words) - set(stop_words))
    if len(temp_words) != 0:
        text_words = temp_words
    syn = []
    syn_noun = []
    for i, val in enumerate(text_words):
        syn_noun.extend(wn.synsets(val, pos=wn.NOUN))

    for i, val in enumerate(text_words):
        syn.extend(wn.synsets(val))

    output_lesk = {}
    output_noun = {}
    context_words = []

    for i, val in enumerate(syn):
        words = word_tokenize(val.definition())
        context_words.extend(words)

    context_words = list(set(context_words) - set(stop_words))

    for word in list(wn.all_lemma_names(lang='eng')):
        if len(word) == k and word.isalpha():
            sim_noun = 0
            sim = 0
            for synset in list(wn.synsets(word, pos=wn.NOUN)):
                temp = 0
                for i, val in enumerate(syn_noun):
                    temp = temp + synset.path_similarity(val)
                sim_noun = max(temp, sim_noun)

            for synset in list(wn.synsets(word)):
                def_words = word_tokenize(synset.definition())
                def_words = list(set(def_words) - set(stop_words))
                temp1 = set(text_words).intersection(def_words)
                temp2 = set(context_words).intersection(def_words)
                temp1 = len(temp1) / len(text_words)
                temp2 = len(temp2) / len(context_words)
                t = 0.75 * temp1 + 0.25 * temp2
                sim = max(t, sim)
            if sim > 0:
                output_lesk[word] = sim
            if sim_noun > 0:
                output_noun[word] = sim_noun
    nouns = sorted(output_noun, key=output_noun.__getitem__, reverse=True)
    lesk = sorted(output_lesk, key=output_lesk.__getitem__, reverse=True)

    max_nouns = 0
    for w in nouns:
        if output_noun[w] > max_nouns:
            max_nouns = output_noun[w]

    for key, value in output_noun.items():
        output_noun[key] = value / max_nouns

    for w in lesk:
        if not (w in output_noun):
            output_noun[w] = 0
        output_lesk[w] += output_noun[w]
    rank = list(sorted(output_lesk, key=output_lesk.__getitem__, reverse=True))
    return rank[:1000]


def verb_fn(sent, k):
    text_words = word_tokenize(sent)
    stop_words = set(stopwords.words("english"))
    temp_words = list(set(text_words) - set(stop_words))
    if len(temp_words) != 0:
        text_words = temp_words
    syn = []
    syn_verb = []
    for i, val in enumerate(text_words):
        syn_verb.extend(wn.synsets(val, pos=wn.VERB))

    for i, val in enumerate(text_words):
        syn.extend(wn.synsets(val))

    output_lesk = {}
    output_verb = {}
    context_words = []

    for i, val in enumerate(syn):
        words = word_tokenize(val.definition())
        context_words.extend(words)

    context_words = list(set(context_words) - set(stop_words))

    for word in list(wn.all_lemma_names(lang='eng')):
        if len(word) == k and word.isalpha():
            sim_verb = 0
            sim = 0
            for synset in list(wn.synsets(word, pos=wn.VERB)):
                temp = 0
                for i, val in enumerate(syn_verb):
                    temp = temp + synset.path_similarity(val)
                sim_verb = max(temp, sim_verb)

            for synset in list(wn.synsets(word)):
                def_words = word_tokenize(synset.definition())
                def_words = list(set(def_words) - set(stop_words))
                temp1 = set(text_words).intersection(def_words)
                temp2 = set(context_words).intersection(def_words)
                temp1 = len(temp1) / len(text_words)
                temp2 = len(temp2) / len(context_words)
                t = 0.75 * temp1 + 0.25 * temp2
                sim = max(t, sim)
            if sim > 0:
                output_lesk[word] = sim
            if sim_verb > 0:
                output_verb[word] = sim_verb
    verbs = sorted(output_verb, key=output_verb.__getitem__, reverse=True)
    lesk = sorted(output_lesk, key=output_lesk.__getitem__, reverse=True)

    max_verbs = 0
    for w in verbs:
        if output_verb[w] > max_verbs:
            max_verbs = output_verb[w]

    for key, value in output_verb.items():
        output_verb[key] = value / max_verbs

    for w in lesk:
        if not (w in output_verb):
            output_verb[w] = 0
        output_lesk[w] += output_verb[w]
    rank = list(sorted(output_lesk, key=output_lesk.__getitem__, reverse=True))
    return rank[:1000]



def adj_fn(sent, k):
    text_words = word_tokenize(sent)
    stop_words = set(stopwords.words("english"))
    temp_words = list(set(text_words) - set(stop_words))
    if len(temp_words) != 0:
        text_words = temp_words
    syn = []
    syn_adj = []
    for i, val in enumerate(text_words):
        syn_adj.extend(wn.synsets(val, pos=wn.ADJ))

    for i, val in enumerate(text_words):
        syn.extend(wn.synsets(val))

    output_lesk = {}
    output_adj = {}
    context_words = []

    for i, val in enumerate(syn):
        words = word_tokenize(val.definition())
        context_words.extend(words)

    context_words = list(set(context_words) - set(stop_words))

    for word in list(wn.all_lemma_names(lang='eng')):
        if len(word) == k and word.isalpha():
            sim_adj = 0
            sim = 0
            for synset in list(wn.synsets(word, pos=wn.ADJ)):
                temp = 0
                for i, val in enumerate(syn_adj):
                    if synset.path_similarity(val):
                        temp = temp + synset.path_similarity(val)
                sim_adj = max(temp, sim_adj)

            for synset in list(wn.synsets(word)):
                def_words = word_tokenize(synset.definition())
                def_words = list(set(def_words) - set(stop_words))
                temp1 = set(text_words).intersection(def_words)
                temp2 = set(context_words).intersection(def_words)
                temp1 = len(temp1) / len(text_words)
                temp2 = len(temp2) / len(context_words)
                t = 0.75 * temp1 + 0.25 * temp2
                sim = max(t, sim)
            if sim > 0:
                output_lesk[word] = sim
            if sim_adj > 0:
                output_adj[word] = sim_adj
    adjs = sorted(output_adj, key=output_adj.__getitem__, reverse=True)
    lesk = sorted(output_lesk, key=output_lesk.__getitem__, reverse=True)

    max_adjs = 0
    for w in adjs:
        if output_adj[w] > max_adjs:
            max_adjs = output_adj[w]

    for key, value in output_adj.items():
        output_adj[key] = value / max_adjs

    for w in lesk:
        if not (w in output_adj):
            output_adj[w] = 0
        output_lesk[w] += output_adj[w]
    rank = list(sorted(output_lesk, key=output_lesk.__getitem__, reverse=True))
    return rank[:1000]
def dont_know_fn(sent, k):
    text_words = word_tokenize(sent)
    stop_words = set(stopwords.words("english"))
    temp_words = list(set(text_words) - set(stop_words))
    if len(temp_words) != 0:
        text_words = temp_words
    syn = []
    for i, val in enumerate(text_words):
        syn.extend(wn.synsets(val))

    syn_verb = []
    for i, val in enumerate(text_words):
        syn_verb.extend(wn.synsets(val, pos=wn.VERB))

    syn_noun = []
    for i, val in enumerate(text_words):
        syn_noun.extend(wn.synsets(val, pos=wn.NOUN))

    syn_adj = []
    for i, val in enumerate(text_words):
        syn_adj.extend(wn.synsets(val, pos=wn.ADJ))


    flag = 0
    output_verb = {}
    output_noun = {}
    output_adj = {}
    output_lesk = {}
    context_words = []

    for i, val in enumerate(syn):
        words = word_tokenize(val.definition())
        context_words.extend(words)

    context_words = list(set(context_words) - set(stop_words))

    for word in list(wn.all_lemma_names(lang='eng')):
        if len(word) == k and word.isalpha():
            sim_verb = 0
            sim_noun = 0
            sim_adj = 0
            sim = 0
            for synset in list(wn.synsets(word, pos=wn.VERB)):
                temp = 0
                for i, val in enumerate(syn_verb):
                    sim_verb = sim_verb + synset.path_similarity(val)
                sim_verb = max(temp, sim_verb)
            for synset in list(wn.synsets(word, pos=wn.NOUN)):
                temp = 0
                for i, val in enumerate(syn_noun):
                    temp = temp + synset.path_similarity(val)
                sim_noun = max(temp, sim_noun)
            for synset in list(wn.synsets(word, pos=wn.ADJ)):
                temp = 0
                for i, val in enumerate(syn_adj):
                    if synset.path_similarity(val):
                        temp = temp + synset.path_similarity(val)
                sim_adj = max(temp, sim_adj)
            for synset in list(wn.synsets(word)):
                def_words = word_tokenize(synset.definition())
                def_words = list(set(def_words) - set(stop_words))
                temp1 = set(text_words).intersection(def_words)
                temp2 = set(context_words).intersection(def_words)
                temp1 = len(temp1) / len(text_words)
                temp2 = len(temp2) / len(context_words)
                t = 0.75 * temp1 + 0.25 * temp2
                sim = max(t, sim)

            if sim > 0:
                output_lesk[word] = sim
            if sim_verb > 0:
                output_verb[word] = sim_verb
            if sim_noun > 0:
                output_noun[word] = sim_noun

    verbs = sorted(output_verb, key=output_verb.__getitem__, reverse=True)
    nouns = sorted(output_noun, key=output_noun.__getitem__, reverse=True)
    adjs = sorted(output_adj, key=output_adj.__getitem__, reverse=True)
    lesk = sorted(output_lesk, key=output_lesk.__getitem__, reverse=True)
    max_verbs = 0
    for w in verbs:
        if output_verb[w] > max_verbs:
            max_verbs = output_verb[w]

    for key, value in output_verb.items():
        output_verb[key] = value / max_verbs

    max_nouns = 0
    for w in nouns:
        if output_noun[w] > max_nouns:
            max_nouns = output_noun[w]

    for key, value in output_noun.items():
        output_noun[key] = value / max_nouns

    max_adjs = 0
    for w in adjs:
        if output_adj[w] > max_adjs:
            max_adjs = output_adj[w]

    for key, value in output_adj.items():
        output_adj[key] = value / max_adjs

    tot_rank = dict(output_verb, **output_noun)
    tot_rank = {k: max(i for i in (output_verb.get(k), output_noun.get(k)) if i) for k in
                output_verb.keys() | output_noun}

    for w in lesk:
        if not (w in tot_rank):
            tot_rank[w] = 0
        tot_rank[w] += output_lesk[w]

    rank = sorted(tot_rank, key=tot_rank.__getitem__, reverse=True)

    flag = 0
    # for w in rank:
    #    flag = flag + 1
    #   if flag > 50:
    #      break
    # print(w,tot_rank[w])
    # print(rank[:300])
    return rank[:1000]
