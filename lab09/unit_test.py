from get_commands import get_commands
from weather import weather

def get_coords_test():
    assert get_coords('Gardner','MA') == False

def get_noaa_endpoint():
    assert get_coords('Gardner','MA') == False

def get_forecast():
    assert get_coords('Gardner','MA') == False
