lines = [line.rstrip().split() for line in open('input07.txt')]

all_dirs = []
class File:
    def __init__(self, name, parent, size = 0):
        self.name = name
        self.parent = parent
        if parent:
            parent.children.append(self)
            parent.add_content(size)
        self.size = size
    def __repr__(self):
        return self.name + ' (' + str(self.size) + ')'
class Dir(File):
    def __init__(self, name, parent = None):
        super().__init__(name, parent)
        self.children = []
        all_dirs.append(self)
    def add_content(self, size):
        self.size += size
        if self.parent:
            self.parent.add_content(size)
    def __repr__(self):
        return super().__repr__() + ': ' + str(self.children)

root = Dir('/')
for fields in lines:
    if fields[0] == '$':
        command = fields[1]
        if command == 'cd':
            assert len(fields) == 3
            new_dir = fields[2]
            if new_dir == '/':
                actual = root
            elif new_dir == '..':
                assert actual, 'actual dir should be a valid object, but is \'None\''
                actual = actual.parent
            else:
                for child in actual.children:
                    if child.name == new_dir:
                        assert isinstance(child, Dir)
                        actual = child
                        break
                assert actual.name == new_dir
        else:
            assert command == 'ls' and len(fields) == 2
    else:
        assert command == 'ls' and len(fields) == 2
        qualifier, name = fields
        if qualifier == 'dir':
            Dir(name, actual)
        else:
            File(name, actual, int(qualifier))

print('Part one:', sum([dir.size for dir in all_dirs if dir.size < 100000]))
total_disk_space = 70000000
unused_space_needed = 30000000
maximum_space_used = total_disk_space - unused_space_needed
freeup_space_needed = root.size - maximum_space_used
print('freeup:', freeup_space_needed)
print('Part two:', min([dir.size for dir in all_dirs if dir.size > freeup_space_needed]))
