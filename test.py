from hashmap import HansMap

def main():
    dictionary = HansMap()
    dictionary[1] = 3
    dictionary[2] = 4
    dictionary[3] = 3
    dictionary[1] = 2
    dictionary[3] = "hei"
    dictionary[2] = "hva"
    dictionary[23] = "jada"
    dictionary[658312] = "hmm"
    print(dictionary[1])
    print(dictionary)

if __name__ == "__main__":
    main()
