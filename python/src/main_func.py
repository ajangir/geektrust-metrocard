cards = {}
stations = {'CENTRAL':[0,0,{}],'AIRPORT':[0,0,{}]}
fare = {'ADULT':200, 'SENIOR_CITIZEN':100, 'KID':50}

def addBalance(card_id, balance):
    if card_id in cards:
        cards[card_id][0] += balance
    else:
        cards[card_id] = [balance,[]]
    return

def deductFare(card_id,start_station,card_category,journey_type):
    curr_balance = cards[card_id][0]
    if journey_type == 'SINGLE':
        to_be_deducted = fare[card_category]
    if journey_type == 'RETURN':
        to_be_deducted = fare[card_category]//2
        stations[start_station][1] += to_be_deducted
    stations[start_station][0] += to_be_deducted
    stations[start_station][2][card_category] = stations[start_station][2].get(card_category,0)+1

    if to_be_deducted > curr_balance:
        auto_deduct = to_be_deducted - curr_balance
        cards[card_id][0] = 0
        stations[start_station][0] += (2*auto_deduct)//100
    else:
        cards[card_id][0] -= to_be_deducted

def checkIn(card_id, card_category, start_station):
    
    last_journeys = cards[card_id][1]
    curr_fare = fare[card_category]
    
    if len(last_journeys) >= 2:
        if start_station != last_journeys[-1]:
            if start_station != last_journeys[-2]:
                deductFare(card_id,start_station,card_category,'RETURN')
            else:
                deductFare(card_id,start_station,card_category,'SINGLE')
        else:
            deductFare(card_id,start_station,card_category,'SINGLE')
    elif len(last_journeys) == 1:
        if start_station != last_journeys[-1]:
            deductFare(card_id,start_station,card_category,'RETURN')
        else:
            deductFare(card_id, start_station, card_category, 'SINGLE')
    else:
        deductFare(card_id,start_station,card_category,'SINGLE')
    
    cards[card_id][1].append(start_station)
    return

def printSummary():
    #print(cards)
    for station in stations:
        print('TOTAL_COLLECTION ',station,stations[station][0],stations[station][1])
        print('PASSENGER_TYPE_SUMMARY')
        summary = sorted([[i,stations[station][2][i]] for i in stations[station][2]],key=lambda x:(x[0],x[1]))
        #print(summary)
        for i in summary:
            print(i[0],i[1])
    return
