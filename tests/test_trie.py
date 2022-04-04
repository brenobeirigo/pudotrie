from pudotrie import pudotrie as trie

def test_add_sequences():
    t = trie.Trie()
    t.add_sequences([[1]])
    print(t)
    assert dict({1:{None:{}}}) == t.tree
    
    t.add_sequences([[1], [2]])
    print(t)
    assert dict({1:dict({None:{}}), 2:dict({None:{}})}) == t.tree
    
    t.add_sequences([[1,2,3], [2,4,5]])
    print(t)
    assert {1:{2:{3:{None:{}}},None:{}}, 2:{4:{5:{None:{}}},None:{}}} == t.tree
    
    t.add_sequences([[1,2,3,4,5], [1,2,3,4,6]])
    print(t)
    assert {1:{2:{3:{None:{},4:{6:{None:{}},5:{None:{}}}}},None:{}}, 2:{4:{5:{None:{}}},None:{}}} == t.tree

def test_get_tree_starts_with_sequence():
    t = trie.Trie()
    t.add_entry([1])
    tree1 = t.get_tree_starts_with_sequence([])
    print(tree1)
    assert {1:{None:{}}} == tree1
    
    t.add_sequences([[1,2,3,4,5], [1,2,3,4,6], [1,4]])
    tree2 = t.get_tree_starts_with_sequence([1])
    print(tree2)
    assert {None:{}, 2:{3:{4:{5:{None:{}}, 6:{None:{}}}}}, 4:{None:{}}} == tree2
    
def test_all_sequences_from_tree():
    t = trie.Trie()
    
    t.add_sequences([[1]])
    print(t)
    t.add_sequences([[1,2,3,4,5], [1,2,3,4,6], [1,4]])
    print(t)
    tree = t.get_all_sequences_from_tree()
    print(tree)
    assert {(1,),(1,2,3,4,5), (1,2,3,4,6), (1,4)} == tree
    
