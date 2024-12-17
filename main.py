results: List[str] = []
datas = ""
serial.redirect(SerialPin.USB_TX, SerialPin.USB_RX, BaudRate.BAUD_RATE9600)
basic.show_icon(IconNames.STICK_FIGURE)

def on_forever():
    global datas, results
    datas = serial.read_string()
    if datas:
        results = datas.split(",")
        basic.show_string("" + str((results)))
        basic.show_string(datas)
basic.forever(on_forever)
