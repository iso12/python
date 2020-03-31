import os
import random
import sys
import rabin_miller as rabinMiller, cryptomath_module as cryptoMath

min_primetive_root = 3

def main():
    print("Making key files...")
    makeKeyFiles("elgamal", 2048)
    print("Key files genration succesful")


def primitiveRoot(p_val):
    print("Generating primitive root of p")

    while True:
        g = random.randrange(3, p_val)
        if  pow(g, 2, p_val) == 1:
            continue
        if pow(g, 2, p_val) == 1:
            continue
        return g


def generate(KeySize):
    print("Generating prime p...")
    p = rabinMiller.genrateLargePrime(keySize)
    e_1 = primitiveRoot(p)
    d = random.randrange(3, g)
    e_2 = cryptoMath.findModInverse(pow(e_1, d, p), p)

    publicKey = (KeySize, e_1, e_2, p)
    privateKey = (KeySize, d)

    return publicKey, privateKey

def makeKeyFiles(name, keySize):
    if os.path.exists("%s_pubkey.txt" % name) or os.path.exists(
        "%s"_privkey.txt % name

    ):

    print("\n WARNING:")
    print(
        '"%s_pubkey.txt" or "%s_privkey.txt" already exists. \n'
            "Use a different name or delete these files and re-run this program."
            % (name, name)
    )

    sys.exit()

    publicKey, privateKey = generateKey = generateKey(keySize)
    print("\nWriting public key to file %s_pubkey.txt..." %  name)
    with open("%s_pubkey.txt" % name, "w") as fo:
        fo.write(
            "%d,%d,%d,%d" % 
        )
