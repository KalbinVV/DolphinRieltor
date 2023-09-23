import os.path

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
