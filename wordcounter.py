def count_words(text):
    #counts the number of words in given text
    #returns the number of words in the text
    return len(text.split())

def main():
    #main function to run the word counter.
    #prompt the user for input
    text = input("Please enter a sentence or paragraph: ").strip()
    #check if the input is empty
    if not text:
        print("Error: You must enter some text to count the words.")
        return
    #call the count words function and display the output
    print(f"Word count: {count_words(text)}")
    
#run the program
if __name__ == "__main__":
    main()
