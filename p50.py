#!/usr/bin/env python3


class Subtree:
    def __init__(self, top_node, symbol, prob, left, right):
        self.top_node = top_node
        self.symbol = symbol
        self.prob = prob
        self.left = left
        self.right = right


global prob_dict


def get_prob(symb):
    return symb[1]


def get_prob_of_item(item):
    return prob_dict.get(item[0])


def get_probabilities(h):
    prob = []
    sum = 0
    count = 0
    for symbol, value in h:
        sum += value
        count += 1
    for symbol, value in h:
        prob.append([symbol, (value / sum)])
    prob.sort(key=get_prob, reverse=True)
    return prob


def find_insert_index(htree, prob):
    for i in range(0, len(htree) - 1):
        if htree[i].prob > prob:
            if htree[i+1].prob < prob:
                return i + 1
            else:
                return i + 2
    return 0


def find_top_node(htree, prob):
    for i in range(1, len(htree) - 1):
        if htree[i].prob == prob:
            return htree[i]
    return None


def generate_prob_dict(prob):
    new_dict = {}
    for item in prob:
        new_dict[item[0]] = item[1]
    return new_dict


def generate_huffmann_tree(h):
    global prob_dict
    prob = get_probabilities(h)
    prob_dict = generate_prob_dict(prob)
    htree = []

    for i in range(len(prob)):
        node = Subtree(None, prob[i][0], prob[i][1], None, None)
        htree.append(node)

    i = len(prob) - 2
    while i >= 1:
        new_prob = htree[i].prob + htree[i+1].prob
        index = find_insert_index(htree, new_prob)
        top_node = find_top_node(htree, new_prob)
        node = Subtree(top_node, "Branch", new_prob, htree[i+1], htree[i])
        htree.insert(index, node)
        htree.pop(-1)
        if len(htree) > 2:
            htree.pop(-1)
        i -= 1

    node = Subtree(None, "Root", htree[0].prob +
                   htree[1].prob, htree[1], htree[0])
    htree.insert(0, node)
    htree.pop(-1)
    htree.pop(-1)
    return htree[0]


def print_huffmann_tree(htree, indent=1):
    print("  "*indent, end="")
    print(htree.symbol, "{:.2f}".format(htree.prob))
    if htree.left != None:
        print_huffmann_tree(htree.left, indent + 1)
    if htree.right != None:
        print_huffmann_tree(htree.right, indent + 1)


def get_huffmann_table(htree, htree_list=[], code=""):
    if htree.symbol == "Root" or htree.symbol == "Branch":
        get_huffmann_table(htree.left, htree_list, code + "0")
        get_huffmann_table(htree.right, htree_list, code + "1")
        return htree_list
    else:
        return htree_list.append([htree.symbol, code])


def make_huffmann_code_table(htree):
    htree_as_list = get_huffmann_table(htree)
    htree_as_list.sort(key=get_prob_of_item, reverse=True)
    return htree_as_list


# P50: Huffman code.
def p50(h):
    htree = generate_huffmann_tree(h)
    print_huffmann_tree(htree)
    htable = make_huffmann_code_table(htree)
    return htable


if __name__ == "__main__":
    ret = p50([["A", 45], ["B", 13], ["C", 12], ["D", 16], ["E", 9], ["F", 5]])
    print(ret)
