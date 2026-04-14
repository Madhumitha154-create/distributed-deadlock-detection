class Site:
    def __init__(self, site_id):
        self.site_id = site_id
        self.wfg = {}

    def add_edge(self, from_p, to_p):
        if from_p not in self.wfg:
            self.wfg[from_p] = []
        self.wfg[from_p].append(to_p)

    def get_neighbors(self, process):
        return self.wfg.get(process, [])

    def get_graph(self):
        return self.wfg