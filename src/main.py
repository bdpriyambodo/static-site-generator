# print('hello world')

from textnode import TextType, TextNode
from remove_and_copy import remove_and_copy

def main():
    test = TextNode('This is some anchor text', TextType.LINK, 'https://www.boot.dev')
    print(test)

    remove_and_copy("static","public")


if __name__ == "__main__":
    # This block is executed only when the script is run directly
    main()