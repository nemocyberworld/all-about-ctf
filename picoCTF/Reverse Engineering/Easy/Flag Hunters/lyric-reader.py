import re
import time

# --- Load the flag to be embedded into the song ---
flag = open('flag.txt', 'r').read()

# --- Create the introductory part of the song including the flag ---
secret_intro = \
'''Pico warriors rising, puzzles laid bare,
Solving each challenge with precision and flair.
With unity and skill, flags we deliver,
The ether’s ours to conquer, '''\
+ flag + '\n'

# --- Full song lyrics (with flag inside the intro) ---
song_flag_hunters = secret_intro +\
'''

[REFRAIN]
We’re flag hunters in the ether, lighting up the grid,
No puzzle too dark, no challenge too hid.
With every exploit we trigger, every byte we decrypt,
We’re chasing that victory, and we’ll never quit.
CROWD (Singalong here!);
RETURN

[VERSE1]
Command line wizards, we’re starting it right,
Spawning shells in the terminal, hacking all night.
Scripts and searches, grep through the void,
Every keystroke, we're a cypher's envoy.
Brute force the lock or craft that regex,
Flag on the horizon, what challenge is next?

REFRAIN;

Echoes in memory, packets in trace,
Digging through the remnants to uncover with haste.
Hex and headers, carving out clues,
Resurrect the hidden, it's forensics we choose.
Disk dumps and packet dumps, follow the trail,
Buried deep in the noise, but we will prevail.

REFRAIN;

Binary sorcerers, let’s tear it apart,
Disassemble the code to reveal the dark heart.
From opcode to logic, tracing each line,
Emulate and break it, this key will be mine.
Debugging the maze, and I see through the deceit,
Patch it up right, and watch the lock release.

REFRAIN;

Ciphertext tumbling, breaking the spin,
Feistel or AES, we’re destined to win.
Frequency, padding, primes on the run,
Vigenère, RSA, cracking them for fun.
Shift the letters, matrices fall,
Decrypt that flag and hear the ether call.

REFRAIN;

SQL injection, XSS flow,
Map the backend out, let the database show.
Inspecting each cookie, fiddler in the fight,
Capturing requests, push the payload just right.
HTML's secrets, backdoors unlocked,
In the world wide labyrinth, we’re never lost.

REFRAIN;

Stack's overflowing, breaking the chain,
ROP gadget wizardry, ride it to fame.
Heap spray in silence, memory's plight,
Race the condition, crash it just right.
Shellcode ready, smashing the frame,
Control the instruction, flags call my name.

REFRAIN;

END;
'''

# --- Max number of lines to prevent infinite looping ---
MAX_LINES = 100

# --- Reader function to sing the song starting from a given label (e.g., [VERSE1]) ---
def reader(song, startLabel):
  lip = 0                # Current line pointer
  start = 0              # Line number where startLabel appears
  refrain = 0            # Line number where [REFRAIN] appears
  refrain_return = 0     # Line number where 'RETURN' appears
  finished = False       # Flag to know when to stop reading

  # --- Split song into list of lines ---
  song_lines = song.splitlines()
  
  # --- Locate special markers: startLabel, [REFRAIN], RETURN ---
  for i in range(0, len(song_lines)):
    if song_lines[i] == startLabel:
      start = i + 1               # Start one line after the label
    elif song_lines[i] == '[REFRAIN]':
      refrain = i + 1              # Start refrain one line after [REFRAIN]
    elif song_lines[i] == 'RETURN':
      refrain_return = i           # RETURN keyword (placeholder for looping)

  # --- Start printing lyrics ---
  line_count = 0
  lip = start                     # Set the pointer to the start position
  while not finished and line_count < MAX_LINES:
    line_count += 1
    for line in song_lines[lip].split(';'):  # Handle multiple commands per line (separated by ;)
      if line == '' and song_lines[lip] != '':
        continue
      
      # --- Handle REFRAIN keyword (jump to refrain section) ---
      if line == 'REFRAIN':
        song_lines[refrain_return] = 'RETURN ' + str(lip + 1)  # Save position to return after refrain
        lip = refrain
      
      # --- Handle CROWD input (ask user for a singalong line) ---
      elif re.match(r"CROWD.*", line):
        crowd = input('Crowd: ')
        song_lines[lip] = 'Crowd: ' + crowd   # Replace CROWD with user's input
        lip += 1

      # --- Handle RETURN (jump back after refrain) ---
      elif re.match(r"RETURN [0-9]+", line):
        lip = int(line.split()[1])  # Jump to saved position after REFRAIN

      # --- Handle END (finish singing) ---
      elif line == 'END':
        finished = True

      # --- Normal lyrics line ---
      else:
        print(line, flush=True)
        time.sleep(0.5)  # Small delay between lines for effect
        lip += 1

# --- Start reading the song from [VERSE1] ---
reader(song_flag_hunters, '[VERSE1]')
