from frontend.app import app
from frontend.config import config


def main():
    app.run(host=config.host, port=config.port)


if __name__ == '__main__':
    main()
