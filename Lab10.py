# Dictionary of letters and their translation to morse code
morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', 
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', 
    '8': '---..', '9': '----.', ' ':'/'
}
# The user Input
user_phrase = input("Enter your phrase : ")
# Function to clean the user input into only the wanted characters
def check_phrase(user_phrase , morse):
    test = True
    while test:
        # string that will have the cleaned version
        cleaned = ''   
        # check if the user have lest the input empty
        if(len(user_phrase) == 0):
            print("Please don't leave your input empty")
            user_phrase = input("Enter your phrase : ") 
        else:
            for l in user_phrase.upper():    #looping over the input with making it upperCase to match the dictionary
                if l in morse :
                    cleaned += l
            test = False    # to pause the loop
            return cleaned 
                
cleaned = check_phrase(user_phrase,morse_code)
