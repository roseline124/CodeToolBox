# 축의금 
congraturatory_money = 5

class Question :
    extra = 0 
    def __init__(self, Y_cost, N_cost, question) :
        self.Y_cost = Y_cost
        self.N_cost = N_cost
        self.question = question
    
    def link_next(self,Y_next, N_next) : 
        self.Y_next = Y_next
        self.N_next = N_next
        
    def ask(self):
        while True : 
            self.answer = input(f"{self.question} (Y/N)").upper()
            
            if self.answer == "Y" :
                Question.extra += self.Y_cost
                return self.Y_next
            elif self.answer == "N" :
                Question.extra += self.N_cost
                return self.N_next
            else : 
                print("'Y' 또는 'N'으로 입력해주세요")
                
Q1 = Question(1, 0, "최근 1년 간 청첩장이 아닌 이유로 만난 적이 있다.")  
Q2 = Question(1, 0, "청첩장을 직접 받았다.")  
Q3 = Question(-1, 0, "청첩장을 모바일로 받았다.")
Q4 = Question(0, 0, "인연을 맺은 지 5년 이상이다.")  
Q5 = Question(0, 0, "직장 동료다.") 
Q6 = Question(0, 0, "SNS 친구다.")  
Q7 = Question(1, 0, "자주 보는 사이다.")  
Q8 = Question(-2, 0, "이번이 재혼이다.")  
Q9 = Question(2, 0, "식장이 호텔이다.")  
Q10 = Question(-2, 0, "그로부터 상처를 받은 적이 있다.")  
Q11 = Question(-1, 0, "결혼 성수기다. ") 
Q12 = Question(-1, 0, "식장이 지방이다.") #  -> 봉투만 전해도 OK
Q13 = Question(2, 0, "나도 2년 안에 결혼할 예정이다.") # -> 필참
Q14 = Question(1, 0, "액수를 정했는데 뭔가 불안하다.") # -> 봉투만 전해도 OK

Q1.link_next(Q2, Q3)
Q2.link_next(Q5, Q3)
Q3.link_next(Q6, Q5)
Q4.link_next(Q7, Q9)
Q5.link_next(Q7, Q4)
Q6.link_next(Q11, Q5)
Q7.link_next(Q8, Q9)
Q8.link_next(Q10, Q11)
Q9.link_next(Q13, Q12)
Q10.link_next(Q12, Q11)
Q11.link_next(Q9, Q13)
Q12.link_next("봉투만 전해도 OK", Q13)
Q13.link_next("필참", Q14)
Q14.link_next("필참", "봉투만 전해도 OK")

next_Q = Q1.ask()
while ((next_Q != "필참") & (next_Q != "봉투만 전해도 OK")):
    next_Q = next_Q.ask()

congraturatory_money += Question.extra

print("=============================================")
print(f"내야할 돈은 {congraturatory_money}만 원!")
print(next_Q)
print("=============================================")
