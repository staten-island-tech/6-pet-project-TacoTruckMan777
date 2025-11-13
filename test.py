







def ratio(number):
    positive = 0
    negative = 0
    zero = 0
    count = len(number)
    for i in range(count):
        if i > 0:
            positive += 1
        elif i < 0:
            negative += 1
        else:
            zero += 1
    pos = float(positive/count)
    neg = float(negative/count)
    ze = float(zero/count)

    print(f"positive:{pos}, negative:{neg}, zero:{ze}")

ratio([1,2,0,-4,-5])