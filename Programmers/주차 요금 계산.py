import datetime
import math


def solution(fees, records):
    answer = []
    parking = dict()
    price = dict()
    for record in records:
        time, number, what = record.split()
        time = datetime.datetime.strptime(time, '%H:%M')
        if what == 'IN':
            parking[number] = time
            if number not in price.keys():
                price[number] = 0
        else:
            price[number] += (time - parking[number]).seconds // 60
            del parking[number]
        # print(parking, price)
    if parking:
        for number in parking.keys():
            try:
                price[number] += (datetime.datetime.strptime('23:59', '%H:%M') - parking[number]).seconds // 60
            except KeyError:
                price[number] = (datetime.datetime.strptime('23:59', '%H:%M') - parking[number]).seconds // 60

    price = dict(sorted(price.items()))
    # print(price)
    for number in price.keys():
        if price[number] > fees[0]:
            answer.append(fees[1] + math.ceil((price[number]-fees[0])/fees[2])*fees[3])
        else:
            answer.append(fees[1])
    return answer


print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
print(solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))
print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))
print(solution(
    [180, 5000, 10, 600],
    ["05:34 5961 IN", "06:34 5961 OUT", "07:34 5961 IN", "08:34 5961 OUT", "09:34 5961 IN", "10:34 5961 OUT", "11:34 5961 IN", "12:34 5961 OUT"]
  ))