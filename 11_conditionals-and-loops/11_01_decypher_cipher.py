# Decipher the message within the `secret` variable.
# Pick out only the alphabetic characters, not the numbers.
import re

secret = "2349h30023388281e3299371l1l3094842o0333322883"
solution =re.sub(r'[^a-zA-Z]', '', secret)

print(solution)

