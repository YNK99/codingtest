def solution(cacheSize, cities):
    
    cache = []
    t = 0
    
    for city in cities:
        
        city = city.lower()
        
        if city in cache:
            t += 1
            cache.remove(city)
        else:
            t += 5
            
        cache.append(city)
        
        if len(cache) > cacheSize:
            cache.pop(0)
            
    return t