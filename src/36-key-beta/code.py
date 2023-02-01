print("Starting")

import board
from kb import KMKKeyboard
from kmk.keys import KC
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

keyboard = KMKKeyboard()
keyboard.modules.append(combos)
keyboard.modules.append(TapDance())
keyboard.modules.append(Layers())
keyboard.modules.append(OneShot())
keyboard.modules.append(ModTap())
keyboard.modules.append(MouseKeys())
keyboard.extensions.append(MediaKeys())



# --------------- Macros ------------- 

redo = simple_key_sequence((KC.LSFT(KC.LGUI(KC.Z),),))
undo = simple_key_sequence((KC.LSFT(KC.LGUI(KC.Z),),))
SPC_sft = KC.MT(KC.LSFT, KC.SPC, timeout=80)
ESC_gui_sft = KC.MT(KC.LGUI(KC.LSFT), KC.ESC, timeout=80)
FIND_gui = KC.MT(KC.LGUI(KC.LSFT), KC.ESC, timeout=80)




# --------------- Combos --------------   

combos.combos = (

    # # #
    # # #---------- KEYS ----------

    # -- Left Hand --
    Chord((KC.R, KC.S), KC.BSPC, timeout=40),
    Chord((KC.T, KC.R), KC.LALT(KC.BSPC), timeout=10),
    Chord((KC.D, KC.C), KC.OS(KC.MO(1))),
    Chord((KC.T, KC.D), KC.LPRN),

    Chord((KC.S, KC.C), KC.EXLM),


    # -- Right Hand --
    Chord((KC.E, KC.I), KC.ENT),
    Chord((KC.N, KC.H), KC.RPRN),





    # # #
    # # # ---------- LEADER KEYS ---------- 

    # select to entire line
    Sequence((KC.LEADER, KC.I), simple_key_sequence((KC.LGUI(KC.LEFT),KC.LSFT(KC.LGUI(KC.RIGHT),),)), timeout=600),

    # WINDOW LEFT 
    Sequence((KC.LEADER, KC.S), KC.LCTL(KC.LSFT(KC.LEFT),), timeout=600),
    # WINDOW RIGHT
    Sequence((KC.LEADER, KC.E), KC.LCTL(KC.LSFT(KC.RIGHT),), timeout=600),

    # CAPS LOCK
    Sequence((KC.LEADER, KC.C), KC.CAPS, timeout=600),
)



keyboard.keymap = (

    #
    # [1] ALPHA2 
    [
                        KC.Q,  KC.W,  KC.F,  KC.P,  KC.B,                KC.J,  KC.L,  KC.U,  KC.Y,  KC.BSPC,\
                        KC.A,  KC.R,  KC.S,  KC.T,  KC.Q,                KC.M,  KC.N,  KC.E,  KC.I,  KC.O,\
                        KC.Z,  KC.X,  KC.C,  KC.D,  KC.V,                KC.K,  KC.H,  KC.COMMA, KC.DOT, KC.SLASH,\
        KC.NO, KC.NO, KC.NO, KC.NO,      SPC_sft,  ESC_gui_sft,        FIND_gui,  KC.MO(1),       KC.NO,  KC.NO,  KC.NO,  KC.NO   
        KC.NO,  KC.NO,      KC.LALT,  undo,  KC.LGUI,  redo,           KC.MO(2),  KC.LEADER,  KC.TAB,  KC.RCTL,       KC.NO, KC.NO\
    #                       forward,   up,     back,    down             down,      back,      up,     forward

    ],
    # 
    # [2] NUM
    [
            KC.NO, KC.NO,     KC.UP,     KC.NO,     KC.NO,           KC.NO, KC.N7,  KC.N8,   KC.N9,   KC.N0, \
            KC.NO, KC.RIGHT,  KC.DOWN,   KC.LEFT,   KC.NO,           KC.NO, KC.N4,  KC.N5,   KC.N6,   KC.N7, \
            KC.NO, KC.NO,     KC.NO,     KC.NO,     KC.NO,           KC.NO, KC.N1,  KC.N2,   KC.N3,   KC.NO, \
           KC.TRNS,   KC.TRNS,   KC.TRNS, KC.TRNS, KC.TRNS,         KC.TRNS, KC.TRNS,   KC.TRNS,   KC.TRNS,    KC.TRNS,\
           KC.TRNS,   KC.TRNS,   KC.TRNS, KC.TRNS, KC.TRNS,         KC.TRNS, KC.TRNS,   KC.TRNS,   KC.TRNS,    KC.TRNS,\
    ],
    # 
    # [2] MACRO LAYER - define your own actions
    [
                     KC.NO,  KC.NO,   KC.NO,   KC.NO, KC.NO,           KC.NO, KC.NO,  KC.NO,   KC.NO,   KC.NO,  \
                     KC.NO,  KC.NO,   KC.NO,   KC.NO, KC.NO,           KC.NO, KC.NO,  KC.NO,   KC.NO,   KC.NO,  \
                     KC.NO,  KC.NO,   KC.NO,   KC.NO, KC.NO,           KC.NO, KC.NO,  KC.NO,   KC.NO,   KC.NO,  \
             KC.TRNS,   KC.TRNS,   KC.TRNS, KC.TRNS, KC.TRNS,         KC.TRNS, KC.TRNS,   KC.TRNS,   KC.TRNS,    KC.TRNS,\
             KC.TRNS,   KC.TRNS,   KC.TRNS, KC.TRNS, KC.TRNS,         KC.TRNS, KC.TRNS,   KC.TRNS,   KC.TRNS,    KC.TRNS,\
    ],

)


if __name__ == '__main__':
    keyboard.go(hid_type=HIDModes.BLE, ble_name='fulcrum')
