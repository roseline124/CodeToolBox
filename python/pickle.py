import pickle

class User : 
    def __init__(self, score) :
        self.score = score 

user = User(100)

#save as pickle 
with open('test.p', 'wb') as f : 
    pickle.dump(user.score, f) #데이터 객체, 파일

#read pickle
with open('test.p', 'rb') as f : 
    user_score = pickle.load(f)
    print(user_score)
