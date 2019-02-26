import random 


def faulty_rate(length) :

    _list = [ round(random.random(),3) for n in range(length) ]

    faulty = [ p for p in _list if (p < 0.99) | (p >= 1.01) ]
    
    print(len(_list))
    print(len(faulty))

    print(round( len(faulty)/len(_list), 3))

faulty_rate(1000)
