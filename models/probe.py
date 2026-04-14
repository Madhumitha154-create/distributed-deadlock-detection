class Probe:
    def __init__(self, initiator, sender, receiver):
        self.initiator = initiator
        self.sender = sender
        self.receiver = receiver

    def __repr__(self):
        return f"Probe({self.initiator} → {self.sender} → {self.receiver})"