class Solution:
    def morese_to_string(self, word):
        morse_to_eng = {
            '.-' : 'a', 
            '-...' : 'b', 
            '-.-.' : 'c', 
            '-..' : 'd', 
            '.' : 'e', 
            '..-.' : 'f', 
            '--.' : 'g',
            '....' : 'h',  
            '..' : 'i', 
            '.---' : 'j', 
            '-.-' : 'k', 
            '.-..' : 'l', 
            '--' : 'm', 
            '-.' : 'n', 
            '---' : 'o', 
            '.--.' : 'p', 
            '--.-' : 'q', 
            '.-.' : 'r', 
            '...' : 's', 
            '-' : 't', 
            '..-' : 'u', 
            '...-' : 'v', 
            '.--' : 'w', 
            '-..-' : 'x', 
            '-.--' : 'y', 
            '--..' : 'z',

            '.----' : '1',
            '..---' : '2',
            '...--' : '3',
            '...._' : '4',
            '.....' : '5',
            '-....' : '6',
            '--...' : '7',
            '---..' : '8',
            '----.' : '9',
            '-----' : '0',

            '.-.-.-' : '.', 
            '..--..' : '?',
            '--..--' : ',',
            '-..-.' : '/',
            '---...' : ':',
            '_...._' : '-',
            '----' : "'",
            '.-..-.' : '"',
            '-.--.' : '(',
            '-.--.-' : ')',
            '-...-' : '=',
            '.-.-.' : '+',
            '_._._.' : ';',
            '.--.-.' : '@',
        }
        translated_output = ''
        morse_chars = word.split(' ')
        # print(morse_chars)
        if morse_chars[0] in morse_to_eng.keys():
            for i in morse_chars:
                if i in morse_to_eng:
                    translated_output=translated_output+morse_to_eng[i]
                elif i ==" " or i=="":
                    translated_output += ' '
                else:
                    translated_output="Data not formatted properly"
                    break
        else:
            translated_output="Data not formatted properly"
        return translated_output
    
    def string_to_morse(self, word):
        translated_output = ''
        eng_to_morse = {
            'a' : '.-', 
            'b' : '-...', 
            'c' : '-.-.', 
            'd' : '-..', 
            'e' : '.', 
            'f' : '..-.', 
            'g' : '--.', 
            'h' : '....', 
            'i' : '..', 
            'j' : '.---', 
            'k' : '-.-', 
            'l' : '.-..', 
            'm' : '--', 
            'n' : '-.', 
            'o' : '---', 
            'p' : '.--.', 
            'q' : '--.-', 
            'r' : '.-.', 
            's' : '...', 
            't' : '-', 
            'u' : '..-', 
            'v' : '...-', 
            'w' : '.--', 
            'x' : '-..-', 
            'y' : '-.--', 
            'z' : '--..',

            '1' : '.----',
            '2' : '..---',
            '3' : '...--',
            '4' : '...._',
            '5' : '.....',
            '6' : '-....',
            '7' : '--...',
            '8' : '---..',
            '9' : '----.',
            '0' : '-----',

            '.' : '.-.-.-', 
            '?' : '..--..',
            ',' : '--..--',
            '/' : '-..-.',
            ':' : '---...',
            '-' : '_...._',
            "'" : '----',
            '"' : '.-..-.',
            '(' : '-.--.',
            ')' : '-.--.-',
            '=' : '-...-',
            '+' : '.-.-.',
            ';' : '_._._.',
            '@' : '.--.-.',
            
        }
        for i in word:
            if i in eng_to_morse:
                translated_output=translated_output+eng_to_morse[i]+" "
            elif i ==" " or i =="":
                translated_output += ' '
            else:
                translated_output="Data not formatted properly"
                break
        return translated_output

if __name__ == "__main__":
    word = input("Enter Something to be Translated: \n")
    obj=Solution()
    choice = int(input("Enter 1 to convert String to Morse Code\nEnter 2 to convert Morse Code to String\n"))
    if choice == 1:
        result = obj.string_to_morse(word)
        print(result)
    elif choice == 2:
        result = obj.morese_to_string(word)
        print(result)
    else:
        print("Wrong Choice")