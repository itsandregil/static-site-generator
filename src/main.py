from text_node import TextNode, TextType


def main():
    node = TextNode("This is a dummy node", TextType.PLAIN)
    print(node)


if __name__ == "__main__":
    main()
