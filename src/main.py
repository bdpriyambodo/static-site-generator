# print('hello world')

from textnode import TextType, TextNode
from remove_and_copy import remove_and_copy
from generate_page import generate_page

def main():
    # test = TextNode('This is some anchor text', TextType.LINK, 'https://www.boot.dev')
    # print(test)

    remove_and_copy("static","public")

    generate_page('content/index.md','template.html','public/index.html')



if __name__ == "__main__":
    # This block is executed only when the script is run directly
    main()