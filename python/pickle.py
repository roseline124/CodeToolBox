import pickle

class User : 
    def __init__(self, score, grade) :
        self.score = score 
        self.grade = grade

user = User(100, 'Gold')
_user = {'score' : user.score, 'grade' :user.grade}
#save as pickle 
with open('test.p', 'wb') as f : 
    pickle.dump(_user, f) #데이터 객체, 파일

#read pickle
with open('test.p', 'rb') as f : 
    user_score = pickle.load(f)
    print(user_score)
