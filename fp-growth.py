class FPTreeNode:
    def __init__(self, item, frequency, parent=None):
        self.item = item
        self.frequency = frequency
        self.parent = parent
        self.children = {}
        self.link = None

    def add_frequency(self, frequency):
        self.frequency += frequency

    def display(self, level=0):
        print(' ' * level, self.item, ' ', self.frequency)
        for child in self.children.values():
            child.display(level+1)

def build_FP_tree(transactions, min_support):
    item_counts = {}
    for transaction in transactions:
        for item in transaction:
            item_counts[item] = item_counts.get(item, 0) + 1
    item_counts = {item: frequency for item, frequency in item_counts.items() if frequency >= min_support}
    frequent_items = set(item_counts.keys())
    header_table = {item: [frequency, None] for item, frequency in item_counts.items()}
    root = FPTreeNode(None, 0)
    for transaction in transactions:
        transaction = [item for item in transaction if item in frequent_items]
        transaction.sort(key=lambda item: header_table[item][0], reverse=True)
        current_node = root
        for item in transaction:
            if item in current_node.children:
                child_node = current_node.children[item]
            else:
                child_node = FPTreeNode(item, 0, current_node)
                current_node.children[item] = child_node
                if header_table[item][1] is None:
                    header_table[item][1] = child_node
                else:
                    node = header_table[item][1]
                    while node.link is not None:
                        node = node.link
                    node.link = child_node
            child_node.add_frequency(1)
            current_node = child_node
    return root, header_table

def mine_FP_tree(header_table, prefix, min_support):
    frequent_items = []
    items = [item for item, node in header_table.items() if node[0] >= min_support]
    items.sort(key=lambda item: header_table[item][0])
    for item in items:
        frequency, node = header_table[item]
        new_prefix = prefix + [item]
        frequent_items.append((new_prefix, frequency))
        conditional_base = []
        while node is not None:
            path = []
            current_node = node.parent
            while current_node.item is not None:
                path.append(current_node.item)
                current_node = current_node.parent
            if path:
                conditional_base.append((path, node.frequency))
            node = node.link
        conditional_tree, conditional_header_table = build_FP_tree([path for path, frequency in conditional_base], min_support)
        if conditional_tree is not None:
            frequent_items.extend(mine_FP_tree(conditional_header_table, new_prefix, min_support))
    return frequent_items

def FP_growth(transactions, min_support):
    fp_tree, header_table = build_FP_tree(transactions, min_support)
    frequent_items = mine_FP_tree(header_table, [], min_support)
    return frequent_items

transactions = [
    ['bread', 'milk', 'cheese', 'apples', 'yogurt'],
    ['diapers', 'beer', 'eggs', 'orange juice', 'shampoo', 'toilet paper'],
    ['bread', 'milk', 'diapers', 'beer', 'chips', 'soda', 'ice cream'],
    ['milk', 'diapers', 'beer', 'cola'],
    ['bread', 'milk', 'diapers', 'cola', 'chocolate'],
]
min_support = 2
frequent_itemsets = FP_growth(transactions, min_support)
frequent_itemsets_by_size = {}
for itemset, support in frequent_itemsets:
    size = len(itemset)
    if size not in frequent_itemsets_by_size:
        frequent_itemsets_by_size[size] = []
    frequent_itemsets_by_size[size].append((itemset, support))
for size in sorted(frequent_itemsets_by_size.keys()):
    print(f"Frequent itemsets of size {size}:")
    for itemset, support in frequent_itemsets_by_size[size]:
        print(f"{itemset} :{support}")