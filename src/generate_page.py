import os
from markdown_to_html import markdown_to_html_node, clear_screen
from htmlnode import HTMLNode, LeafNode, ParentNode

def extract_title(markdown):
    try:
        with open(markdown, 'r') as file:
            lines = file.readlines() # Read the entire file
            title = []
            for number, line in enumerate(lines,1):
                if line.startswith('# '):
                    # print(f'line number: {number} --> {line}')
                    title.append(line.replace('# ','').strip())
                    print(f'title: {title}')
            if len(title) == 0:
                raise Exception('Title (h1) is not found')
            if len(title) > 1:
                raise Exception('Multiple titles (h1) are found')
            return title[0]

    except FileNotFoundError:
        print("The file was not found.")

def generate_page(from_path, template_path, dest_path):
    print(f'Generating page from {from_path} to {dest_path} using {template_path}')


    with open(from_path) as file:
        content = file.read()

    with open(template_path) as file:
        template = file.read()

    # convert markdown to html
    print('\nSTARTING PROCESS: MARKDOWN TO HTML NODE...')
    html_node = markdown_to_html_node(content)
    print(html_node)
    html = html_node.to_html()

    # extract title from markdown
    title = extract_title(from_path)

    edited_template = template.replace("{{ Title }}",title).replace("{{ Content }}",html)

    # write into file
    with open(dest_path, 'w') as file:
        file.write(edited_template)


if __name__ == '__main__':
    clear_screen()
    title = extract_title("content/index.md")
    print(title)