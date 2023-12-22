import operator
import random

class MbtiGift:
    def __init__(self):
        print("******** This is a gift recommending program depending on mbti ********")

        while True:
            print("\n***********************************************************************")
            print("*     category: 도서/패션/상품권/코스메틱/전자기기/문구/리빙/건강     *")
            print("* ----------------------- << choose option >> ----------------------- *")
            print("*                                                                     *")
            print("* (1) Get gift recommendation | (2) Enter the desired gift | (3) Quit *")
            print("*                                                                     *")
            print("***********************************************************************")
            option = int(input("enter the number of your option --> "))

            if option == 1:
                self.output_gift()
            elif option == 2:
                self.input_gift()
            elif option == 3:
                print("프로그램을 종료합니다.")
                break
            else:
                print("Wrong input. Please input 1~3.")

    def  output_gift(self):
        fp_e = open("present/present_e.txt", "r+", encoding="utf8")
        fp_i = open("present/present_i.txt", "r+", encoding="utf8")
        fp_n = open("present/present_n.txt", "r+", encoding="utf8")
        fp_s = open("present/present_s.txt", "r+", encoding="utf8")
        fp_f = open("present/present_f.txt", "r+", encoding="utf8")
        fp_t = open("present/present_t.txt", "r+", encoding="utf8")
        fp_p = open("present/present_p.txt", "r+", encoding="utf8")
        fp_j = open("present/present_j.txt", "r+", encoding="utf8")

        mbti_ = self.enter_mbti()
        gift_category = input("Enter the category --> ")
        gifts = []

        if mbti_[0] == 'e':
            gifts += fp_e.readlines()
        else:
            gifts += fp_i.readlines()
        if mbti_[1] == 'n':
            gifts += fp_n.readlines()
        else:
            gifts += fp_s.readlines()
        if mbti_[2] == 'f':
            gifts += fp_f.readlines()
        else:
            gifts += fp_t.readlines()
        if mbti_[3] == 'p':
            gifts += fp_p.readlines()
        else:
            gifts += fp_j.readlines()

        category_selected_gifts = []
        for gift in gifts:
            tokens = gift.strip().split(",")
            if tokens[0] == gift_category:
                category_selected_gifts.append(tokens[1])

        freq = dict()
        category_selected_gifts_set = set(category_selected_gifts)
        for selected_gift in category_selected_gifts_set:
            freq[selected_gift] = category_selected_gifts.count(selected_gift)
        sorted_freq = sorted(freq.items(), key = operator.itemgetter(1))
        # printing for debugging
        # print(sorted_freq)
        # print(sorted_freq[-3:])
        recommended_gift = random.choice(sorted_freq[-3:])[0]
        print("-----------------------------------------------------------------------")
        print("recommended gift: ", recommended_gift)
        self.output_msg(gift_category)


    def input_gift(self):
        fp_e_w = open("present/present_e.txt", "a", encoding="utf8")
        fp_i_w = open("present/present_i.txt", "a", encoding="utf8")
        fp_n_w = open("present/present_n.txt", "a", encoding="utf8")
        fp_s_w = open("present/present_s.txt", "a", encoding="utf8")
        fp_f_w = open("present/present_f.txt", "a", encoding="utf8")
        fp_t_w = open("present/present_t.txt", "a", encoding="utf8")
        fp_p_w = open("present/present_p.txt", "a", encoding="utf8")
        fp_j_w = open("present/present_j.txt", "a", encoding="utf8")

        mbti_ = self.enter_mbti()
        preferred_gift = input("Enter your favorite gift with the category (category,gift) --> ")
        line = "\n" + preferred_gift

        if mbti_[0] == 'e':
            fp_e_w.write(line)
        else:
            fp_i_w.write(line)
        if mbti_[1] == 'n':
            fp_n_w.write(line)
        else:
            fp_s_w.write(line)
        if mbti_[2] == 'f':
            fp_f_w.write(line)
        else:
            fp_t_w.write(line)
        if mbti_[3] == 'p':
            fp_p_w.write(line)
        else:
            fp_j_w.write(line)

        fp_e_w.close()
        fp_i_w.close()
        fp_n_w.close()
        fp_s_w.close()
        fp_f_w.close()
        fp_t_w.close()
        fp_p_w.close()
        fp_j_w.close()

    def output_msg(self, gift_category):
        category_messages = {
            "도서": "기억에 오래 남는 책이 되길..",
            "패션": "잘 어울릴 것 같아 선물합니다!",
            "상품권": "필요한 곳에 유용히 잘 쓰세요.",
            "코스메틱": "향기로운 일상을 위한 선물!",
            "전자기기": "바쁜 일상에 함께 하세요.",
            "문구": "생각과 기억을 기록하세요.",
            "리빙": "보금자리를 위한 선물을 준비했어요.",
            "건강": "건강이 최고!"
        }

        if gift_category in category_messages:
            print("gift card message: ", category_messages[gift_category])
        else:
            print("카테고리를 찾을 수 없습니다. 올바른 카테고리를 입력하세요.")


    def enter_mbti(self):
        while True:
            mbti = input("Enter the mbti --> ").lower()
            if len(mbti) != 4:
                print("Incorrect input !! MBTI consists of four letters.")
            elif mbti[0] != 'i' and mbti[0] != 'e':
                print("Incorrect input !! MBTI starts with 'i' or 'e'.")
            elif mbti[1] != 's' and mbti[1] != 'n':
                print("Incorrect input !! MBTI's second letter is 's' or 'n'.")
            elif mbti[2] != 'f' and mbti[2] != 't':
                print("Incorrect input !! MBTI's third letter is 'f' or 't'.")
            elif mbti[3] != 'p' and mbti[3] != 'j':
                print("Incorrect input !! MBTI's last letter is 'p' or 'j'.")
            else:
                return mbti