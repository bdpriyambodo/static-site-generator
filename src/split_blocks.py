

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
