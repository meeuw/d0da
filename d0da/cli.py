import click
import d0da.device_linux as d0da_device
import d0da.helper
import d0da.d0da_feature
import d0da.d0da_report


@click.group()
def main():
    pass


@main.command()
def list_devices():
    for device in d0da_device.list_devices():
        click.echo(device)


@main.command()
@click.option("--device", required=True)
@click.option("--report", required=True)
@click.option("--value", required=True, multiple=True)
def d0da_report(device, report, value):
    device = d0da_device.get_device(device)

    pass_values = []
    for val in value:
        if val.startswith("rgb:"):
            pass_values.append(
                (int(val[4:6], 16), int(val[6:8], 16), int(val[8:10], 16))
            )
        elif val.startswith("rgbrow:"):
            row = []
            for rgbrow in val[7:].split(","):
                row.append(
                    (
                        int(rgbrow[0:2], 16),
                        int(rgbrow[2:4], 16),
                        int(rgbrow[4:6], 16),
                    )
                )
            pass_values.append(row)
        else:
            pass_values.append(int(val))

    try:
        payload = getattr(d0da.d0da_report, report)(*pass_values)
    except AttributeError:
        payload = None

    device.send_buffer(payload)


@main.command()
@click.option("--device", required=True)
@click.option("--feature", required=True)
@click.option("--value", multiple=True, type=int)
def d0da_feature(device, feature, value):
    device = d0da_device.get_device(device)

    payload = None

    try:
        payload = getattr(d0da.d0da_feature, feature)(*value)
    except AttributeError:
        payload = None

    if payload is None:
        print(f"Cannot create payload for {feature}")
    else:
        print(device.send_feature(payload))
