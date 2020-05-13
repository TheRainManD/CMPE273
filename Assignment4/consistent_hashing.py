import bisect
import hashlib 
import sys

class consistent_hashing(object):
    def __init__(self, nodes = None, replicate = 2):
        self.replicate = replicate
        self.ring = dict()
        self.keys = []
        if nodes:
            for node in nodes:
                self.add_node(node)

    def hash_key(self, key):
        x = hashlib.md5()
        x.update(key.encode('utf-8'))
        return int(x.hexdigest(), 16)

    def add_node(self, node):
        for i in range(0, self.replicate):
            key = self.hash_key('%s:%s' % (node, i))
            self.ring[key] = node
            self.keys.append(key)
        self.keys.sort()

    def remove_node(self, node):
        for i in range(0, self.replicate):
            key = self.hash_key('%s:%s' % (node, i))
            del self.ring[key]
            self.keys.remove(key)

    def get_node_position(self, value):
        if not self.ring:
            return None, None
        key = self.hash_key(value)
        nodes = self.keys
        for i in range(0, len(nodes)):
            node = nodes[i]
            if key <= node:
                return self.ring[node], i 
        return self.ring[nodes[0]], 0

    def get_node(self, value):
        return self.get_node_position(value)[0]
    
    def get_nodes(self, value):
        if not self.ring:
            return None, None
        node, position = self.get_node_position(value)
        for key in self.keys[position:]:
            yield self.ring[key]


def test():
    cache_servers = ['192.168.0.123:214',
                     '192.168.0.153:672',
                     '192.168.0.199:777',
                     '192.168.0.162:220',
                     '192.168.0.175:330']
    #ring = consistent_hashing(cache_servers, 1) give different parameter for replicate
    ring = consistent_hashing(cache_servers)
    position = ring.get_node_position('192.168.0.175:330')
    print(position)
    server = ring.get_nodes('1')
    server_lst = list(server)
    print(server_lst)
    server_2 = ring.get_nodes('3')
    server_lst_2 = list(server_2)
    print(server_lst_2)

test()