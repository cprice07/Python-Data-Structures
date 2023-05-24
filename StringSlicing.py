# 6.5 Write code using find() and string slicing (see section 6.10)
# to extract the number at the end of the line (text = "X-DSPAM-Confidence:    0.8475").
# Convert the extracted value to a floating point number and print it out.

# Given text value
text = "X-DSPAM-Confidence:    0.8475"
# Find intial index occurence of 0
pos = text.find('0')
# Find value of 5 starting at previously noted index of 0
spos = text.find('5', pos)
# Slice out number value 0.8475
# spos+1 is to stop slicing at 1 index after 5
total = text[pos : spos+1]
# Convert string to float
totalfl = float(total)
# Print out extracted value
print(totalfl)