# HackFu 2017

I'm writing this after completing the first ten HackFu 2017 challenges
presented by  [MWR Info Security] (https://hackfu.mwrinfosecurity.com/).  Since 
I actually started these challenges almost eight weeks earlier - please read 
with a sense of romanticism.  I may present something that fits in a sentence, but
simplifies the time, commitment, and number of things that went wrong before
solving the solution.
 
I have worked on challenges like this before, but this is the first that I've done 
while it was taking place. There was
an added sense of excitement that the answers are not yet on the 'net and a time
limit was always racing to stop me from finishing.  There was also a leaderboard
which added an additional level of competitiveness.  This writeup is the end of 
two months of working on these challenges and hopefully be of some interest to
others who just finished the competition.  It will also be bittersweet for the
future solvers.  They will immediately know that there may be clues here that 
will end their frustration, but take away their personal victory. 

What I recognized is needed to solve these challenges:
1. Domain Knowledge is important
2. Intuition is important
3. Confidence and Humility are important

What I had to learn or get better at technically:
1. VirtualBox
2. Linux - Kali, binwalk, strings, OllyDebug, EDB Debug, understanding the ELF file format
3. Windows7 - using IDA, Visual Studio
4. Mac - hexfiend, sonic visualizer
5. Reading assembly for the purpose of reverse engineering, buffer overflow concepts,
 steganography, reading file headers, and file carving


While I toiled away on these challenges I did not know where they would go or if 
I would solve them.  There was this unknown opportunity of almost reading the mind 
of an author who truly didn't want to overtly communicate their ending.  However, 
once solved I can't look back at them without thinking they are a bit simple.  In fact
when having an opportunity to chat with others who were working on challenges 
that I had already solved -- I could see they had the answer, but didn't quite
recognize that they simply had to, metaphorically, turn the key in the lock.  What
was so hard at one time now looks so simple.  

I'm sure that MWR had to balance the difficultly level of the challenges against
knowing the answers already.  I don't know the makeup of the people who attempted
the challenges, but I discovered them approx. a month after the three month
competition started.  One person appeared to have finished the initial ten in 
only a few weeks and it is unclear how much time anyone actually puts in.  

*Spoilers To The Challenges Exist Beyond This Point*

# Challenge 00
I consider this a pre-challenge -- its pretty simple - but in order to open the zip file
with all the challenges I had to get OpenSSL running.  So that's what that directory is 
in the depot. It is interesting to note that the leaderboard on the hackfu website showed
at least 40 people opened the challenges, but for whatever reason never completed any of 
the challenges.


# Challenge 01
My initial goal was simply to get on the leaderboard.  I figured if I could do
that I would feel like my bit of puzzling here and there had paid off.  I could feel
proud about finally completing a 'live' competition challenge.  

The first puzzle took me 12 days.


An image of Buzz Aldrin on the moon is provided:
- Zooming in and looking at the image showed a watermark in lower right
- Since the image looked legit I did a reverse Google image search and 
found an original
- I diffed the two images and the following phrase is revealed: DidTheMoonLandingReallyHappen?!?


The image file was fairly large:
- I examined the file using HexFiend to discover 'PK', 'pass3/password'
- I copied out the bytes of the PK header to the end of the file and saved it out. I later found out this is called carving.

The Zip File:
- The file would not open with the watermark password
- Using StegHide prompted me for a password -- and using the one found from the image it worked, producing: 
HackFuTheresAFalseWallInTheBackOfTheClosetQuiteObviousReally

# Challenge 02

Once on the board I was pretty stoked.  This challenge was maybe a week,
but I never felt desperate -- it seemed pretty straight forward.

The Erno Rubik.pdf:
- I printed out the coloured page, cut out the shape and taped together the cube.
- There was also some text underneath which I promptly sorted into three even lines.
- I was fairly quick to notice letters and numbers corresponded to colours and coordinates

The Cube:
- I went out and purchased an official Rubik's Cube
- I restickied the cube to match the one on the printout
- I solved the cube (with some help from a website)
- and did the rest on paper, writing out the letter for each coordinate, revealing: 
HackFuThreeBlocksNorthRightAtTheDoomsayerKnockThreeTimesOnTheUglyOrangeDoor

I should note that I also knew that I was on the right track because part of the 
HackFu rules was that all the final passwords had to start with 'hackfu' - so I knew
very quickly I was on the right path and was looking for that H even before I really knew
what I was doing.  This 'exploit' is something I used on several of the challenges.

# Challenge 03

So I work in a place that has an audio department - although I don't really know much about
audio.  I happened to be in the audio peeps space though when they were showing me how they 
could write words or hide pictures in the audio spectrum.  So when I saw the wav file I 
immediately jumped to software that would reveal this part of the audio.

The Wav file:
- Played the audio ('Twinkle Twinkle Little Star...')
- Opened the file in Sonic Visualizer (available on Mac and PC)
- The spectrogram was interesting - showed the bars of the melody, but also these little dots above each bar. While a colleague who saw the dots said 'morse code?' it didn't make sense because they were going up and down rather than short and long.
- 7 dots were above each bar though -- and I was in a coffee shop and wrote out each number which corresponded to letters in the alphabet: hackfuandallyourtrickshellbearandneverseemtomind

Like Challenge 02 -- the 'hac...' in the first few 7bits ensured I was on the right tracka nd revealed:
hackfuandallyourtrickshellbearandneverseemtomind

# Challenge 04

This challenge involved a key file and a pass file.  Since the pass file contained a 
relatively short phrase and there was no hidden data (it wasn't a zip or image file), 
I felt it had to be the password and plugged in the 'hackfu...' to the start.

The Key File:
- I did look for patterns first -- and saw there were some phrases that appeared to be repeated.
- Once I ran Python's collections.Counter() on the pass contents though it was clear that with 
only 27 unique items it must at least contain the alphabet and one extra (space/return/etc).
- I did run some letter frequency analysis, but combined with the 'hackfu' the key was revealed to be: 
hackfuthisisthefinalstatementofreindercartwrightfounderoftheorderofthespark

# Challenge 05

I'd be interested to know how others solved this one.  A 'broken' img file is provided.  I found
some software that did say it could 'fix it', but I wasn't interested in paying the cash for it.

The IMG file:
- Examined the file using HexFiend.  Scrolling through the file revealed patterns (blocks?) of content.
- A partial list of directories and files were present, so I started looking for those first and carved them out of the IMG: 

* lost+found, my-files, my-scripts (dirs?)
* /tmp/backups (dir)
*   encrypted.py (Found)
*   audio0.mp3 (Likely)
*   file0.ps  (Found)
*   arr.txt.enc (Likely)
*   gee.txt.enc (Likely)
*   bee.txt.enc (Likely)


The PS File:
- Looking at this file in a text editor revealed: %%Creator: That audio file has some interesting metadata...
- So opened the audio file to reveal:
* Angle Arithmetic (song)
* Acutes (artist) 
* Alphabet (Album)
- I was able to open the PS file properly in an Adobe PDF reader 
and printed out the file. My Mac however could not read the file.
- I printed this page out and after looking it over for a bit decided to count the triangles and see if it matched against the 
alphabet.  This revealed: wejustfireinside

The Py File:
- The file was a decryptor program.  And it required both encrypted texts and a password.
- I fed it the different text files one by one and used the password from the PS file. This produced files containing
streams of numbers which looked a lot like pixels.  Note the initial backup list hinted at the 'arr', 'gee', 'bee' files.


The Text Stream / JPG Files:
- Using PIL and Python -- I spit out new images based on the row length and number of rows creating a series of jpegs.
- I wrote out each one and did some guessing, but they all came together to form: 
hackfuihaveseenthenightgauntsintheirhauntsandtheoldonesatthebottomofthesea

# Challenge 06
This challenge fascinated me and was my favorite.  I had never heard of an ELF file - which is the first
thing you find out when examining the header.  I also didn't know how to deal with 
this file format at all.  I read up a bit about it and there is a lot of stuff that 
had to happen on my end but ultimately it involved setting up a virtual machine, 
installing linux.  Lucky for me the easiest one to get going was Kali. I had to chmod-x 
the file and it took me forever to figure out that I had to type ./ before I could even
execute the file. 

The MD5 titled file:
- I never did look into what the md5 hash was -- i should do that.
- Looking at this file revealed some interesting repeating text: Phantom-Key

The ELF file:
- Examined the file in a hex numbers. This revealed the ELF file format
- Strings on linus revealed a slew of text including some hex numbers.  They converted to the name: L. Ron Hubbard.  
This linked to the ascii art title 'Dianetic Decryptor'.
- I held onto this info as I tried to run the program which clearly stated that I had to 
reverse engineer the program or rename a file to move forward.
- I dumped the ASM of the ELF file and printed out the code to step through
it by hand.  I became focused on the 'create_decrypt_key' func and after a few
days the following was built up in the stackframe: phantom_bits

Renaming the MD5 to this file completed Part 1.

Rerunning the program provided another clue - which was that the key would be 
revealed on the date of the messiah's death.  L Ron's name was already found
so I changed the date of my virtual machine and my host machine to the date
of his death and ran the program again.  This revealed: 
hackfusummonthedemonatyourperilitisnotintelligentactuallyitsferal

# Challenge 07
This challenge was fairly simplistic -- probably spent the least amount of time 
on this one.  There are three images.  Two inputs and only one output.  The goal
is to find the 2nd output.

The output1.png File:
- Looked like a QR code
- Mapped the coloured noise blocks to teh black and white squares of the output

Creating Output2 file:
- Using the mapping from input1/output1 I remapped the values to create an output2.
- While there was a lot of holes in teh QR code generated -- i think this was a 
lesson in understanding how durable qr codes can be.  By snapping a pic of the image
with my phone - the qr code revealed: 
hackfuwearehonouredtohavewithusarevolutionaryofadifferentcalibre

# Challenge 08
This is the first challenge where I stumbled pretty hard and learned a lesson in humility.
I cannot explain this challenge without first griping about some missteps.  Like the 
other challenges I tried to follow wherever the puzzle's clues led me - believing that the
author(s) wanted me to ultimately solve the problem.  This puzzle led me down the
correct path -- but I became too distracted by a few 'too on the nose' clues.  I wonder if
others also fell into the same trap?

The Wav File:
- This file revealed a QR code in the spectrogram which contained: domoarigiatomrroboto

The 7z File:
- The file is password protected, but would not open with the phrase obtained from the QR code.
- The size of the file was interesting -- the last zip was bytes -- this was almost 8k - so it 
clearly held something else inside.

At this point I introduce you to the solution clue and the angst I would have for weeks trying to 
open this horrible little file.

The MD5 hashes:
- Both the file names were MD5 hashes -- but I didn't notice this until I googled one of them and 
it was revealed to be 'password'. However, I was not able to reproduce this hash in Python unless I 
added '\n' to the end --> 'password\n'.  The other hash was not googlable tho.  So I downloaded a 
1.6gig password list (supposedly all passwords publicly exposed over the past few years) and proceeded
to MD5 each one and compare it against the hash I had. 
- I ensured that each hash had the added '\n'.  Sure enough this revealed the second
 hash as: 'hellomoto\n'
- A this point I figured I could brute force the 7z with the same list and ran an automated
retry against the 7z file with two runs.  The first being the md5 hash of each password, and
the second was the plaintext. Unfrortunately for me -- I made an assumption that the '\n' was
needed.  After two days my little laptop completed the task, but the 7z was locked up tight.

Weeks Passed:
- I learned about Styx, killroy, watched the concert, learned about escaping, even watched
the video to find out what 'rock codes' were sprayed onto the walls.  I reexamined the wav
file, the 7z file - but nothing revealed itself.  I started seeing things that weren't there.
- At some point I received several emails from different people all reaching out to ask 
how I was getting on with #8.  Some said they too were stuck and we danced around what we 
knew and didn't know, but wished each other good luck and moved on.  One person however was
looking for information for a different challenge.  They had the answer - almost -- but it was
just slightly out of grasp -- like myself.   I gave him a series of prodding questions in a base64 encoding
text and in return he sent me a rot13 clue about #8.  Which was to go back and revisit the brute force.
- After two weeks of seeing all sorts of things that simply did not exist - the 7z file opened with: domoarigato
and inside was a mrroboto.png file.

I am sure I would not have finished this puzzle without the clue pointing me in the right 
direction.  I was too confident that my previous brute force attempt had already exhausted that avenue. 
It took me a bit to recover from this -- since my brain was generating a crazy complex layered crypto solution 
-- when it was really pretty straightforward.

The PNG:
The PNG is a 88x88 pixel image of squares with multiple colours per square except for a few that are
all white or all red.  A text file contained a clue that explained to go into the colours and to add one then take 
one away.  Also PYCHARM FTW! -- I love pycharm -- all my work is done in that IDE :)

- Used Pillow to read the three colours from each square and did the math and did a character cast.
- This revealed a table of letters which clearly had 'hackfuthe' on the far left and 'louratall' on the right.
- I did attempt to guess what was inside the rest as it wasn't immediatey clear how to solve this challenge.  Here are
some of my guesses:
* hackfutheseoddballschoosetocolourinsidethelinesiprayanamendmenttorgbcoulditbecalledcolouratall
* hackfutheoddballschoosetocolourinsidethelinesiprayanamendmenttwilightcouldbestbecalledcolouratall
- Ultimately, I needed to go for a hike -- and thinking on it I felt that there was a 
similarity to teh rubiks cube and wished I could 'twist' the letters -- and then it hit me, the 
red cubes needed to line up.  I had some paper with me and my phone containing an image of the letter pattern. I
rewrote out the letters lining up the red squares diagnoally and this revealed: 
hackfuthecolourintheoddbandsonthemeteorwasimpossibletodescribeonlybyanalogycoulditbecalledcolouratall

Finished this puzzle about 40 hours before the deadline.

# Challenge 09
The APK file in this challenge was thematically relevant with several other references
to Motorolla.  This was the first time I had encountered this type of file and a Google
search had me downloading a Chrome plugin called "Arc Welder" to run the file without 
the phone and APKTool (which I ran on the Linux Virtualbox) to both decompile and even 
rewrite changes to the file.

Part1: The APK File
- Running the file asks for a password and you have a time limit.  I used the APKTool to remove 
the timelimit and to stop hiding the text I was typing in.
- Long story short I found the xoring routine that was decoding the encrypted text, but wasn't 100% sure
what was going on -- so I went line by line and rewrote it in Python.  This revealed some logic errors - I wonder if 
this is a limitation of the debugger or happened by design by the challenge authors?  In either case running the Python 
script revealed: pomegranates2eds <-- note the 2 -- I changed it to an e: pomegranateseeds
- Entering this as the password produced a new file called soup.chef.

Part2: The chef file
- This file contained a list of ingredients followed by the method of prep.  By rearranging the incredents based on the
method and converting all th amounts to characters revealed: 
hackfuwhereitlandswesetourscene


# Challenge 10
Although Challenge 8 threw me for a loop and Challenge 1 took 12 days - I think 
this was the most difficult challenge in terms of doing the work.  You can know you have teh answer, 
but if you can't push through the logic of what is presented it won't matter.

This challenge involved a single exe file.  There is some text that comes up and a simple prompt to 
input some data.

The EXE file:
- I ran the file through strings and would come back to this a few times.  From the exposition to the error codes -- it 
all held clues.
- I opened this file in both IDA and OllyDbg.  IDA was great because it broke down the functions in a very clear way; 
however, Ollydbg was more useful as I could control which part of the registry I was focussed on and provide a relative
overview going up and down from that point.
- The program did something interesting which was to compare part of the input stream in an area of memory to a 
particular memory address.  Only that memory address was not in the stackframe of the function.  I'm assuming this is 
what is called a buffer overflow attack and you enter in text that is long enough to reach where you want it to go
but not intended by the original author.
- Using OllyDbg and stepping through the program I entered in the following inputs:
* asdf
* asdf2
* asdf3

NotYetDone: input3
- While I was now able to pass all three gates it simply exited instead of providing me with the key.
- I had identified the block of memory that had the encrypted text -- and saw that there was a xoring 
function that would decrypt it. 
- I know I failed to do something that would have made my life easy here -- but I turned to the previous 
'hackfu' exploit and ran all letter combinations on the encrypted text till I hit an 'h', then an 'a', and so on.  This
spelled out 'notyet' -- and I had seen that in the debugger.
- While I wasn't able to enter in the correct input phrase -- I was able to see in memory the three memory addresses I 
had previously pushed into areas, plus the 'notyetdone' phrase.  I used these in my xoring function rewritten in python
to generate the decryption key: 
- Using this as the xoring routine revealed: 
hackfutwinkleoutnowfoullittlestarwehavenointerestinwhatyouare

