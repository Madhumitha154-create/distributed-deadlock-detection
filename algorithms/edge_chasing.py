from models.probe import Probe

class EdgeChasingDetector:
    def __init__(self, sites):
        self.sites = sites
        self.visited_probes = set()
        self.deadlock_detected = False
        self.logger = None

    def send_probe(self, probe):
        key = (probe.initiator, probe.sender, probe.receiver)

        if key in self.visited_probes:
            return

        self.visited_probes.add(key)

        # 🔥 LOG PROBE
        log_msg = f"📡 {probe}"

        if hasattr(self, 'logs'):
            self.logs.append(log_msg)

        if self.logger:
            self.logger.text("\n".join(self.logs))

        # DEADLOCK CONDITION
        if probe.receiver == probe.initiator:
            self.deadlock_detected = True
            return

        for site in self.sites:
            neighbors = site.get_neighbors(probe.receiver)

            for neighbor in neighbors:
                new_probe = Probe(probe.initiator, probe.receiver, neighbor)
                self.send_probe(new_probe)