let results: string[] = []
let datas = ""
serial.redirect(
SerialPin.USB_TX,
SerialPin.USB_RX,
BaudRate.BaudRate9600
)
basic.showIcon(IconNames.StickFigure)
basic.forever(function () {
    datas = serial.readString()
    results = datas.split("|")
    basic.showString("" + (results))
    if (datas) {
        basic.showString("" + (results))
        basic.showString(datas)
    }
})
