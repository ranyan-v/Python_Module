#!/usr/bin/env python3


def secure_archive(
    file_name: str,
    operation: int,
    text: str = ""
) -> tuple[bool, str]:
    if operation == 1:
        try:
            with open(file_name, "r") as file:
                content = file.read()
                return (True, content)
        except OSError as error:
            error_msg = str(error)
            return (False, error_msg)

    elif operation == 2:
        try:
            with open(file_name, "w") as file:
                file.write(text)
                return (True, 'Content successfully written to file')
        except OSError as error:
            error_msg = str(error)
            return (False, error_msg)

    else:
        return (False, "invalid operation")


def main() -> None:
    print("=== Cyber Archives Security ===\n")

    print("Using 'secure_archive' to read from a nonexistent file:")
    result = secure_archive("/not/existing/file", 1)
    print(result)
    print()

    print("Using 'secure_archive' to read from an inaccessible file:")
    result = secure_archive("/etc/master.passwd", 1)
    print(result)
    print()

    print("Using 'secure_archive' to read from a regular file:")
    result = secure_archive("ancient_fragment.txt", 1)
    print(result)
    print()

    print("Using 'secure_archive' to write previous content to a new file:")
    if result[0]:
        result = secure_archive("new_file", 2, result[1])
        print(result)
    else:
        print("ERROR: content does not exist!")


if __name__ == "__main__":
    main()
