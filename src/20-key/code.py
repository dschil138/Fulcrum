print("Starting")

import board
from kb import KMKKeyboard
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers
from kmk.handlers.sequences import simple_key_sequence, send_string
from kmk.modules.combos import Combos, Chord, Sequence
from kmk.modules.tapdance import TapDance
from kmk.modules.oneshot import OneShot
from kmk.modules.modtap import ModTap
from kmk.hid import HIDModes
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.mouse_keys import MouseKeys


# --------------- Module Settings -------------- 

combos = Combos()
encoder_handler = EncoderHandler()
encoder_handler_2 = EncoderHandler()

keyboard = KMKKeyboard()
keyboard.modules.append(combos)
keyboard.modules.append(TapDance())
keyboard.modules.append(Layers())
keyboard.modules.append(OneShot())
keyboard.modules.append(ModTap())
keyboard.modules.append(MouseKeys())
keyboard.extensions.append(MediaKeys())
keyboard.modules.append(encoder_handler)
keyboard.modules.append(encoder_handler_2)

encoder_handler.pins = ((board.SCK, board.A4, board.A5, False,),)
encoder_handler_2.pins = ((board.D2, board.MISO, board.MOSI, False,),)


# --------------- Macros ------------- 

redoMacro = simple_key_sequence((KC.LSFT(KC.LGUI(KC.Z),),))
t_h_e = send_string('the')
a_n_d = send_string('and')
a_k_e = send_string('ake')


# --------------- Combos --------------   

combos.combos = (

    # # #
    # # #---------- KEYS ----------

    # -- Left Hand --
    Chord((KC.R, KC.S), KC.BSPC, timeout=40),
    Chord((KC.T, KC.R), KC.LALT(KC.BSPC), timeout=10),
    Chord((KC.D, KC.C), KC.OS(KC.MO(1))),
    Chord((KC.S, KC.V), KC.LGUI(KC.SLASH)), 
    Chord((KC.T, KC.D), KC.LPRN),

    Chord((KC.N, KC.V), KC.TAB),
    Chord((KC.X, KC.C), KC.EQL),
    Chord((KC.S, KC.C), KC.EXLM),
    Chord((KC.R, KC.V), KC.LGUI(KC.F)),


    # -- Right Hand --
    Chord((KC.E, KC.I), KC.ENT),
    Chord((KC.H, KC.U), KC.DOT),
    Chord((KC.A, KC.K), KC.RPRN),
    Chord((KC.K, KC.H), KC.MINUS),
    Chord((KC.E, KC.H), KC.SLASH),
    
    Chord((KC.N1, KC.N3), KC.N2),
    Chord((KC.N3, KC.N4), KC.N5),
    Chord((KC.N6, KC.N8), KC.N7),
    Chord((KC.LEFT, KC.DOWN), KC.LGUI(KC.LEFT)),




    # # #
    # # #---------- WORDS ----------

    # -- Left Hand --
    Chord((KC.R, KC.N), send_string('rn'), timeout=50),
    Chord((KC.R, KC.C), send_string('qu')),


    # -- Right Hand --
    Chord((KC.I, KC.O), send_string('you')),
    Chord((KC.E, KC.U), send_string('of')),
    Chord((KC.A, KC.I), send_string('ay')),
    Chord((KC.A, KC.E), send_string('The')),

    Chord((KC.I, KC.H), send_string('ould')),
    Chord((KC.I, KC.K), send_string('ough')),
    Chord((KC.A, KC.U), send_string('from')),
    Chord((KC.K, KC.U), send_string('just')),


    # -- Both Hands --
    Chord((KC.R, KC.I, KC.O), send_string("you're "), timeout=80),
    Chord((KC.T, KC.I, KC.O), send_string('You'), timeout=80),
    Chord((KC.R, KC.C, KC.I), send_string('qu')),




    # # #
    # # # ---------- LEADER KEYS ---------- 

    # select to entire line
    Sequence((KC.LEADER, KC.I), simple_key_sequence((KC.LGUI(KC.LEFT),KC.LSFT(KC.LGUI(KC.RIGHT),),)), timeout=600),
    # Open iTerm
    Sequence((KC.LEADER, KC.T), simple_key_sequence((KC.LALT, KC.LALT)), timeout=600),

    # WINDOW LEFT 
    Sequence((KC.LEADER, KC.S), KC.LCTL(KC.LSFT(KC.LEFT),), timeout=600),
    # WINDOW RIGHT
    Sequence((KC.LEADER, KC.E), KC.LCTL(KC.LSFT(KC.RIGHT),), timeout=600),

    # CAPS LOCK
    Sequence((KC.LEADER, KC.C), KC.CAPS, timeout=600),
)



