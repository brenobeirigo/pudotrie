class Trie:
        
    def __init__(self):
        self.tree = {}
    
    def get_all_sequences_from_tree(self, tree=None):
        
        all_sequences = set()
        
        def visit_children(tree, sub_sequence=[]):
                
                
            if not tree:
                all_sequences.add(tuple(sub_sequence))
                return

            for node,sub_tree in tree.items():
                if node == None:
                    all_sequences.add(tuple(sub_sequence))
                    continue
                    
                seq = list(sub_sequence)
                seq.append(node)
                visit_children(sub_tree, sub_sequence=seq)

        if not tree:
            tree = self.tree
        
        visit_children(tree)
        
        return all_sequences
        
    def get_tree_starts_with_sequence(self, sequence):
        tree = self.tree
        for node in sequence:
            if node not in tree:
                return tree.values()
            else:
                sub_tree = tree[node] 
                tree = sub_tree
        return tree
    
    def starts_with_sequence(self, sequence):
        tree = self.get_tree_starts_with_sequence(sequence)
        return self.get_all_sequences_from_tree(tree)
        
    def add_entry(self, sequence):
        
        tree = self.tree
        
        for node in sequence:
            
            if node not in tree:
                tree[node] = dict()
            
            sub_tree = tree[node]
            tree = sub_tree
        
        # End of sequence
        # TODO {1:{None:{arrival_time=3}}}
        tree[None] = dict()
    
    def __str__(self):
        return "{"+",".join(map(str,self.get_all_sequences_from_tree()))+"}"
    
    def __repr__(self):
        return self.__str__()
    
    def add_sequences(self, sequences):
        for sequence in sequences:
            self.add_entry(sequence)