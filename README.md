# Fulcrum Keyboard

The Fulcrum is a wireless ergo-mechanical split keyboard. It has 20 keys, two rotary encoders, and two 5-way switch joysticks. It runs KMK circuitpython firmware on an nRF52840 microcontroller.

![Photo of the Fulcrum Keyboard](photos/fulcrum-1-web.jpg)

## Description



This keyboard uses Ben Vallack's innovative approach to sub-20-key keyboards and extends it using 5-way switch joysticks and other features to improve the overall utility and comfort of the board.

The four regular thumb keys are low profile choc switches, and the rest are MX. This is done to accommodate for the fact that your thumb sits on lower plane than the rest of your fingers while typing, helping to reduce hand strain.

The rotary encoders are positioned and angled to make them as easy to reach and use as possible. They are right where your hands expect them to be.

The same is true with the 5-way switch joysticks on the thumbs. They are effortless to use. These joysticks are really the defining feature of this keyboard. They open up such a huge field of utility that once you use, it's hard to imagine going back to a keyboard that doesn't have them.

## Bill Of Materials

| Part      | Quantity | Notes| 
| :-------------- | :---: | :------ |
| nRF52840 Microcontroller | 1 | Recommended: Adafruit nRF52340 [Itsy Bitsy](https://www.adafruit.com/product/4481) or [Feather](https://www.adafruit.com/product/4062) version.|
| Choc key switch | 4 | For thumb keys|
| MX style key switches    | 16 | For non-thumb keys |
| 1N4148 Diodes  | 22 | Only one is needed for each 5-way switch | 
| Rotary Encoders | 2 | Recommended: EC11, but you do you|
| 5-Way Switches   | 2 | Try to buy the ones with the lowest operating force that you can find |
| On/Off switch    | 1 | |
| USB-C Breakout Board   | 1 | (optional)|
| Lipo battery    | 1 | At least 1000 mAh, this things chews batteries |
| Wire      |  | Recommend 30AWG or 28AWG|

## Firmware

This keyboard runs on KMK firmware, which you can get [here](https://github.com/KMKfw/kmk_firmware). My code.py and kb.py files are in this repo, which are the only files that need to be updated from the stock firmware to run this board.

---

# Keyboard Features

## 5-Way Switches

**This is the most essential and defining feature of the Fulcrum design. Each side has a small 5-way switch joystick, which is mounted horizontally so that the top of the joystick sits against the pad of your thumb when on the "home" thumb position. This provides a wide range of ergonomic movements to utilize on each thumb.**

Our thumbs are criminally underutilized on regular keyboards. Your two most capable fingers, both regulated to just one key - the space bar.

Many ergonomic keyboards try to rectify this problem by giving each thumb several keys, arranging them in either a cluster or an arc shape. This is an improvement, but most people quickly find that it is actually quite difficult for your thumb to stretch over multiple keys and hit something accurately, let alone comfortably. More inefficency!

So what's going on with our phones? Look at how well we use our thumbs to type on them. On a smartphone, our thumbs are fast, accurate, and dexterous. Incredibly efficient. What's the disconnect? Why are they so nimble over there, and so lumbering and inaccurate on our keyboards?

The disconnect is that our thumbs are *opposable*, but for some reason our keyboards insist on giving them the same type of key as our other fingers. Our thumbs want to move in a different direction!

The 5-way switch joysticks on the Fulcrum are mounted sideways, allowing you to use your thumbs in a dimension more similar to how you type on a smartphone. This is highly comfortable and very efficient. You already know how to do it quite well!

With the regular key switch placed directly below joystick, this actually puts six different actions at the tip of each thumb with very minimal movement.

Most importantly, all of these actions are easily paired with other key presses elsewhere on the keyboard. It's a whole new world of utility.

![Photo of the Fulcrum Keyboard](photos/fulcrum-detail-1-web.jpg)

The switches are mounted using an angled platform. It consists of two pieces which clamp around the base of the switch. The whole assembly is then superglued to the top of the case.

There is no precise place to glue this little platform. There is meant to be flexibility there so that you can mount it where it feels comfortable to you. You may want to consider lengthening or shortening the joystick as well, with a longer joystick providing extra leverage on the switch.

> **Note**
> Useful tips to help you choose what functions to assign to the joysticks:
> 1. Pressing "down" (towards the desk) on the joystick should be a layer switch when held. This is because it is the easiest motion to hold & press other keys.
> 2. The most awkward movement is pushing them "forward" (away from you), so choose what you put there carefully
> 3. Mod-Tap works well on them, so consider a "hold" & "tap" key for each
> 4.  The first few times you use them, you may find it hard to not move the whole board around a bit when pressing certain directions. This will go away after a day or two of getting used to the movements.


## Combos
This keyboard uses a layout with a *significant* number of combos. You don't necessarily have to use as many as I do, but you are going to have to use some no matter what.

The combos are split into two main categories: Keys/Actions and Words. For the most part, you probably need to keep the Key combos while the Word combos are more optional.

Here is a layout of most of the Key/Action Combos:

![Key Combos Diagram](photos/key-action-combos.png)

> **Note**
> If you want to add more combos, you will have to delete some that are already there, as the firmware is basically operating at it's limit right now.

## Word Keys
In addition to having combos for certain words, there are also a couple words that get their own dedicated keys in this layout. 

We type the words "the" and "and" a lot. Even more-so when you count them when they appear as part of other words (**the**m, **the**y, or ano**the**r). So this keyboard just gives them their own keys. You will be surprised how much time this saves! Feel great and efficient to type with them. 


## Optional key risers
Most keys have optional risers to help them conform to the shape of your hand. Every non-thumb key gets them except the bottom two on the middle finger. The top middle finger key gets a slanted riser.  

![Photo of the Fulcrum Keyboard Detail](photos/fulcrum-detail-2-web.jpg)

To use them, print the top plate of the case as normal, and just superglue the risers on top. The switches should friction fit into the risers.


## Rotary Encoders
I find rotary encoders to be very useful, so this keyboard includes two of them. Similarly to the key risers, the encoders use an extra "cap" to angle and raise the encoders so that they sit in a more ergonomic position and give a little extra clearance underneath in the low-profile case.

## Wiring
While this is a split keyboard, I have chosen to hard-wire the halves together. You can follow my wiring if you'd like, or if you want to use a TRRS cable to connect the halves, KMK does offer I2C connection functionality. There is a wiring diagram in the photos folder.

## Hotswap Sockets
There is no PCB for this keyboard, it is a hand-wired build. But we all still want to be able to swap out different switches, so I've made printable hot-swap socket holders that allow you to still do so. You can find both the MX & Choc versions [here](https://www.printables.com/model/284057-hot-swap-socket-holders). 

---

# Layer Keymaps
(blank spaces on joystick directions inherit the key from the previous layer)

![All Fulcrum Layers](photos/fulcrum-layouts-full-2.jpg)
