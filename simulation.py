import simpy
import random
from models.site import Site
from algorithms.edge_chasing import EdgeChasingDetector
from models.probe import Probe

class DistributedSimulation:
    def __init__(self, env, num_sites, processes_per_site):
        self.env = env
        self.sites = [Site(i) for i in range(num_sites)]
        self.processes = []
        self.logger = None
        self.logs = []
        pid = 0
        for site in self.sites:
            for _ in range(processes_per_site):
                self.processes.append((pid, site))
                pid += 1

    def set_logger(self, logger):
        self.logger = logger

    def generate_waits(self):
        while True:
            yield self.env.timeout(1)

            p1, site1 = random.choice(self.processes)
            p2, site2 = random.choice(self.processes)

            if p1 != p2:
                site1.add_edge(p1, p2)

                # 🔥 LOG WAIT
                log_msg = f"🔄 P{p1} waits for P{p2}"
                self.logs.append(log_msg)

                if self.logger:
                    self.logger.text("\n".join(self.logs))

    def detect_deadlock(self):
        detector = EdgeChasingDetector(self.sites)
        detector.logger = self.logger
        detector.logs = self.logs
        # 🔥 CONNECT LOGGER
        detector.logger = self.logger

        for (pid, site) in self.processes:
            neighbors = site.get_neighbors(pid)

            for neighbor in neighbors:
                probe = Probe(pid, pid, neighbor)
                detector.send_probe(probe)

        return detector.deadlock_detected