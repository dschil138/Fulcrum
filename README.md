# Fulcrum Keyboard
The Fulcrum Keyboard is an ergo-mechanical split keyboard with extra thumb functionality. It has 20 keys, two rotary encoders, and two 5-way switches.
![Photo of the Fulcrum Keyboard](Fulcrum_Keyboard.jpg "")

The original inspiration for such a small number of keys came from Ben Vallack’s "Piano" board. I have made some pretty significant changes from his design, but the core idea of putting several of the alpha keys on a second layer is what drives this board’s design.

The four regular thumb keys are low profile choc switches, and the rest are MX. This is done to accommodate for the fact that your thumb sits on lower plane than the rest of your fingers while typing. In the future I may explore ways to make this height difference even greater.

The rotary encoders are positioned and angled to make them as easy to reach and use as possible. They are right where your hands expect them.

The same is true with the 5-way switch joysticks on the thumbs. They are effortless to use. These joysticks are really the defining feature of this keyboard. They open up such a huge field of utility that once you use it, it's hard to imagine ever going back to a keyboard that doesn't have them again.

## BOM
1. nRF52840
2. 16 MX style key switches
3. 4 choc style key switches
4. 2 EC11 Rotary Encoders
5. 2 5-way switches
6. on/off switch
7. USB-C breakout board
8. LiPo battery (at least 1,000 mAh)
9. wire (recommended)


# Keyboard Features
## COMBOS

This keyboard uses a layout with a *significant* number of combos. You don't necessarily have to use as many as I do, but you are going to have to use some no matter what.

So many, in fact, that the KMK firmware files must be altered pretty significantly to free up enough memory on the microcontroller to handle all the timeout timers. There are also only two microcontrollers currently available to my knowledge which can run this firmware without crashing - The Adafruit nRF52340 [Itsy Bitsy](https://www.adafruit.com/product/4481) version or the [Feather](https://www.adafruit.com/product/4062) version.

The combos are split into two main categories: Keys and Words. For the most part, you probably need to keep the Key combos while the Word combos are more optional.


## Rotary Encoders
I find rotary encoders to be very useful, so this keyboard includes two of them. similarly to the key risers, the encoders use an extra "cap" to angle the encoders into a more ergonomic position and to give a little extra clearance so that the rest of the case can remain more low profile.


## 5-Way Switches
This is the most essential part of the Fulcrum design. A small joystick on a 5-way switch is mounted sideways so that the top joystick rests against the pad of your thumb as it rests on the "home" thumb key. This provides a range of ergonomic movements for each thumb. 

You should experiment with different functions to find what feels comfortable for you, but here are some useful tips:
1. Pressing "down" (towards the desk) on the joystick should be a layer switch while held. This is because it is the easiest motion to hold while also pressing other keys on the keyboard.
2. I find that pushing "up" on the left joystick is a very intuitive place for "Undo"
3. The most awkward movement is pushing them "forward" (away from you), so choose what you put there carefully
4. They handle "Mod-Tap" functionality very well, so consider a "hold" key and a "tap" key for each direction

The switches are mounted using two pieces. They clamp around the base of the switch and then are superglued to the top of the plate.

There is no precise place to mount this little platform, it is meant to have flexibility there so that you can mount it where it feels comfortable. You may want to consider lengthening or shortening the joystick as well.


## Word Keys
We type the words "the" and "and" a lot. Even more-so when you count them when they are just part of another word (Like *the*m, *the*y, or ano*the*r). So this keyboard just gives *the*m *the*ir own keys. You will be surprised how much time this saves! Feel great and efficient to type with them. 


## Optional key risers
Most keys have optional risers to help them conform to the shape of your hand. They are used according to this diagram. To use them, print the top plate of the case as normal, and just superglue the risers on top. The switches should friction fit into the risers.


## Wiring
While this is a split keyboard, I have chosen to hardwire the halves together. You can follow my wiring if you'd like, or if you want to use a TRRS cable to connect the halves, KMK does offer I2C connection it's official firmware (I have removed it here - see Combos section)

