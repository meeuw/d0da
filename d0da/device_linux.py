import pyudev
import d0da.helper
import d0da.hidraw


class Device:
    def __init__(self, parent):
        self.devices = []
        self.context = pyudev.Context()
        self.parent = pyudev.Devices.from_path(self.context, parent)
        self.open()

    def open(self):
        for udev in self.context.list_devices(parent=self.parent, subsystem="hidraw"):
            device_handle = open(udev.device_node, "wb+")
            self.devices.append(device_handle)
            hidraw = d0da.hidraw.HIDRaw(device_handle)

            # fmt: off
            desc5 = [6, 0, 255, 9, 1, 161, 1, 9, 2, 21, 0, 38, 255, 0, 117, 8, 149, 8, 129, 2, 192]
            desc4 = [5, 1, 9, 6, 161, 1, 5, 8, 21, 0, 37, 1, 117, 1, 149, 5, 25, 1, 41, 5, 145, 2, 117, 3, 149, 1, 145, 1, 5, 7, 21, 0, 37, 1, 117, 1, 149, 8, 25, 224, 41, 231, 129, 2, 117, 1, 149, 46, 25, 4, 41, 49, 129, 2, 117, 2, 149, 1, 129, 1, 117, 1, 149, 105, 25, 51, 41, 155, 129, 2, 117, 7, 149, 1, 129, 1, 117, 1, 149, 8, 25, 157, 41, 164, 129, 2, 117, 1, 149, 46, 25, 176, 41, 221, 129, 2, 117, 2, 149, 1, 129, 1, 192]
            desc3 = [6, 55, 19, 9, 1, 161, 1, 9, 2, 21, 0, 38, 255, 0, 117, 8, 150, 0, 1, 129, 2, 9, 4, 150, 0, 1, 145, 2, 9, 6, 149, 7, 177, 2, 192]
            desc2 = [5, 1, 9, 128, 161, 1, 133, 1, 25, 129, 41, 131, 21, 1, 37, 3, 149, 1, 117, 8, 129, 0, 192, 5, 12, 9, 1, 161, 1, 133, 2, 25, 1, 42, 162, 2, 21, 1, 38, 162, 2, 149, 3, 117, 16, 129, 0, 192, 5, 1, 9, 2, 161, 1, 133, 3, 9, 1, 161, 0, 5, 9, 25, 1, 41, 5, 21, 0, 37, 1, 117, 1, 149, 5, 129, 2, 149, 3, 129, 3, 5, 1, 9, 48, 9, 49, 21, 129, 37, 127, 117, 8, 149, 2, 129, 6, 192, 192]
            desc1 = [6, 84, 255, 9, 1, 161, 1, 9, 2, 21, 0, 38, 255, 0, 117, 8, 149, 48, 129, 2, 192]
            # fmt: on

            if hidraw.getRawReportDescriptor() == desc3:
                # put control interface first
                self.devices[0], self.devices[-1] = self.devices[-1], self.devices[0]

    def close(self):
        for device in self.devices:
            device.close()
        self.devices = []

    def send_buffer(self, payload):
        device_handle = self.devices[0]
        for packet in d0da.helper.create_packets(payload, 64, 4):
            device_handle.write(b"\x00" + packet)
            device_handle.flush()

    def send_feature(self, payload):
        device_handle = self.devices[0]
        hidraw = d0da.hidraw.HIDRaw(device_handle)
        for packet in d0da.helper.create_packets(payload, 7, 1):
            hidraw.sendFeatureReport(packet)
        return device_handle.read(128) + device_handle.read(128)


def list_devices():
    context = pyudev.Context()
    for device in context.list_devices(DEVTYPE="usb_device"):
        if device.attributes.get("manufacturer") == b"Wooting":
            yield device


def get_device(parent):
    return Device(parent)
