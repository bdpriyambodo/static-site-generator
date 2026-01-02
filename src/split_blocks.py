from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"

def block_to_blocktype(block):
    prefix = ('# ', '## ', '### ', '#### ', '##### ', '###### ')
    if block.startswith(prefix):
        return BlockType.HEADING
    if block.startswith('```') and block.endswith('```'):
        return BlockType.CODE
    
    quote_check = []
    unordered_list_check = []
    ordered_list_check = []
    i = 1
    for line in block.splitlines():
        quote_check.append(line.startswith('> '))
        unordered_list_check.append(line.startswith('- '))
        # print(f'i: {i}')
        ordered_list_check.append(line.startswith(str(i)+'.'))
        i += 1

    # print(f'ordered list check: {ordered_list_check}')

    if all(quote_check):
        return BlockType.QUOTE
    if all(unordered_list_check):
        return BlockType.ULIST
    if all(ordered_list_check):
        return BlockType.OLIST
    
    return BlockType.PARAGRAPH

def markdown_to_blocks(markdown):
    blocks = markdown.split('\n\n')
    tidy_blocks = []
    for block in blocks:
        if block == "":
            continue
        tidy = block.replace('\n    ','\n')
        tidy_blocks.append(tidy.strip())
    
    return tidy_blocks


# markdown = """
#     # This is a heading

#     This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

#     - This is the first list item in a list block
#     - This is a list item
#     - This is another list item
#     """

# result = markdown_to_blocks(markdown)
# print(result)

# md = """
#     This is **bolded** paragraph

#     This is another paragraph with _italic_ text and `code` here
#     This is the same paragraph on a new line

#     - This is a list
#     - with items
#     """

# result = markdown_to_blocks(md)
# print(result)

## TEST
# block = '# TITLE'
# print(block_to_blocktype(block))

# block = '1. This is a list\n2. with items'
# print(block_to_blocktype(block))

