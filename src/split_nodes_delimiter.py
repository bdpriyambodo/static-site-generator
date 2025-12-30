from textnode import TextType, TextNode

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
                        print(new_list)
                    else:
                        new_list.append(TextNode(split_text[i], text_type))

            new_nodes.extend(new_list)
    return new_nodes


# node = TextNode("This is text with a **bolded** word and **another**", TextType.TEXT)
# new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
# print(f'new nodes: {new_nodes}')          

