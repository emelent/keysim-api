# Key Sim API

This is a basic keyboard input simulator I'm using to control powerpoint slides
(these presenter remotes are pricy).

It has two parts:
- The flask rest API
- The html front-end

The front-end sends key click requests to the server and the server simulates
these keypresses on the hosts. There's no security of any kind here, this is
not something enterprise level, and it's just a convenience tool I use.
