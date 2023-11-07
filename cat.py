from subprocess import Popen, PIPE

c = Popen(["cat"], stdin=PIPE, stdout=PIPE)

s = input("Enter a prompt: ")

out = c.communicate(s.encode())

print(f"Output was: {out}")