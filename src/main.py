# print('hello world')

import sys
from textnode import TextType, TextNode
from remove_and_copy import remove_and_copy
from generate_page import generate_page, generate_pages_recursive

def main():
    # test = TextNode('This is some anchor text', TextType.LINK, 'https://www.boot.dev')
    # print(test)
    
    if sys.argv[1] is not None:
        basepath = sys.argv[1]
    else:
        basepath = '/'

    print(f'basepath: {basepath}')

    destination = 'docs'

    remove_and_copy("static",destination)

    # generate_page('content/index.md','template.html','public/index.html')
    generate_pages_recursive('content','template.html',destination, basepath)



if __name__ == "__main__":
    # This block is executed only when the script is run directly
    main()