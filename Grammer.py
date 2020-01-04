class Grammer:
    def __init__(self):
        self.grammer   = {}
        self.grammer_d = {}
        self.grammer_list = []

    def add_grammer(self, parent:str, children:[]):
        self.grammer.update({parent:children})
        self.grammer_list.append({'p': parent, 'c': children})
        for child in children:
            cv = self.grammer_d.setdefault(child, [])
            cv.append(parent)
            self.grammer_d.update({child:cv})

    def get_grammer_by_parent(self, p:str):
        return self.grammer.get(p) or []

    def get_grammer_by_child(self, c:str):
        return self.grammer_d.get(c) or []

    def get_grammer(self):
        return self.grammer_list

