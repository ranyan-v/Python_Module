import alchemy

print(
    "=== Alembic 4 ===\n"
    "Accessing the alchemy module using 'import alchemy'"
    f"\nTesting create_air: {alchemy.create_air()}\n"
    "Now show that not all functions can be reached\n"
    "This will raise an exception!"
    )
# try:
#     print(alchemy.create_earth())
# except Exception as e:
#     print(
#         f"\nTesting the hidden create_earth: {e}\n"
#         )
alchemy.create_earth()
