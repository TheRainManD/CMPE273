LRUcache_container = []

def lru_cache(size):
    def inner(function):
        def wrapper(*args):            
            i = 0
            while(i < len(LRUcache_container)):
                lru_obj = LRUcache_container[i]
                if lru_obj['parameter'] == args:
                    print("cache hit")
                    del LRUcache_container[i]
                    LRUcache_container.append(lru_obj)
                    return lru_obj["data"]
                i = i + 1
            data = function(*args)
            lru_obj = {'parameter': args, 'data': data}
            if(len(LRUcache_container) < size):
                LRUcache_container.append(lru_obj)
            else:
                del LRUcache_container[0]
                LRUcache_container.append(lru_obj)
            return data
        return wrapper
    return inner
