import board
from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation

class KMKKeyboard(_KMKKeyboard):
    col_pins = (board.RX, board.TX, board.D7, board.D10, board.A3, board.A2, board.A1, board.A0)
    row_pins = (board.SCK, board.A5, board.A4, board.SDA)
    diode_orientation = DiodeOrientation.COL2ROW

