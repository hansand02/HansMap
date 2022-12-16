
class HansMap:

    LOAD_FACTOR_TRESHOLD = 0.75

    def __init__(self) -> None:
        self.n = 1
        self.__items = 0
        self.array = [None] * self.n

    def __loadfactor(self) -> int:
        return  self.__items/self.n
    
    def __ensurecapacity(self) -> None:
        if self.__loadfactor() >= self.LOAD_FACTOR_TRESHOLD:
            self.__rehash()

    def __rehash(self) -> None:
        """ Rehashes self.array to make size for new items, never use manually"""
        tmp = [list for list in self.array]
        self.n *= 2
        self.array = [None] * self.n
        self.__items = 0
        for list in tmp:
            if list == None: continue
            for tuple in list:
                self[tuple[0]] = tuple[1]
            
    def __setitem__(self, key, value) -> None:
        """ Sets item in the self datastructure, by using dunder method to make self[k] = v possible.
        Items sent in must be of correct type (string or integer), and will not be converted """

        self.__ensurecapacity()
        
        #LAGE HASHNØKKEL 
        k = self.hashKey(key)
        #SJEKK OM "BØTTE" FINNES 
        if self.array[k] == None:
            self.array[k] = list()
            self.__items += 1
            return self.array[k].append((key,value))   
        
        #SETT INN TUPLE I "BØTTE"
        bucket = self.array[k]
        for i, v in enumerate(bucket):
            if v[0] == key:
                bucket[i] = (key,value) 
                self.__items += 1
                return
        self.__items += 1
        bucket.append((key, value))

    def __getitem__(self, key):
        k = self.hashKey(key)

        bucket = self.array[k]
        if bucket == None:
            return "ingenting her " ##### /TODO: Fjern denne string etter første test av MVP
        for tuple in bucket:
            if tuple[0] == key:
                return tuple[1]

    def __delitem__(self, key):
        k = self.hashKey(key)
        self.array[k] = [(i,v) for i,v in self.array[k] if i != key]
        self.__items -= 1

    def __str__(self) -> str:
        string = "Start HansMap {\n"
        for i in self:
            string += f"{i[0]} : {i[1]}\n"
        string += "} End HansMap"
        return string

    def __repr__(self) -> str:
        pass

    def __iter__(self) -> tuple:
        for b in self.array:
            if b:
                for tuple in b:
                    yield tuple
    
    def __len__(self) -> int:
        """ Returns amount of items in list """
        print(self.__items)
        return self.__items

    def hashKey(self, key) -> int:

        def hashString(s) -> int:
            """This function hashes a string and creates a key for inserting in self.array
            A copy of the function used for hashing in Java
            """
            assert isinstance(s, str), "Her har det skjedd noe rart! Er du sikker på at du enten har sendt inn en int eller str?"
            h = 0   
            for l in s:
                h = h*31 + ord(l)
            return h%len(self.array)
        def hashInt(i) -> int:
            """ Hashes int by ret """
            return i%len(self.array)
    
        if isinstance(key,int):
            return hashInt(key)
        elif isinstance(key, str):
            return hashString(key)
        else:
            raise Exception("Input for keys and values must be of type int or str, at least for now")
    
    def insert(self, key, value) -> None:
        self.__setitem__(key,value)

    

    

    