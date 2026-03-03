class AgentMemory:
    def __init__(self):
        self._state = {}

    def store(self, key: str, value):
        self._state[key] = value

    def get(self,key: str):
        return self._state.get(key)
    
    def get_all(self):
        return self._state
    
    def clear(self):
        self._state = {}