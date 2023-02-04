import random
import time


class math_qeus_gen():
    def __init__(self) -> None:
        pass
    
    q = 0
    #문제를 출제하는 함수
    def make_question(self):
        operand1 = str(random.randint(1, 50))	#1~50사이의 임의의 수
        operand2 = str(random.randint(1, 50))	#1~50사이의 임의의 수
        operator = random.randint(1,4)		#덧셈, 뺄셈, 곱셈, 나눗셈을 랜덤으로

        global q

        if (operator == 1):
            q = operand1 + ' + ' + operand2
        if (operator == 2):
            q = operand1 + ' - ' + operand2
        if (operator == 3):
            q = operand1 + ' * '+ operand2
        if (operator == 4):
            q = operand1 + ' / '+ operand2

        return q


    def startTest(self, user_input):
        main = math_qeus_gen()
        correct = 0
        wrong = 0
        sum_time = 0

        start = time.time()
        user = float(user_input) #사용자에게 답 입력받고 실수로 변환
        end = time.time()
        answer = round(eval(q), 2)

        sum_time = sum_time + end - start
        
        if (user == answer):
            print("정답!")
            correct = correct+1
            result = "Correct!"
        else :
            print("오답!")
            print("answer :", answer)
            wrong = wrong+1
            result = "Wrong!"

        print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
        print("모든 문제를 푸는데 걸린 시간 :", round(sum_time,2), "초")
        print("정답 :", correct, "오답 :", wrong)

        result_time = round(sum_time,2)


        if(wrong == 0):
            print("당신은 천재입니다!")

        result_dic = {
            # "qeustion" : q, # 문제
            "result" : result, # 정답 오답 판단
            "result_time" : result_time, # 문제 푸는데 걸린 시간
        }

        return result_dic



    def run(self):
        main = math_qeus_gen()
        correct = 0
        wrong = 0
        sum_time = 0

        for x in range(1, 6):			#다섯 문제 출제
            question = main.make_question()		#문제 출제
            print(question)			#문제 출력
            start = time.time()
            user = float(input("= "))		#사용자에게 답 입력받고 정수로 변환
            end = time.time()
            answer = round(eval(question), 2)

            print("문제", x, "번을 푸는데 걸린 시간 :", round(end-start, 2), "초")
            sum_time = sum_time + end - start
            
            if (user == answer):
                print("정답!")
                correct = correct+1
            else :
                print("오답!")
                print(answer)
                wrong = wrong+1


        print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
        print("모든 문제를 푸는데 걸린 시간 :", round(sum_time,2), "초")
        print("정답 :", correct, "오답 :", wrong)


        if(wrong == 0):
            print("당신은 천재입니다!")




# def startTest(self, user_input):
#         main = math_qeus_gen()
#         correct = 0
#         wrong = 0
#         sum_time = 0

#         # question = main.make_question()		#문제 출제
#         # print(question)			#문제 출력
#         start = time.time()
#         user = float(input("= " + user_input))
#         #user = float(input("= "))		#사용자에게 답 입력받고 실수로 변환
#         end = time.time()
#         answer = round(eval(q), 2)

#         sum_time = sum_time + end - start
        
#         if (user == answer):
#             print("정답!")
#             correct = correct+1
#             result = "Correct!"
#         else :
#             print("오답!")
#             print(answer)
#             wrong = wrong+1
#             result = "Wrong!"

#         print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
#         print("모든 문제를 푸는데 걸린 시간 :", round(sum_time,2), "초")
#         print("정답 :", correct, "오답 :", wrong)

#         result_time = round(sum_time,2)


#         if(wrong == 0):
#             print("당신은 천재입니다!")

#         result_dic = {
#             "qeustion" : q, # 문제
#             "result" : result, # 정답 오답 판단
#             "result_time" : result_time, # 문제 푸는데 걸린 시간
#         }

#         return result_dic