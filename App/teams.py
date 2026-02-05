class Team:
    def __init__(self, name: str, pid: str):
        self.name = name            # team number (string or int)
        self.pid = pid              # hex pager ID (as string)

    def __repr__(self):
        return f"Team(name={self.name}, pid={self.pid})"
