It's a key value store with a graph layered on top

key is the sha-1 of the value
value is a compressed blob of bytes which is either blob, tree, commit, or tag 

you can poke at the db directly, ops: 

git hash-object -w <file> : PUT writes value and return key
git cat-file -p <sha> : GET value by key
git cat-file -t <sha> : type of the value 

3 states: 
- modified: changed file, not commiteted in db yet
- staged: marked as modified to go into next commit snapshot
- commited: safely stored in local db

git doesn't use a db like sqlite, it uses the filesystem

.git/index : this is file that stores what will go into the next commit, it's the same as staging area

git status -s : shortened version

git diff : shows changes that are not staged
git diff --staged : shows staged
git diff --cached : shows staged so far, cached and staged are synonims 

git commit : opens editor
git commit -v : opens editor and shows the diff 
git commit -m : inline message
git commit -a : skips staging area and directly adds modified changes 

git rm --cached <file> : removes the file if you checked in before
git log -p -2: -p flag shows the patches, -<num> limits log count
