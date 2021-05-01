from classQuestions import Question
from classDiagnosis import Diagnosis

class ExpertSystem():
    def run():
        __then__ = Diagnosis()
        __if__ = Question()

        while __then__.resultProbability != 100:
            question = __if__.text()
            __then__.question(question[0], question[1])
            print('\nA probabilidade é de ' + str(__then__.resultProbability()) + '%')
            print(__then__.results)
            if __then__.resultProbability() == 100:
                print('\nSeu dinossauro é o: ' +  __then__.results[0] + '\n')
                exit()

if __name__ == "__main__":
    initialPrompt = input('\n ---------- Sistema Especialista Dinossauro v2.0 ---------- \n \n ------ Descubra as características de um dinossauro ------ \n                Vamos começar? Sim ou Não?               \n Resposta: ')
    if initialPrompt.lower() == "s" or initialPrompt.lower() == "sim":
        ExpertSystem.run()
    elif initialPrompt.lower() == "n" or initialPrompt.lower() == "não":
        exit()

