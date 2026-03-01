from utils.tokenizer import Tokenizer

def main():
    text = str(input("Enter the text to tokenize: ")).strip()
    tokenizer = Tokenizer(tokenizer_type="nltk")
    tokens = tokenizer.tokenize(text)
    print(tokens)

if __name__ == "__main__":
    main()