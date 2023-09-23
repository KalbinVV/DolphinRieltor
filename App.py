import os.path
import tkinter
from typing import Optional

import customtkinter
import tkintermapview

from Events import Events


class App(customtkinter.CTk):
    __instance = None

    APP_NAME = "DolphinRieltor - Версия 0.1"
    WIDTH = 800
    HEIGHT = 500
    VERSION = '0.1'
    DEFAULT_ADDRESS = 'Оренбург'

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = App()
        return cls.__instance

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title(App.APP_NAME)
        self.geometry(str(App.WIDTH) + "x" + str(App.HEIGHT))
        self.minsize(App.WIDTH, App.HEIGHT)

        self.__map_widget: Optional[tkintermapview.TkinterMapView] = None

        self.__upper_frame: Optional[customtkinter.CTkFrame] = None
        self.__search_entry: Optional[customtkinter.CTkEntry] = None

        self.__server_choose_frame: Optional[customtkinter.CTkFrame] = None
        self.__server_option_menu: Optional[customtkinter.CTkOptionMenu] = None

        self.__left_frame: Optional[customtkinter.CTkFrame] = None

        self.__init_map()
        self.__init_upper_panel()
        self.__init_server_choose_panel()
        self.__init_left_panel()

    def __init_map(self):
        self.__map_widget = tkintermapview.TkinterMapView(self, width=self.WIDTH, height=self.HEIGHT,
                                                          corner_radius=0)
        self.__map_widget.pack(fill="both", expand=True)

        self.__map_widget.set_address(self.DEFAULT_ADDRESS)

        self.__map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)

        self.__map_widget.add_right_click_menu_command("Добавить здание",
                                                       command=lambda x: print(tkintermapview.convert_coordinates_to_address(x[0], x[1])),
                                                       pass_coords=True)

    def __init_upper_panel(self):
        self.__upper_frame = customtkinter.CTkFrame(master=self, width=700, height=30)

        self.__upper_frame.place(relx=0.5, rely=0.02, anchor='n', relwidth=0.7)

        self.__search_entry = customtkinter.CTkEntry(self.__upper_frame,
                                                     width=400,
                                                     height=30,
                                                     corner_radius=0,
                                                     font=('monospace', 14))

        self.__search_entry.bind("<Return>", Events.on_search)

        search_button = customtkinter.CTkButton(self.__upper_frame,
                                                width=100,
                                                height=30,
                                                text='Поиск',
                                                corner_radius=0,
                                                font=(self.MAIN_FONT_FAMILY, 14),
                                                command=Events.on_search)

        self.__search_entry.pack(side=tkinter.LEFT, fill="both", expand=1)

        search_button.pack(side=tkinter.RIGHT)

    def __init_server_choose_panel(self):
        self.__server_choose_frame = customtkinter.CTkFrame(master=self,
                                                   width=100,
                                                   height=300,
                                                   fg_color='white')

        self.__server_choose_frame.place(relx=0.02, rely=0.9, anchor='sw')

        select_tiles_server_label = customtkinter.CTkLabel(self.__server_choose_frame,
                                                           text="Cервер:")

        self.__server_option_menu = customtkinter.CTkOptionMenu(self.__server_choose_frame,
                                                                values=[
                                                                    "Google",
                                                                    "Google (Спутник)",
                                                                    "OpenStreetMap",
                                                                    "ЧБ"],
                                                                corner_radius=0,
                                                                command=Events.on_server_change)

        select_tiles_server_label.pack()
        self.__server_option_menu.pack()

    def __init_left_panel(self):
        self.__left_frame = customtkinter.CTkFrame(self, width=100, height=700, fg_color='white')

        self.__left_frame.place(relx=0.02, rely=0.45, anchor='w')

        search_label = customtkinter.CTkLabel(self.__left_frame,
                                              text="Настройки поиска:",
                                              font=('monospace', 14))

        search_label.pack(padx=10, pady=10, anchor="w")

        search_apartments_switch = customtkinter.CTkSwitch(self.__left_frame,
                                                           text="Отображать квартиры")

        search_homes_switch = customtkinter.CTkSwitch(self.__left_frame,
                                                      text="Отображать дома")

        search_already_rented = customtkinter.CTkSwitch(self.__left_frame,
                                                        text="Отображать уже арендованные")

        search_apartments_switch.pack(padx=10, pady=10, anchor="w")
        search_homes_switch.pack(padx=10, pady=10, anchor="w")
        search_already_rented.pack(padx=10, pady=10, anchor="w")

    def get_search_value(self):
        return self.__search_entry.get()

    def set_location(self, address: str):
        self.__map_widget.set_address(address)

    def get_server_value(self):
        return self.__server_option_menu.get()

    def set_server(self, address: str, zoom_value: Optional[int] = None):
        if zoom_value is not None:
            self.__map_widget.set_tile_server(address, max_zoom=zoom_value)
        else:
            self.__map_widget.set_tile_server(address)

    def start(self):
        self.mainloop()
