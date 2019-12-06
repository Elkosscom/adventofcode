import requests
import os

with open("sessionid", "rb") as f:
    SESSIONID = f.read().decode("utf8")


def get_response(day):
    year = 2019
    uri = f"http://adventofcode.com/{year}/day/{day}/input"
    response = requests.get(uri, cookies={"session": SESSIONID})
    return response.content


def main():
    try:
        day = int(input("Please input day:\n"))
    except ValueError:
        print("Please input a number")
        exit(1)

    folder = f"Day {day}"
    if folder in os.listdir(os.getcwd()):
        print("Data already exists")
    else:
        try:
            os.mkdir(folder)
        finally:
            with open(f"{folder}\\input", "wb") as f:
                f.write(get_response(day))


if __name__ == "__main__":
    main()
