from pathlib import Path, PureWindowsPath


#folder = Path("/tmp/pathlib_test/my_pathlib_file.txt")
folder = Path("/tmp", "pathlib_test", "my_pathlib_file.txt")

windows_path = PureWindowsPath(folder)

print(folder.read_text()) #read content of file

print(folder.name) #get the name of the file
print(folder.suffix)  #get extension
print(folder.stem)  # get filename without the extension

print(windows_path)

base = Path.home() # this gets the user home directory
#we can get a path the following way too:
guide = Path(base, 'Europe', 'France', Path('Paris', 'Eiffel_tower.txt'))
guide2 = guide.with_name('Notre_Dame.txt') # this changes the destination file or the last item in the previous path
print(guide)  
print(guide2)
print(guide.parent) # this will return Parents. The destination file is Eiffel_tower.txt and the parent is Paris. We can also do guide.parent.parent(as many times as it is allowed)

print("=" * 80)
"""Another great method of the Path class is glob . Just like globbing in Linux
Imagine we have a folder called Europe in the user home directory which contains subdirs France 
(with subdir Paris and Marseille which contains some file with .txt extensions) and Spain
(with subdir Barcelona which also contains some file with .txt ) and also a few .txt files in the 
Europe directory """
guide3 = Path(Path.home(), "Europe")
for txt in Path(guide3).glob('*.txt'):
    print(txt ) # this will return all the files in the Europe folder
print("=" * 80)
#To return all the .txt file in the Europe directory and subdirs we do the following
for txt in Path(guide3).glob('**/*.txt'):
    print(txt)

print('-' * 80)
for txt in guide3.glob('*.txt'): # Same result as line 32
    print(txt)

print(guide3.parents[2]) #This will return the parent x(2) level high of the destination folder/file(Europe)--> here it's '/'