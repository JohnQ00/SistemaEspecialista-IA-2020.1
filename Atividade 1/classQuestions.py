class Question:

    def __init__(self):
        self.questionsData = [
            ['\nSeu dinossauro é bípede?\n', 'bipede'],
            ['\nSeu dinossauro possui toneladas de peso?\n', 'pesado'],
            ['\nSeu dinossauro viveu no período jurássico?\n', 'jurassico']
        ]
    
    def text(self):
        questionToSend = self.questionsData[0]
        del self.questionsData[0]
        return questionToSend

    # def teste():
    #     print("tobesal")
    #     return "aaaaaa"


