import modules.password_cracker as password_cracker

print('use_salts=True :\n')
password = password_cracker.crack_sha1_hash(
    'b305921a3723cd5d70a375cd21a61e60aabb84ec')
print(password)

password = password_cracker.crack_sha1_hash(
    'c7ab388a5ebefbf4d550652f1eb4d833e5316e3e')
print(password)

password = password_cracker.crack_sha1_hash(
    '5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8')
print(password)

password = password_cracker.crack_sha1_hash(
    '03810a46a2c1a0eae58d9332f01c32bdcec9a01a')
print(password)

print('\nuse_salts=False :\n')
password = password_cracker.crack_sha1_hash(
    "53d8b3dc9d39f0184144674e310185e41a87ffd5", use_salts=True)
print(password)

password = password_cracker.crack_sha1_hash(
    "da5a4e8cf89539e66097acd2f8af128acae2f8ae", use_salts=True)
print(password)
