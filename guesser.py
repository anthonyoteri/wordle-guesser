#!/usr/bin/env python3
"""A simple tool for wordls."""


import argparse
import random
import re
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--automate", action="store_true", default=False)
    parser.add_argument(
        "-w", "--wordlist", type=Path, required=False, default=Path("./wordlist.txt")
    )
    parser.add_argument("-p", "--pattern")

    args = parser.parse_args()

    with open(args.wordlist, "r") as wordlist:
        words = [w.strip() for w in wordlist.readlines()]

    if args.pattern:
        r = re.compile(args.pattern)
        filtered_list = [w for w in words if r.match(w)]
        print(", ".join(filtered_list))
        return

    if args.automate:

        guess = random.choice(words)
        print("Guess: %s" % guess)

        for i in range(6):
            result = input("Enter result: (./y/g for each position): ")

            if result.lower() == "ggggg":
                break

            for i, (g, r) in enumerate(zip(guess, result)):
                if r.lower() == "g":
                    words = list(filter(lambda w: w[i] == g, words))
                if r.lower() == "y":
                    words = list(filter(lambda w: g in w and w[i] != g, words))
                if r.lower() == ".":
                    words = list(filter(lambda w: g not in w, words))

            if len(words) == 1:
                print("Word is %s" % words[0])
                return

            if len(words) == 0:
                print("I give up!")
                break

            print("Remaining words %s" % ", ".join(words))
            guess = random.choice(words)
            print("Next guess is %s" % guess)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        raise SystemExit(0)
