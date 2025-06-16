SENTENCE_START :str = "i want to "

def main():
    verb : str = (input( "Enter a verb and press enter: "))
    noun :str = (input( "Enter a noun and press enter: "))
    adjective :str = (input( "Enter an adjective and press enter: "))
    
    
    print(SENTENCE_START +verb + " "+ noun + " "+ adjective + " "+ ".")
    
if __name__ == '__main__':
    main()
    