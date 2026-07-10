import tomllib
from dataclasses import dataclass
from pathlib import Path

project_root = Path(__file__).parent.parent
config_file = project_root / "global_config.toml"

with open(config_file, "rb") as f:
    _config = tomllib.load(f)

@dataclass(frozen=True)
class DisplayConfig:
    mosi_pin = _config["Display"]["mosi_pin"]
    clk_pin = _config["Display"]["clk_pin"]
    cs_pin = _config["Display"]["cs_pin"]
    dc_pin = _config["Display"]["dc_pin"]
    rst_pin = _config["Display"]["rst_pin"]

@dataclass(frozen=True)
class ButtonConfig:
    confirm_button_pin = _config["Buttons"]["confirm_button_pin"]
    shutdown_button_pin = _config["Buttons"]["shutdown_button_pin"]

@dataclass(frozen=True)
class GlobalConfig:
    gpio_mode = _config["Global"]["gpio_mode"]
    emulator = _config["Global"]["emulator"]

@dataclass(frozen=True)
class Settings:
    display = DisplayConfig()
    buttons = ButtonConfig()
    global_config = GlobalConfig()

settings = Settings()

if settings.global_config.emulator:
    print("Emulator enabled.")