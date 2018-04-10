<h3> python_vote_bot_attempt </h3>

I tried to make a vote bot for google forms that would click on something as many times as possible

This was just made for selecting the 6th thing in a list of multiple choice options on a google form.
Quick and dirty just doing it for a friend. You'll also need chromewebdriver in the same directory which you cnan get here: https://chromedriver.storage.googleapis.com/index.html?path=2.37/





<h1> How to Use: </h1>

1. Download the zip file and extract it somewhere or clone the repo and put it somewhere.
2. Change the URL in the spamtest file to whatever you want the url to be. if you want it to pick something other than the 6th option go and find that then change the values in the for loop. 
2. Go into your shell and cd over to the directory you extracted the files into
3. You may have to have selenium installed for this to work. Either with `pip3 install selenium`(might be just pip for you) or `conda install selenium` 
4. run the script with `python3 spamtest.py "number of votes"`(python3 might also just be python) or 
you can chmod +x the script and run with `./spamtest.py "number of votes"` but that's a little bit pointless. If you don't add the argument number at the end it will default to 25000, but you can change that if you want to.

<h1> Random Notes </h1>

looks like Reloading The page back to the start is faster than clicking the "submit again button"

When method with reloading time is alone time for 20 is: `16.47681474685669`

When Method with realoading time is first time for 20 is: `14.862403631210327`

When Method with reloading time is second time for 20 is: `14.325935363769531`



When method with clicking time is alone, time for 20 is: `18.313595056533813`

When Method with clicking time is first, time for 20 is: `17.434386253356934`

When Method with clicking time is second time for 20 is: `17.580833911895752`