# Fulcrum Keyboard

The Fulcrum is a wireless ergo-mechanical split keyboard. It has 20 keys, two rotary encoders, and two 5-way switch joysticks. It runs KMK circuitpython firmware on an nRF52840 microcontroller.

![Photo of the Fulcrum Keyboard](photos/fulcrum-1-web.jpg)

## Description



This keyboard uses Ben Vallack's innovative approach to sub-20-key keyboards and extends it using 5-way switch joysticks and other features to improve the overall utility and comfort of the board.

These joysticks are really the defining feature of this keyboard. They are positioned to give you several actions on each thumb by utilizing your thumb's natural range of motion. They are comfortable and almost effortless to use.



# Keyboard Features

## 5-Way Switch Thumb Joysticks

Our thumbs are criminally underutilized on regular keyboards. Your two most capable fingers, both regulated to just one key - the space bar.

Many ergonomic keyboards try to rectify this problem by giving each thumb several keys, arranging them in either a cluster or an arc shape. This is an improvement, but most people quickly find that it is actually quite difficult for your thumb to stretch over multiple keys and hit something accurately, let alone comfortably. More inefficency!

> So what's going on with our phones? Look at how well we use our thumbs to type on them. On a smartphone, our thumbs are fast, accurate, and dexterous. Incredibly efficient. What's the disconnect? Why are they so nimble over there, and so lumbering and inaccurate on our keyboards?

> The disconnect is that our thumbs are *opposable*, but for some reason our keyboards keep insisting on giving them the same type of key as our other fingers. Our thumbs want to move in a different direction!

> The 5-way switch joysticks on the Fulcrum are mounted sideways, allowing you to use your thumbs in a dimension more similar to how you type on a smartphone. This is highly comfortable and very efficient. It immediately feels natural.

With the regular key switch placed directly below joystick, this actually puts six different actions at the tip of each thumb with very minimal movement.

Most importantly, all of these actions are easily paired with other key presses elsewhere on the keyboard.

![Photo of the Fulcrum Keyboard](photos/fulcrum-detail-1-web.jpg)

The switches are mounted using an angled platform. It consists of two pieces which clamp around the base of the switch. The whole assembly is then superglued to the top of the case.

There is no precise place to glue this little platform. There is meant to be flexibility there so that you can mount it where it feels comfortable to you. You may want to consider lengthening or shortening the joystick as well, with a longer joystick providing extra leverage on the switch.

> **Note**
> Useful tips to help you choose what functions to assign to the joysticks:
> 1. Pressing "down" (towards the desk) on the joystick should be a layer switch when held. This is because it is the easiest motion to hold & press other keys.
> 2. Mod-Tap works well on them, so consider a "hold" & "tap" key for each
> 3.  The first few times you use them, you may find it hard to not move the whole board around a bit when pressing certain directions. This will go away after a day or two of getting used to the movements.


## Combos
This keyboard uses a layout with a *significant* number of combos. You don't necessarily have to use as many as I do, but there are some that you are going to want to keep.

Here is a guide to most of the important combos. They are generally split into combos that output words, and combos that output certain keys or actions (like "delete").
![Important Combos Diagram](photos/important-combos-2.webp)

> **Note**
> If you want to add more combos, you will need to delete some that are already defined, as the firmware is basically operating at its limit right now.

## Word Keys

We type the words "**the**" and "**and**" a lot. Even more-so when you count them when they appear as a part of another word (**the**m, **the**y, ano**the**r).

So this keyboard just gives them their own keys!

It's funny, we never question giving Z or Q their own key, but the trigram "the" is more common than either of those letters (2-3 times as common!). So using a single key to type "the" just makes sense.

The full keymap can be found at the [bottom of this page](#layer-keymaps).


## Optional Key Risers
Most keys have optional risers to help them conform to the shape of your hand. Every key gets them except the thumb keys and the bottom two middle finger keys. The top middle finger key gets a slanted riser.  

![Photo of the Fulcrum Keyboard Detail](photos/fulcrum-detail-2-web.jpg)

To use them, print the top plate of the case as normal, and superglue the risers on top. The switches should friction fit into the risers.

>**Note** 
>The four thumb keys are low profile choc switches, as opposed to the rest which are MX. This is to accommodate the fact that your thumb sits on lower plane than the rest of your fingers, helping to further reduce hand strain.
>
>The custom angled keycaps for the thumb keys can be found in the STLs folder.


## Rotary Encoders
 Similarly to the key risers, the encoders use a slanted riser to angle and raise the encoders so that they sit in a more ergonomic position and give a little extra clearance underneath in the low-profile case.
 
 This is printed separately and then glued to the top of the case, giving you some wiggle room to position the knobs exactly where you want them.



# Build Guide

## BOM

| Part      | Quantity | Notes| 
| :-------------- | :---: | :------ |
| nRF52840 Microcontroller | 1 | Recommended: Adafruit nRF52340 [Itsy Bitsy](https://www.adafruit.com/product/4481) or [Feather](https://www.adafruit.com/product/4062) version.|
| Choc key switches | 4 | For thumb keys|
| MX key switches    | 16 | For non-thumb keys |
| 1N4148 Diodes  | 22 | Only one is needed for each 5-way switch | 
| Rotary Encoders | 2 | Recommended: EC11, but you do you|
| 5-Way Switches   | 2 | Try to buy the ones with the lowest operating force that you can find |
| On/Off switch    | 1 | |
| USB-C Breakout Board   | 1 | (optional)|
| Lipo battery    | 1 | At least 1000 mAh, this thing chews batteries |
| Wire      |  | Recommend 30AWG or 28AWG|

## Wiring
While this is a split keyboard, I have chosen to hard-wire the halves together. You can follow my wiring if you'd like, or if you want to use a TRRS cable to connect the halves, KMK does offer I2C connection functionality.
![Wiring Diagram](photos/wiring.webp)

## Hotswap Sockets
There is no PCB for this keyboard, it is a hand-wired build. But we all still want to be able to swap out different switches, so I've made printable hot-swap socket holders that allow you to do that. You can find both the MX & Choc versions [here](https://www.printables.com/model/284057-hot-swap-socket-holders)

---

# Layer Keymaps
(blank spaces on joystick directions inherit the key from the previous layer)

![All Fulcrum Layers](photos/fulcrum-layouts-full-2.jpg)
