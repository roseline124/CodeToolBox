class myMeta : 
    def __init__(self, name) :
        self.className = name

    def __str__(self) :
        return self.className

class myClass :

    __metaclass__ = myMeta
    pass

    
    myClass = myMeta('안녕 메타')
    print(type(myClass))
    print(myClass)
    print(type(myMeta))

