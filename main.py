from App import App


def main() -> None:
    app = App.get_instance()
    app.start()


if __name__ == "__main__":
    main()
