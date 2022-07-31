def odometer(oksana):
    way = oksana[0] * oksana[1]
    for i in range(2,len(oksana),2):
        try:
            way = way + (oksana[i] * (oksana[i+1]-oksana[i-1]))
        except OverflowError:
            print("переполнение!!!")
    return way
