import os
from markdown_to_html import markdown_to_html_node, clear_screen
from htmlnode import HTMLNode, LeafNode, ParentNode
from pathlib import Path



def absolute_path(path):
    if os.path.isabs(path):
        abs_path = path
    else:
        abs_path = os.path.abspath(path)

    return abs_path

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

def generate_page(from_path, template_path, dest_path, basepath = '/'):
    print(f'Generating page from {from_path} to {dest_path} using {template_path}')


    with open(from_path) as file:
        content = file.read()

    with open(template_path) as file:
        template = file.read()

    # convert markdown to html
    print('\nSTARTING PROCESS: MARKDOWN TO HTML NODE...')
    html_node = markdown_to_html_node(content)
    # print(html_node)
    html = html_node.to_html()

    # extract title from markdown
    title = extract_title(from_path)

    edited_template = template.replace("{{ Title }}",title).replace("{{ Content }}",html).replace('href="/',f'href="{basepath}').replace('src="/',f'src="{basepath}')

    # write into file
    with open(dest_path, 'w') as file:
        file.write(edited_template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath = '/'):

    print(f'\nBASEPATH: {basepath}')
    
    abs_dir_path_content = absolute_path(dir_path_content)
    abs_template_path = absolute_path(template_path)
    abs_dest_dir_path = absolute_path(dest_dir_path)

    print(abs_dir_path_content)
    print(abs_template_path)
    print(abs_dest_dir_path)

    contents = os.listdir(abs_dir_path_content)

    for content in contents:
        join_path_source = os.path.join(abs_dir_path_content, content)
        join_path_destination = os.path.join(abs_dest_dir_path, content)
        if os.path.isfile(join_path_source) and Path(join_path_source).suffix == '.md':
            join_path_destination_html = Path(join_path_destination).with_suffix('.html')
            generate_page(join_path_source, abs_template_path, join_path_destination_html,basepath)
            print(f'{join_path_destination_html} is generated')
        else:
            os.mkdir(join_path_destination)
            print(f'Directory {join_path_destination} is created\n')
            generate_pages_recursive(join_path_source, template_path, join_path_destination,basepath)
    


if __name__ == '__main__':
    clear_screen()
    # title = extract_title("content/index.md")
    # print(title)

    generate_pages_recursive('content','template.html','public')

    