radio.onReceivedString(function (receivedString) {
    radio_in = receivedString
    if (receivedString == "t") {
        radio.sendNumber(input.temperature())
    }
})
let radio_in = ""
radio.setGroup(88)
basic.forever(function () {
    basic.showString(radio_in)
})
