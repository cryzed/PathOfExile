# PathOfExile
Python library and tools for interacting with Path of Exile.


## pathofexile/
Library for interacting with the Path of Exile client (only stuff allowed by
GGG). This currently only includes proper log parsing, which is needed for
Trades Companion-like applications.


## tradecompanion/
A scuffed trade companion application which runs and works on Linux. `xdotool`
is required. It works by monitoring and parsing the client's log file and
displaying the trade requests in an orderly interface. Also allows you to send
certain commands directly to the game, for example to invite the buyer to the
party or open a trade window.

![Screenshot](https://media.discordapp.net/attachments/242221235382124544/597124690355683338/b2aaddc9-02c2-489d-af10-3f0281d0b447.png)


### Notes
This is pretty rough around the edges currently and is missing quite a few
features still.
