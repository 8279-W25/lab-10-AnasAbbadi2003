import time
from adafruit_circuitplayground import cp

# Dictionary of letters and their translation to Morse code
morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
    'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', 
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', 
    '8': '---..', '9': '----.', ' ': '/'
}


# The user Input
user_phrase = input("Enter your phrase: ")

# Function to clean the user input
def check_phrase(user_phrase , morse):
    test01 = True
    while test01:
        # string that will have the cleaned version
        cleaned = ''   
        # check if the user have left the input empty
        if(len(user_phrase) == 0):
            print("Please don't leave your input empty")
            user_phrase = input("Enter your phrase : ") 
        else:
            for l in user_phrase.upper():    #looping over the input with making it upperCase to match the dictionary
                if l in morse :
                    cleaned += l
            test01 = False    # to pause the loop
            return cleaned 

#putting the return value into a variable
cleaned = check_phrase(user_phrase, morse_code)
# Function to translate cleaned input into a Morse code list
def translate(cleaned, morse_code):
    morse_list = []
    for i in cleaned:
        morse_list.append(morse_code[i])
    return morse_list

#putting the return value into a variable
morse_list = translate(cleaned, morse_code)

# Get user time with validation
while True:
    try:
        entered_time = float(input("Please enter a number between 0 - 1 seconds: "))
        if 0 < entered_time <= 1:
            break
        else:
            print("Please enter a number in the given range (0-1 seconds)!!!")
    except ValueError:
        print("Please enter a number!!")

# Function to display Morse code with lights
def morse_light(entered_time, morse_list):
    # Get user color with validation
    while True:
        user_color = input("Which color would you like (Red, Green, Blue)? ").lower()
        if user_color == "red":
            color = (255, 0, 0)
            tone_freq = 600  
            break
        elif user_color == "green":
            color = (0, 255, 0)
            tone_freq = 500  
            break
        elif user_color == "blue":
            color = (0, 0, 255)
            tone_freq = 400  
            break
        else:
            print("Please pick one of the three colors: Red, Green, or Blue.")

    
    

    # Display Morse code
    for morse in morse_list:
        if morse == '/':  # Word separator
            cp.pixels.fill((0, 0, 0))  # Turn off LEDs
            time.sleep(entered_time * 7)  # 7-unit space
        else:
            for letter in morse:  # Process each dot or dash
                if letter == '.':
                    cp.pixels.fill(color)  # Turn on LEDs
                    cp.play_tone(tone_freq, entered_time)  # Play tone for 1 unit
                    cp.pixels.fill((0, 0, 0))  # Turn off LEDs
                    time.sleep(entered_time)  # Off for 1 unit
                elif letter == '-':
                    cp.pixels.fill(color)  # Turn on LEDs
                    cp.play_tone(tone_freq, entered_time * 3)  # Play tone for 3 units
                    cp.pixels.fill((0, 0, 0))  # Turn off LEDs
                    time.sleep(entered_time)  # Off for 1 unit
            time.sleep(entered_time * 2)  # Additional 2 units (total 3 between letters)

# Run the Morse code display
morse_light(entered_time, morse_list)
