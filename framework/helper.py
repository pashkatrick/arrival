expected_error_pins = [
    {'Name': 'Gear_1', 'PinId': 1, 'Voltage': 0.01},
    {'Name': 'Gear_2', 'PinId': 2, 'Voltage': 0.01},
    {'Name': 'AccPedal', 'PinId': 3, 'Voltage': 0.01},
    {'Name': 'BrakePedal', 'PinId': 4, 'Voltage': 0.01},
    {'Name': 'BatteryVoltage', 'PinId': 5, 'Voltage': -1.0}
]

expected_error_signals = [
    {'Name': 'GearPosition', 'SigId': 1, 'Value': 'Neutral'},
    {'Name': 'AccPedalPos', 'SigId': 2, 'Value': 'Error'},
    {'Name': 'BrakePedalState', 'SigId': 3, 'Value': 'Error'},
    {'Name': 'ReqTorque', 'SigId': 4, 'Value': '0 Nm'},
    {'Name': 'BatteryState', 'SigId': 5, 'Value': 'Error'}
]
