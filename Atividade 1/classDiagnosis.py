class Diagnosis():

    def __init__(self):
        self.results = [
            'triceratops', 
            'estegossauro', 
            'braquiceratops', 
            'galimimus', 
            'tiranossauro', 
            'celidossauro', 
            'dilofossauro',
            'callovossauro'
        ]
        self.database = []
        
        file = open('db2.txt', 'r')

        for line in file:
            if line[len(line) - 1] == '\n':
                line = line.replace("\n", "")
                (self.database).append(line.split('-'))

        file.close()
    
    def size(self):
        print(len(self.results))
    
    def resultProbability(self):
        return (
            int(
                (1/int(len(self.results))) * 100
            )
        )

    def question(self, question, characteristic):
        answer = input(question + 'Resposta: ')
        if answer.lower() == 's' or answer.lower() == "sim":
            self.removingTheUnnecessary(True, characteristic)
        elif answer.lower() == 'n' or answer.lower() == "não":
            self.removingTheUnnecessary(False ,characteristic)
    
    def removingTheUnnecessary(self, yesOrNo, characteristic):
        itemsToRemove = []
        counter = 0
        for count in range(len(self.results)):
            if yesOrNo != self.search(self.results[count], characteristic):
                itemsToRemove.append(self.results[count])
                counter = counter + 1
        for count in range(counter):
            self.results.remove(itemsToRemove[count])
    
    def search(self, dinosaur, characteristic):
        for count in range(len(self.database)):
            if dinosaur == self.database[count][1]:
                if self.database[count][0] == characteristic:
                    return True
        return False


             