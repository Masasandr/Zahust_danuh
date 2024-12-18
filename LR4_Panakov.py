# don't print anything in the console, because it will take to much time
import hashlib
import itertools

def crack(hash):
    for pin_tuple in itertools.product(range(10), repeat=5):
        pin = ''.join(map(str, pin_tuple))
        pin_hash = hashlib.md5(pin.encode()).hexdigest()
        
        if pin_hash == hash:
            return pin