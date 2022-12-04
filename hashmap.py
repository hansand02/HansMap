
class HansMap:

    LOAD_FACTOR_TRESHOLD = 0.75

    def __init__(self) -> None:
        self.n = 1
        self.items = 0
        self.array = [None] * self.n

    def __loadfactor(self) -> int:
        return  self.items/self.n
    
    def __ensurecapacity(self) -> None:
        if self.__loadfactor() >= self.LOAD_FACTOR_TRESHOLD:
            self.__rehash()

    def __rehash(self) -> None:
        tmp = [(k,v) for k, v in enumerate(self.array)]
        self.n *= 2
        self.array = [None] * self.n
        for k,v in tmp:
            self.array[k] = v

    def insert(self, key, value) -> None:
        self.__setitem__(key,value)

    def __setitem__(self, key, value) -> None:
        """ Sets item in the self datastructure, by using dunder method to mak self[k] = v possible.
        Items sent in must be of correct type (string or integer), and will not be converted """

        self.__ensurecapacity()
        
        #LAGE HASHNØKKEL 
        if isinstance(key,int):
            k = self.hashInt(key)
        elif isinstance(key,str):
            k =self.hashString(key)
        else:
            raise Exception("Input for keys and values must be of type int or str, at least for now")

        #SJEKK OM "BØTTE" FINNES 
        if self.array[k] == None:
            self.array[k] = list()
        
        #SETT INN TUPLE I "BØTTE"
        bucket = self.array[k]

        bucket.append((key, value))
        self.items += 1


    def __getitem__(self, key) -> int or str:
        val = key
        if isinstance(key,int):
            key = self.hashInt(key)
        elif isinstance(key, str):
            key =self.hashString(key)
        else:
            raise Exception("Input for keys and values must be of type int or str, at least for now")

        bucket = self.array[key]
        if bucket == None:
            return "ingenting her " ##### /TODO: Fjern denne string etter første test av MVP
        
        for i in bucket:
            if i == val:
                return i

    def __str__(self) -> str:
        return self.array.__str__()
    
    def hashString(self, s) -> int:
        """This function hashes a string and creates a key for inserting in self.array
        A copy of the function used for hashing in Java
        """
        assert isinstance(s, str), "Her har det skjedd noe rart! Er du sikker på at du enten har sendt inn en int eller str?"
        h = 0   
        for l in s:
            h = h*31 + ord(l)
        return h%len(self.array)
    
    def hashInt(self, i) -> int:
        return i-1 if i <= len(self.array) else i%len(self.array)

    