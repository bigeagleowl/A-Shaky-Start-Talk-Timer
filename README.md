# A-Shaky-Start-Talk-Timer

This is a BBC micro:bit count down talk timer to tell you how much time you have left to complete your talk. You start the timer by shaking the micro:bit. It gives you a visual indication as to the time left to give your talk. It starts counting down when you stop shaking it. Initially it lights all LEDs, and as time passes it progressively switches then off. When your time is up it displays a clock animation :-)  

To set the duration of the talk press button A.  You can then increment the talk length in 1 min steps by pressing button B, and button A decrements the talk length by 1 minute. To exit this mode, press Button A for more than 2 seconds. It will then tell you the length of the talk.

If you have other micro:bits with the "A-Shaky-Start-Talk-Timer" program it broadcasts a start message, which causes then to count down too - cool eh!

This is written in MicroPython.

If you press button B for more than 2 seconds whilst not counting down, this sets the timer into debug mode which sets the talk duration to 15 seconds. To exit debug mode just press the reset button.

A little trivia - the first submit was made from a Chromebook when on a train journey between Cromford to Nottingham when approaching Derby. Just after Derby saw the Britian’s rarest train the “Flying Banana” aka the New Measurement Train.


