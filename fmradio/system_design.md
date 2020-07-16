# FM Radio Receiver - System Design

Main intention of this project is to learn, not expensive, not too complicated.

Main components we need to choose inorder to build a FM Radio Receiver are: 
1. FM Receiver/Tuner
2. Potentiometer (for changing frequency)
3. Buttons (cases like, reset)
4. Display for showing channel information
5. Audio device, for hearing the sound like speaker or headphone 
6. Microcontroller

![design](https://user-images.githubusercontent.com/10448770/87686760-bf9ca980-c739-11ea-8605-a519c6e76577.png)

## Design options
### 1. FM Tuner Si4703
**Options:**
  1. basic board: cheap $10, No headphone jack. require antenna
  2. evaluation board: not cheap $20, level: easy, headphone jack present, no antenna required.
  3. Complete module off the shelf with LCD display: easy; and nothing to learn.

**Evaluation:**
will choose the evaluation board in 2nd option: 
- time: faster progress with inbuilt headphone jack(headphone can serve as an antenna). Easy to setup.
- availability: not many FM receiver are in market. 
- communicate I2C, so works with both Arduino and Raspberry Pi

**Chosen:** Evaluation board.

**References:** 
- https://learn.sparkfun.com/tutorials/si4703-fm-radio-receiver-hookup-guide/all

### 2. Display
**Options:**
	1. LCD: serial communication is used or use 8pins on the Arduino. 
	2. OLED: Uses SPI/I2C communication, hence we choose OLED. 

**Evaluation:**
- price is approximately same.
- learning also is not difficult, as some pin connection and guides are avaiable for both. 
- OLED require less pins
- Serial communication not possible(or complicated), since we already decided to make bluetooth as serial interface. 
- OLED can be used as I2C/SPI and not limited to use serial or 8 pins.

**Chosen:** OLED

**References:**
- https://learn.sparkfun.com/tutorials/micro-oled-breakout-hookup-guide
- https://learn.sparkfun.com/tutorials/basic-character-lcd-hookup-guide


### 3. Audio: 
**Options:**
	1. headphone jack only: cheaper, time saving option
	2. speaker with amplifier: Needs amplifier, and more sound. Also if its using the speaker, external antenna required for FM reciever.

**Evaluation:**
Initialy headphone can save time, and money, as it can act as an antenna and no amplifier required. hence we will choose headphone jack. 

**Chosen:** Headphone

### 4. Microcontroller: 
**Options:**
  1. Arduino Uno R3: Dedicated for Radio, so faster.
  2. Raspberry Pi Zero WH: With operating system, and can run a python program which can process the GPIO pins. 

**Evaluation:** 
Radio with an Operating system is not necessary, time to boot the system, and then run as program etc. But instead a dedicated microcontroller, which can function only as FM Radio, hence we choose Arduino. 

**Chosen:** Arduino Uno R3
