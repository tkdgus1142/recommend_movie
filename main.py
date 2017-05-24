#-*- coding: utf-8 -*-
import math
import pickle
import numpy

class Search:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.score_list = []

def set_Search():#사용자에게 영화 제목과 평점을 입력받는 함수

    num=raw_input("몇개의 영화를 입력하시겠습니까?\n")
    name=[]
    score=[]
    for i in range(0,int(num)):
        mName = raw_input("Name: ")
        mScore = raw_input("Score : ")
        name.append(unicode(mName, 'utf-8'))
        score.append(unicode(mScore))

    search = Search(name, score)
    return search

def score_Search(search):
#네이버의 영화 평점 데이터를 모은 파일을 가져오고
#사용자가 입력한 영화제목을 평가한 데이터를 score_list에 저장한다.
    f = open('reviewData.txt', 'rb')
    a = pickle.load(f) #저장된 데이터
    mName = search.name

    for key, value in a.items():
        b = value
        for i in b.keys():
            if i in mName:
                search.score_list.append(b)

def compare(search):
#사용자가 입력한 영화의 대한 평점을 그 영화를 본 id가 입력한 평점과
#코사인 유사도를 계산하여 가장높은 유사도를 가진 id가 평가한 영화중
#평점이 7점 이상인 영화를 추천한다.
    my_score = search.score
    other_score = search.score_list

    compare_list=[]

    user_vector=[]
    compare_vector=[]

    result=[]

    for i in other_score:
        temp=set()
        for j in i.keys():
            temp.add(j)
        for j in search.name:
            temp.add(j)
        temp=list(temp)
        compare_list.append(temp)

    for i in compare_list:
        user=[]
        for j in i:
            if j in search.name:
                user.append(int(search.score[search.name.index(j)]))
            else:
                user.append(0)
        user_vector.append(user)

    for i in compare_list:
        count=0
        com=[]
        for j in i:
            if j in search.score_list[count].keys():
                com.append(int(search.score_list[count][j]))
            else:
                com.append(0)
        count+=1
        compare_vector.append(com)

    # 점곱(두 벡터로 스칼라를 계산하는 연산)
    for i in range(len(user_vector)):
        d=0
        len(compare_list[i])
        user_vector[i], compare_vector[i]

        temp = numpy.array(user_vector[i])*numpy.array(compare_vector[i])
        for k in temp:
            d+=k



        # A벡터의 길이
        h = 0
        for j in user_vector[i]:
            h += int(j)*int(j)
        h = math.sqrt(h)

        # B벡터의 길이
        k = 0
        for j in compare_vector[i]:
            k += int(j)*int(j)
        k = math.sqrt(k)

        result.append(d/h*k)

    print max(result)
    index= result.index(max(result))
    recommend=search.score_list[index]
    for i in recommend.keys():
        if int(recommend[i])>=7:
            print i, recommend[i]

def run():
    while 1:
        search = set_Search()
        score_Search(search)
        compare(search)
        break

if __name__ == "__main__":
    run()
