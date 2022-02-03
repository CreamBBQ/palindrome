def is_palindrome(string : str) -> bool:
    string = string.replace(" ", "").lower()
    return string == string[::-1]

def run(): 
    userPhrase = input("Ingrese una palabra o frase para saber si es un palindromo: ")
    if is_palindrome(userPhrase):
        print("Es un palindromo")
    else: 
        print("No es un palindromo")


if __name__ == "__main__":
    run()
