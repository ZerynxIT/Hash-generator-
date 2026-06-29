import hashlib

print("=" * 40)
print("        ZERYNX HASH GENERATOR")
print("=" * 40)

text = input("Enter text: ")

algorithms = {
    "1": "md5",
    "2": "sha1",
    "3": "sha224",
    "4": "sha256",
    "5": "sha384",
    "6": "sha512"
}

print("\nChoose Algorithm:")
print("1 - MD5")
print("2 - SHA1")
print("3 - SHA224")
print("4 - SHA256")
print("5 - SHA384")
print("6 - SHA512")

choice = input("\nSelect: ")

if choice in algorithms:
    algorithm = algorithms[choice]

    hash_object = hashlib.new(algorithm)
    hash_object.update(text.encode("utf-8"))

    print("\nResult:")
    print(hash_object.hexdigest())

else:
    print("\nInvalid selection.")
