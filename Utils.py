import os.path
import tkinter

import customtkinter
from PIL import Image

ASSETS_PATH = "assets"


def get_path_from_assets(file_name: str) -> str:
    return os.path.join(ASSETS_PATH, file_name)


def get_asset_image(file_name: str) -> Image:
    return Image.open(get_path_from_assets(file_name))


def get_ctk_image(file_name: str, size: tuple[int, int]) -> customtkinter.CTkImage:
    image = get_asset_image(file_name)

    return customtkinter.CTkImage(light_image=image,
                                  dark_image=image,
                                  size=size)


def create_input_frame(parent_frame: tkinter.Frame, width: int, height: int, fg_color: str,
                       text: str, placeholder_text: str = "",
                       padx: int = 5, pady: int = 5) -> customtkinter.CTkEntry:
    input_frame = customtkinter.CTkFrame(parent_frame,
                                         width=width,
                                         height=height,
                                         fg_color=fg_color)

    label = customtkinter.CTkLabel(input_frame,
                                   text=text)
    entry = customtkinter.CTkEntry(input_frame,
                                   placeholder_text=placeholder_text)

    label.pack(expand=1, fill="x")
    entry.pack(expand=1, fill="x")

    input_frame.pack(expand=1, fill="x", padx=padx, pady=pady)

    return entry
