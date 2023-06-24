D0DA = b"\xd0\xda"


def ping():
    return D0DA + b"\x00"


def get_version():
    return D0DA + b"\x01"


def reset_to_bootloader():
    return D0DA + b"\x02"


def get_serial():
    return D0DA + b"\x03"


def get_rgb_profile_count():
    return D0DA + b"\x04"


def removed_get_current_rgb_profile_index():
    return D0DA + b"\x05"


def removed_get_rgb_main_profile():
    return D0DA + b"\x06"


def reload_profile0(index):
    return D0DA + bytes((0x07, index))


def save_rgb_profile():
    return D0DA + b"\x08"


def get_digital_profiles_count():
    return D0DA + b"\x09"


def get_analog_profiles_count():
    return D0DA + b"\x0a"


def get_current_keyboard_profile_index():
    return D0DA + b"\x0b"


def get_digital_profile():
    return D0DA + b"\x0c"


def get_analog_profile_main_part():
    return D0DA + b"\x0d"


def get_analog_profile_curve_change_map_part1():
    return D0DA + b"\x0e"


def get_analog_profile_curve_change_map_part2():
    return D0DA + b"\x0f"


def get_number_of_keys():
    return D0DA + b"\x10"


def get_main_mapping_profile():
    return D0DA + b"\x11"


def get_function_mapping_profile():
    return D0DA + b"\x12"


def get_device_config():
    return D0DA + b"\x13"


def get_analog_values():
    return D0DA + b"\x14"


def keys_off():
    return D0DA + b"\x15"


def keys_on():
    return D0DA + b"\x16"


def activate_profile(index):
    return D0DA + bytes((0x17, index))


def get_dks_profile():
    return D0DA + b"\x18"


def do_soft_reset():
    return D0DA + b"\x19"


def removed_get_rgb_colors_part1():
    return D0DA + b"\x1a"


def removed_get_rgb_colors_part2():
    return D0DA + b"\x1b"


def removed_get_rgb_effects():
    return D0DA + b"\x1c"


def refresh_rgb_colors(index):
    return D0DA + bytes(0x1D, index)


def woot_dev_single_color(row, column, red, green, blue):
    id = (row << 5) | column
    return D0DA + bytes((0x1E, blue, green, red, id))


def woot_dev_reset_color(row, column):
    id = (row << 5) | column
    return D0DA + bytes((0x1F, id))


def woot_dev_reset_all():
    """
    Reset keyboard to wootility mode (after woot_dev_init)
    """
    return D0DA + b"\x20"


def woot_dev_init():
    """
    Initialize mode to manually set the RGB array using
    d0da.d0da_report.rgb_array_update_keyboard()
    """
    return D0DA + b"\x21"


def get_rgb_profile_base():
    return D0DA + b"\x22"


def get_rgb_profile_color_part1():
    return D0DA + b"\x23"


def get_rgb_profile_color_part2():
    return D0DA + b"\x24"


def get_rgb_profile_effect():
    return D0DA + b"\x25"


def reload_profile():
    return D0DA + b"\x26"


def get_keyboard_profile():
    return D0DA + b"\x27"


def get_gamepad_mapping():
    return D0DA + b"\x28"


def get_gamepad_profile():
    return D0DA + b"\x29"


def save_keyboard_profile():
    return D0DA + b"\x2a"


def reset_flash():
    return D0DA + b"\x2b"


def set_raw_scanning():
    return D0DA + b"\x2c"


def start_xinput_detection():
    return D0DA + b"\x2d"


def stop_xinput_detection():
    return D0DA + b"\x2e"


def save_dks_profile():
    return D0DA + b"\x2f"


def get_mapping_profile():
    return D0DA + b"\x30"


def get_actuation_profile():
    return D0DA + b"\x31"


def get_rgb_profile_core():
    return D0DA + b"\x32"
