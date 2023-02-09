import board
from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation

class KMKKeyboard(_KMKKeyboard):
    col_pins = (board.D13, board.D12, board.D10, board.D9, board.D7, board.SCL, board.SDA, board.TX, board.RX, board.D2)
    row_pins = (board.MOSI, board.SCK, board.A5, board.A4, board.A3)
    diode_orientation = DiodeOrientation.COL2ROW

