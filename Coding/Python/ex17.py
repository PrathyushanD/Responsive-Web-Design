from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# We can do these two in one line, how?
in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to-file)}")
print("Ready, hit RETURN to comtinue. CTRL-C to abort")
input()

output_file = open(to_file, 'W')
output_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()
