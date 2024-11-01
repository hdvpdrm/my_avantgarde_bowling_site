from argparser import Parser
from server import Server


if __name__ == "__main__":
    parser = Parser()
    svr = Server(parser.get_port())
    svr.run()
