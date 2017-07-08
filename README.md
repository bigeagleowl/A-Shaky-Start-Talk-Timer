# A-Shaky-Start-Talk-Timer

This is a BBC micro:bit count down talk timer to tell you how much time you have left to complete your talk. You start the timer by shaking the micro:bit. It gives you a visual indication as to the time left to give your talk. It starts counting down when you stop shaking it. Initially it lights all LEDs, and as time passes it progressively switches then off. When your time is up it displays a clock animation :-)  

To set the talk length just set the variable minutes to the duration you want the talk to be.

If you have other micro:bits with the "A-Shaky-Start-Talk-Timer" program it broadcasts a start message, which causes then to count down too - cool eh!

If you press button A whilst not counting down, this sets the timer into debug mode whichs sets the talk duration to 15 seconds. To exit debug mode just press the reset button.

This is written in MicroPython.

A little trivia - the first submit was made from a Chromebook when on a train journey between Cromford to Nottingham when approaching Derby.

