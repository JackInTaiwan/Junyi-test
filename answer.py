def q1() :
    sentence = input("Please enter one complete sentence: ")
    words = sentence.split()

    for i, word in enumerate(words) :
        words[i] = word[-1::-1]

    sentence_rev = " ".join(words)

    print (sentence_rev)



def q2() :
    num = int(input("Please enter one positive integer: "))
    count = 0
    for i in range(1, num + 1) :
        if (i % 3 != 0 and i % 5 != 0) or (i % 3 == 0 and i % 5 == 0) :
            count += 1

    print (count)



if __name__ == "__main__" :
    while True :
        q = int(input("Please enter the number of question (1 or 2) : "))

        # Question 1
        if q == 1 :
            q1()
            break

        # Question 2
        elif q == 2 :
            q2()
            break