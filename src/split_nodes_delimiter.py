from textnode import TextType, TextNode
from extract_markdown import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
        else:
            text = old_node.text
            if (text.count(delimiter) % 2 != 0):
                raise Exception('Invalid Markdown syntax')
            else:
                new_list = []
                split_text = text.split(delimiter)
                # print(f'split_text: {split_text}')
                # new_list.append(TextNode(split_text[0], TextType.TEXT))
                # new_list.append(TextNode(split_text[1], text_type))
                # new_list.append(TextNode(split_text[2], TextType.TEXT))

                for i in range(len(split_text)):
                    if split_text[i] == "":
                        continue
                    if i % 2 == 0:
                        new_list.append(TextNode(split_text[i], TextType.TEXT))
                        # print(new_list)
                    else:
                        new_list.append(TextNode(split_text[i], text_type))

            new_nodes.extend(new_list)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        text = old_node.text
        matches = extract_markdown_links(text)

        if len(matches) == 0:
            new_nodes.append(TextNode(text, TextType.TEXT))
            continue

        new_list = []
        for match in matches:
            sections = text.split(f"[{match[0]}]({match[1]})",1)
            if len(sections) != 2:
                raise ValueError('invalid markdown')
            if sections[0] != "":
                new_list.append(TextNode(sections[0],TextType.TEXT))
            new_list.append(TextNode(match[0], TextType.LINK, match[1]))
            text = sections[1]
        if text != "":
            new_list.append(TextNode(text, TextType.TEXT))
        new_nodes.extend(new_list)

    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        text = old_node.text
        matches = extract_markdown_images(text)

        if len(matches) == 0:
            new_nodes.append(TextNode(text, TextType.TEXT))
            continue

        new_list = []
        for match in matches:
            sections = text.split(f"![{match[0]}]({match[1]})",1)
            if len(sections) != 2:
                raise ValueError('invalid markdown')
            if sections[0] != "":
                new_list.append(TextNode(sections[0],TextType.TEXT))
            new_list.append(TextNode(match[0], TextType.IMAGE, match[1]))
            text = sections[1]
        if text != "":
            new_list.append(TextNode(text, TextType.TEXT))
        new_nodes.extend(new_list)

    return new_nodes
                
def text_to_textnodes(text):
    initial = [TextNode(text, TextType.TEXT)]
    aft_delimiter_bold = split_nodes_delimiter(initial, '**', TextType.BOLD)
    aft_delimiter_italic = split_nodes_delimiter(aft_delimiter_bold, '_', TextType.ITALIC)
    aft_delimiter_code = split_nodes_delimiter(aft_delimiter_italic, '`', TextType.CODE)

    # print(f'after delimiter split: {aft_delimiter_code} \n')

    aft_link = split_nodes_link(aft_delimiter_code)
    # print(f'after link split: {aft_link}\n')
    aft_image = split_nodes_image(aft_link)

    return aft_image

text = 'This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)'
result = text_to_textnodes(text)
print(result, '\n')


# node = TextNode("This is text with a **bolded** word and **another**", TextType.TEXT)
# new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
# print(f'new nodes: {new_nodes}')  
# 

# Test split_nodes_link
# node = TextNode(
#     "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
#     TextType.TEXT,
# )
# new_nodes = split_nodes_link([node])
# print(new_nodes)
# [
#     TextNode("This is text with a link ", TextType.TEXT),
#     TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
#     TextNode(" and ", TextType.TEXT),
#     TextNode(
#         "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
#     ),
# ]    

# node = TextNode(
#     "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows",
#     TextType.TEXT,
# )
# new_nodes = split_nodes_link([node])
# print(new_nodes, "\n")

# Test split_nodes_image
# print('TEST split nodes image')

# node = TextNode(
#     "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
#     TextType.TEXT,
# )
# new_nodes = split_nodes_image([node])
# print(new_nodes)

# node = TextNode(
#     "![image](https://www.example.COM/IMAGE.PNG)",
#     TextType.TEXT,
# )
# new_nodes = split_nodes_image([node])
# print(new_nodes, "\n")