keyboard.keymap = (
    #
    # [0] ALPHA1
    #
    # (This first layer is difficult to read. Due to memory limitations, I've used as few variable
    # definitons as possible, instead defining the functionality of keys directly in the keymap here)
    [
                                                        KC.N,   KC.R,   KC.S,  KC.T,         KC.A,   KC.E,   KC.I,   KC.O,\
                                                        KC.NO,  KC.X,  KC.C,   KC.D,         KC.H,   KC.U,   KC.K,   KC.NO,\
        KC.V,      KC.NO,  KC.MT(KC.SPC, KC.LSFT, tap_time=80),   KC.MT(KC.ESC, KC.LSFT(KC.LGUI), tap_time=80),         KC.MT(KC.LGUI(KC.F), KC.RGUI, tap_time=80), KC.OS(KC.MO(1)), KC.NO,     KC.QUOTE,  \
            KC.MT(KC.OS(KC.MO(1)), KC.LALT),   KC.LT(4, KC.LGUI(KC.Z), tap_time=180),   KC.MO(3),   KC.LGUI,         KC.LEADER,   KC.MO(2),   KC.LT(4, KC.TAB, tap_time=180),   KC.RCTL,\
        # --- DEFAULT LAYER GUIDE FOR LAYOUT ---
        #
        #       N,   R,    S,     T,       -       A,      E,      I,      O,  
        #   V,       X,    C,     D,       -       K,      H,      U,         QUOTE, # <-- due to wiring, this is the top right middle finger key. V is the top left
        #     SPC/Shift,   ESC/CMD+SHIFT,  -     CMD+F/CMD,    ALPHA2, 
        #                                  -
        #                undo              -             Tab
        #            CMD      ALT          -        CTL      LEADER    
        #                NAV               -             NUM
    ],
    #
    # [1] ALPHA2 
    [
                    KC.J,    KC.F,    KC.L,    KC.P,          a_n_d,     t_h_e,     KC.Y,      KC.Q,\
                    KC.NO,   KC.B,    KC.M,    KC.G,          KC.SCLN,    KC.COMMA,    a_k_e,      KC.NO,\
        KC.W,         KC.TRNS,   KC.TRNS,  KC.TRNS,        KC.TRNS,   KC.TO(0),   KC.TRNS,            KC.Z, # <--this is the top right middle finger key. W is the top left
        KC.TRNS,   redoMacro,   redoMacro,   KC.TRNS,         KC.TRNS,   KC.TRNS,   KC.TRNS,  KC.TRNS,\
    ],
    # 
    # [2] NUM
    [
                        KC.NO,   KC.N6,     KC.N8,      KC.N0,         KC.N1,   KC.N3,   KC.N4,   KC.N5,\
                        KC.NO,   KC.LBRC,   KC.MINUS,   KC.N9,         KC.N2,   KC.EQL,  KC.RBRC, KC.NO,\
            KC.LBRC,             KC.NO,     KC.TRNS,    KC.TRNS,       KC.RGUI, KC.TRNS, KC.NO,               KC.RBRC,  \
        KC.TRNS,   redoMacro,   redoMacro,   KC.LSFT(KC.LGUI),         KC.TRNS,   KC.TRNS,   KC.TRNS,   KC.TRNS,\
    ],
    #
    # [3] NAV
    [
            KC.LSFT,   KC.LALT,   KC.LGUI,    KC.LCTL,             KC.LEFT,    KC.DOWN,   KC.RIGHT,   KC.RGUI(KC.RIGHT),\
            KC.NO,     KC.NO,     KC.MB_RMB,  KC.GRAVE,            KC.MB_LMB,  KC.MB_RMB, KC.NO,      KC.NO,\
        KC.UP,         KC.NO,     KC.TRNS,    KC.TRNS,             KC.RGUI,    KC.TRNS,   KC.NO,                KC.UP,  \
            KC.TRNS,   KC.TRNS,   KC.TRNS,    KC.TRNS,             KC.MS_DN,   KC.MS_LT,  KC.MS_RT,   KC.MS_UP,\
    ],
    #
    # [4] FUNCTION LAYER
    # (Define extra functionality here)
    [
                        KC.NO,   KC.NO,   KC.NO,   KC.NO,           KC.NO, KC.NO, KC.NO,  KC.NO,\
                        KC.NO,   KC.NO,   KC.NO,   KC.NO,           KC.NO, KC.NO, KC.NO,  KC.NO,\
            KC.NO,               KC.NO,   KC.NO,   KC.NO,           KC.NO, KC.NO, KC.NO,            KC.NO,\
                KC.RALT, redoMacro, KC.NO,  KC.LSFT(KC.LGUI),       KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,\
    ],
)

#  Right Knob:             1 - volume,                      2 - TRNS,                       3- TRNS,                          4 - Mouse Scroll
encoder_handler.map = [((KC.VOLD, KC.VOLU, KC.MPLY,),), ((KC.TRNS, KC.TRNS, KC.TRNS,),), ((KC.TRNS, KC.TRNS, KC.TRNS,),),  ((KC.MW_UP, KC.MW_DN, KC.NO,),),]
encoder_handler_2.map = [((KC.LGUI(KC.Z), redoMacro, KC.NO,),), ((KC.TRNS, KC.TRNS, KC.TRNS,),), ((KC.LSFT(KC.LGUI(KC.LEFT)), KC.LSFT(KC.LGUI(KC.RIGHT)), KC.MPLY,),), ((KC.MW_DN, KC.MW_UP, KC.NO,),),]
#  Left Knob:              1 - Undo/Redo,                          2 - TRNS,                         3- Tab Left/Right,                                                     4 - Mouse Scroll


if __name__ == '__main__':
    keyboard.go(hid_type=HIDModes.BLE, ble_name='fulcrum')
