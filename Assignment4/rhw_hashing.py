import hashlib

class RendezvousHashing(object):
    def __init__(self, nodes):
        self.nodes = set(nodes)
    
    def hash(self, value):
        x = hashlib.md5()
        x.update(value.encode('utf-8'))
        return int(x.hexdigest(), 16)
 
    def weight(self, node, key):
        node_hash = hash(node)
        key_hash = hash(key)
        a = 1103515245
        b = 12345
        return (a * ((a * node_hash + b) ^ key_hash) + b) % (2 ^ 31)

    def hash_key(self, key):
        node_weights = []
        for node in self.nodes:
            node_weight = weight(node, key)
            node_weights.append[node_weight]
        return node

    def get_node(self, key):
        return self.nodes

    def add_node(self, node):
        self.nodes.add(node)
        return None