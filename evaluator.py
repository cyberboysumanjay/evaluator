from gensim.models.doc2vec import Doc2Vec
from nltk.tokenize import word_tokenize
import questions

usernames=questions.usernames

#to find the vector of a document which is not in training data
def generate_score(model_number,answer,question_number):
    model= Doc2Vec.load(model_number)
    #print(test_answer)
    test_data = word_tokenize(answer.lower())
    v1 = model.infer_vector(test_data)
    similar_doc = model.docvecs.most_similar([v1])

    l=[]
    for mark in similar_doc:
        l.append(mark[1])
    avg_score=sum(l)/len(similar_doc)
    return(avg_score)

'''
#Relative Score
user_scores=list(scores.values())
topper_score=max(user_scores)
relative_scores={}
users=questions.usernames
for i in range(len(user_scores)):
    relative_scores[users[i]]=(user_scores[i]/topper_score)*100
print("Relative Scores",relative_scores)
'''
