import argparse


class Parser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="local server  to process sqlite data base")
        self.parser.add_argument("port",type=int,help="port to listen.")
        self.__args = self.parser.parse_args()

    def get_port(self) -> int:
        return self.__args.port
