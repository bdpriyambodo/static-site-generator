from split_blocks import markdown_to_blocks, block_to_blocktype, BlockType
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import text_node_to_html_node, TextNode, TextType
from split_nodes_delimiter import text_to_textnodes

import os

def clear_screen():
    # Check the operating system name
    if os.name == 'nt':
        # Command for Windows
        _ = os.system('cls')
    else:
        # Command for Mac and Linux (posix)
        _ = os.system('clear')

def text_to_children(text):
    textnodes = text_to_textnodes(text)
    htmlnodes = []
    for textnode in textnodes:
        htmlnodes.append(text_node_to_html_node(textnode))
    return htmlnodes

def markdown_to_html_node(markdown):
    
    print(f'ORIGINAL MARKDOWN:\n{markdown}')

    # CONVERT MARKDOWN TO BLOCKS
    blocks = markdown_to_blocks(markdown)
    print(f'AFTER MARKDOWN_TO_BLOCKS:\n{blocks}\n')

    # DETERMINE EACH BLOCK TYPE
    block_types = []
    block_nodes = []

    for block in blocks:
        blocktype = block_to_blocktype(block)
        block_types.append(blocktype)

        # print(f'ORIGINAL BLOCK: \n{block}\n')
        # print(f'AFTER CONVERTING TO TEXT NODE:\n{text_to_textnodes(block)}\n')

        # htmlnodes = text_to_children(block)
        # print(f'\nAFTER CONVERTING TO HTML NODES:\n{htmlnodes}')

        if blocktype == BlockType.PARAGRAPH:
            block_nodes.append(
                ParentNode(tag = "p", children = text_to_children(block.replace('\n',' ')))
                )
        if blocktype == BlockType.HEADING:
            if block.startswith('# '):
                block_nodes.append(
                    ParentNode(tag = "h1", children = text_to_children(block))
                    )
            elif block.startswith('## '):
                block_nodes.append(
                    ParentNode(tag = "h2", children = text_to_children(block))
                    )
            elif block.startswith('### '):
                block_nodes.append(
                    ParentNode(tag = "h3", children = text_to_children(block))
                    )
            elif block.startswith('#### '):
                block_nodes.append(
                    ParentNode(tag = "h4", children = text_to_children(block))
                    )
            elif block.startswith('##### '):
                block_nodes.append(
                    ParentNode(tag = "h5", children = text_to_children(block))
                    )
            else:
                block_nodes.append(
                    ParentNode(tag = "h6", children = text_to_children(block))
                    )
        if blocktype == BlockType.CODE:
            tidy_block = block.replace('```\n','```').replace('```','')
            print(f'tidy block: {tidy_block}')
            codeblock_textnode = TextNode(tidy_block,TextType.CODE)
            codeblock_htmlnode = text_node_to_html_node(codeblock_textnode)
            block_nodes.append(
                ParentNode(tag = "pre", children = [codeblock_htmlnode])
                )
        if blocktype == BlockType.QUOTE:
            block_nodes.append(
                ParentNode(tag = "blockquote", children = text_to_children(block))
                )
        if blocktype == BlockType.ULIST:
            block_nodes.append(
                ParentNode(tag = "ul", children = text_to_children(block))
                )
        if blocktype == BlockType.OLIST:
            block_nodes.append(
                ParentNode(tag = "ol", children = text_to_children(block))
                )
    print(f'AFTER BLOCK TYPE:\n{block_nodes}')
    
    all_nodes = ParentNode(tag = "div", children = block_nodes)

    return all_nodes

    # convert text to text node
    # text_to_textnodes_list = []
    # for block in blocks:
    #     text_to_textnodes_list.append(text_to_textnodes(block))
    
    # print(f'AFTER TEXT_TO_TEXTNODES:\n{text_to_textnodes_list}\n')

    # textnodes_to_htmlnodes_list = []
    # for textnode in text_to_textnodes_list:
    #     print(textnode)
    #     # textnodes_to_htmlnodes_list.append(text_node_to_html_node(textnode))
    
    # print(f'AFTER TEXT_NODE_TO_HTML_NODE: {textnodes_to_htmlnodes_list}\n')

    # create HTMLNode



# CLEAR TERMINAL
# clear_screen()

# # ACTUAL 
md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

result = markdown_to_html_node(md)
print('\n')
print(result)
print('\n')
print(result.to_html())
print('\n')

# CODE TEST
md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

# print(markdown_to_html_node(md))
result = markdown_to_html_node(md)
print('\nCODE BLOCK TEST')
print(result)
print('\n')
print(result.to_html())
print('\n')



