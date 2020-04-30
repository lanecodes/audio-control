#! /opt/miniconda3/bin/python
"""
toggle_audio.py
~~~~~~~~~~~~~~~

Mute/ unmute master audio on PC.

Depends on `amixer`.
"""
from enum import Enum
import re
from subprocess import check_call, check_output


DEVICES = ['Master', 'Speaker', 'Headphone']


class Status(Enum):
    OFF = 0
    ON = 1


def toggle_all():
    """Synchronise all devices with Master and turn on/ off."""
    master_status = toggle_device('Master')
    other_devices = [x for x in DEVICES if x != 'Master']
    for d in other_devices:
        if device_status(d) != master_status:
            toggle_device(d)


def toggle_device(device: str) -> Status:
    """Toggle device status, return new status."""
    res = check_output(['amixer', 'set', _validate_device(device), 'toggle'])
    return _parse_status(res.decode())


def device_status(device: str) -> Status:
    """Get status of given device from `amixer`."""
    res = check_output(['amixer', 'get', _validate_device(device)])
    return _parse_status(res.decode())


def _parse_status(response: str) -> Status:
    """Convert amixer device response string to Status."""
    status_str = re.match(r'.*\[(.*)\]\n$', response, re.DOTALL).group(1)
    if status_str == 'on':
        return Status.ON
    elif status_str == 'off':
        return Status.OFF
    else:
        raise ValueError('Could not parse amixer response status')


def _validate_device(device: str) -> str:
    if device not in DEVICES:
        raise ValueError(f"'{device}' is not a known device")
    return device


if __name__ == '__main__':
    toggle_all()
