from os import system
system("cls")

def sortbro(word : str):
    wordlist = []
    for i in word:
        wordlist.append(i)
    return sorted(wordlist)



def anagrammas(input : list[str]) -> list:
    output = []
    
    

    while len(input) > 0:
        j = 0
        i = 0
        currentWordList = sortbro(input[i])
        tempOutput = []

        while j < len(input):
            if sortbro(input[j]) == currentWordList:
                tempOutput.append(input[j])
                input.pop(j)
            else:
                j += 1
        output.append(tempOutput)
    
    return output


kirish = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat','cat','atc', 'tab']

print(anagrammas(kirish))

print(sortbro("salomatlik"))

        

        
