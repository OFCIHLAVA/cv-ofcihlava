import base64
import argparse
import sys


def main():
    p = argparse.ArgumentParser(description="Convert image to base64 string.")
    p.add_argument("-img", "--image", help="Path to image to process.")

    args = p.parse_args()

    try:
        with open(args.image, "rb") as f:
            raw = f.read()
    except Exception as e:
        print(f"Exception: {e} when reading file: {args.image}")
        sys.exit(1)

    b64_string = base64.b64encode(raw).decode("ascii")
    if b64_string:
        with open("img_data.txt", "w", encoding="utf-8") as o:
            o.write(b64_string)


if __name__ == "__main__":
    main()
