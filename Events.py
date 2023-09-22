class Events:
    @classmethod
    def __get_app_instance(cls):
        from App import App

        return App.get_instance()

    @classmethod
    def on_search(cls, event=None):
        app = cls.__get_app_instance()

        app.set_location(app.get_search_value())

    @classmethod
    def on_server_change(cls, event=None):
        app = cls.__get_app_instance()

        server_value = app.get_server_value()

        server_addresses_map = {
            'Google': ('https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga', 22),
            'Google (Спутник)': ('https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga', 22),
            'OpenStreetMap': ('https://a.tile.openstreetmap.org/{z}/{x}/{y}.png', None)
        }

        address, zoom_value = server_addresses_map[server_value]

        app.set_server(address, zoom_value)



