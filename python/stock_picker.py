import math
def picker(prices):
    status = 'still'

    start = 0
    end = 0
    max = 0
    min = prices[0]
    diff = 0

    maybe = 0
    maybe_max = 0
    maybe_min = prices[0]

    for i, price in enumerate(prices):
        if status == 'still':
            if (i == len(prices) - 1 or prices[i + 1] > price) and price < min:
                start = i
                min = price
                max = price
                status = 'bought'
        if status == 'bought':
            if (i == len(prices) - 1 or prices[i + 1] < price) and price > max:
                max = price
                diff = max - min
                status = 'sold'
                end = i
                maybe_min = prices[i + 1]
        elif status == 'sold':
            if (i == len(prices) - 1 or prices[i + 1] > price)and price < maybe_min:
                status = 'maybe'
                maybe = i
                maybe_min = price
                maybe_max = price
        elif status == 'maybe':
            if (i == len(prices) - 1 or prices[i + 1] < price) and price > maybe_max:
                maybe_max = price
                if maybe_max - maybe_min > diff:
                    start = maybe
                    end = i
    return [start, end]



