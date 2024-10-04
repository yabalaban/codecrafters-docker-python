import subprocess
import sys


def subprocess_run(argv: list[str]):
    return subprocess.run(argv, capture_output=True)
    

def main():
    completed = subprocess_run(sys.argv[3:])
    sys.stdout.buffer.write(completed.stdout)
    sys.stderr.buffer.write(completed.stderr)


if __name__ == "__main__":
    main()
