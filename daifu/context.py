
class Context():
    def __init__(self, kwlocals):
        self.locals = {}
        self.exception = None

        for key, value in kwlocals.items():
            if isinstance(value, Exception):
                self.exception = value
            else:
                self.locals[key] = value
    
class ContextManager():
    def __init__(self):
        self.queue = []

    def save(self, kwlocals):
        print('Context Saving')
        self.queue.append(Context(kwlocals))

    def get_current(self):
        return self.queue[-1]
        

CT_MANAGER = ContextManager()