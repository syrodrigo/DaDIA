#################################
# Usage: python convert_MSDIAL_MSP.py input_MSDIAL_MSP_file.msp
#################################
#coding: utf-8
from __future__ import print_function
import sys

input = sys.argv[1]
output_file = "Converted_Library.msp"

print("Loading MSP Library file\n")
with open(input) as fh:
	input_file = fh.read()

input_file = input_file.rstrip() + "\n"
input_file = input_file.lstrip()
input_file = input_file.replace("\t", " ")
input_file = input_file.replace("NAME:", "Name:")
input_file = input_file.replace("PRECURSORMZ:", "PrecursorMZ:")
input_file = input_file.replace("PRECURSORTYPE:", "Precursor_type:")
input_file = input_file.replace("FORMULA:", "Formula:")
input_file = input_file.replace("INCHIKEY:", "InChIKey:")
input_file = input_file.replace("IONMODE: Negative", "Ion_mode: N")
input_file = input_file.replace("IONMODE: Positive", "Ion_mode: P")
input_file = input_file.replace("COLLISIONENERGY:", "Collision_energy:")
input_file = input_file.replace("Num Peaks: 0\n", "Num Peaks: 1\n0.0 0\n")

segment_input_file = input_file.split("\n\n")
output_segment = []

for i in segment_input_file:
	l = i.split("\n")
	tmp = ["" for t in range(0, len(l))]
	for r in l:
		if "Name" in r:
			tmp[0] = r
		if "InChIKey" in r:
			tmp[1] = r
		if "Precursor_type" in r:
			tmp[2] = r
		if "PrecursorMZ" in r:
			tmp[3] = r
		if "Ion_mode" in r:
			tmp[4] = r
		if "Collision_energy" in r:
			tmp[5] = r
		if "Formula" in r:
			tmp[6] = r
		if "Comment" in r:
			tmp[7] = r
		if "Num Peaks" in r:
			tmp[8: 8 + (len(l) - l.index(r))] = l[l.index(r):]
	tmp = [x for x in tmp if x != ""]
	output_segment.append("\n".join(tmp))

output = "\n\n".join(output_segment) + "\n"
print("Converting...\n")
open(output_file, "w").write(output)