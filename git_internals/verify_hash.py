'''
When diffing with git diff we get the following:

  diff --git a/notes.md b/notes.md <--- explains the 2 paths of files compared 
  index 87bf73d..0e290af 100644 <--- hashes the content before and after SHA-1 
  --- a/notes.md <--- --- and +++ are the conventions for old and new
  +++ b/notes.md
  @@ -22,3 +22,4 @@ git status -s : shortened version <--- hunk header, the line section and lines that changed


Index is saying that we currently have a new version in staging
And shows the 2 hashes of the files being compared
ie. hash_a .. hash_b

git uses SHA-1 in this format:

    sha1("<obj type> + <byte_length> + "\0" + <file_contents>")

'''

from hashlib import sha1 
from pathlib import Path
import subprocess

h = sha1()
fpath = Path("./notes.md")

with open(fpath, "rb") as f:
    content = f.read()

obj_type = "blob"
byte_len = len(content)

header = f"{obj_type} {byte_len}\0".encode()

h.update(header + content)

manual_hash = h.hexdigest()

git_hash = subprocess.check_output(["git", "hash-object", "notes.md"], text=True).strip()

assert git_hash == manual_hash 

print(f"git's: {git_hash} \nmanual: {manual_hash}")
