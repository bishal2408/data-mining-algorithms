from itertools import combinations
from collections import defaultdict
# Generate candidate itemsets of size k+1 from frequent itemsets of size k


def generate_candidates(frequent_itemsets, k):
    candidates = set()
    for i in frequent_itemsets:
        for j in frequent_itemsets:
            if len(i.union(j)) == k+1:
                candidates.add(i.union(j))
    return candidates
# Get support count for each candidate itemset


def get_support_count(transactions, candidates, min_support):
    counts = defaultdict(int)
    for transaction in transactions:
        for candidate in candidates:
            if candidate.issubset(transaction):
                counts[candidate] += 1
    return {itemset: count for itemset, count in counts.items() if count >= min_support}
# Generate frequent itemsets of size k


def apriori(transactions, min_support):
    itemsets = [frozenset([item]) for item in set([item for transaction in transactions for item in
                                                   transaction])]
    frequent_itemsets = {itemset: count for itemset, count in get_support_count(transactions,
                                                                                itemsets, min_support).items()}
    k = 1
    while frequent_itemsets:
        yield frequent_itemsets, k
        k += 1
        candidates = generate_candidates(frequent_itemsets.keys(), k-1)
        frequent_itemsets = {itemset: count for itemset, count in
                         get_support_count(transactions, candidates, min_support).items()}


# Example usage
transactions = [
    ['milk', 'diapers'],
    ['eggs', 'beer', 'diapers'], 
    ['bread', 'milk', 'beer', 'diapers'], 
    ['cola', 'milk', 'diapers'], 
    ['eggs', 'bread', 'milk', 'beer']
]

min_support = 2
for frequent_itemsets, k in apriori(transactions, min_support):
    print(f"Frequent Itemsets of size {k}:")
    for itemset, count in frequent_itemsets.items():
        print(f"{list(itemset)} : {count}")
    print()