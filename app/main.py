import subprocess
import sys


def run_local(argv: list[str]):
    completed_process = subprocess.run(argv, capture_output=True)
    return completed_process.stdout.decode("utf-8")


def main():
    local_res = run_local(sys.argv[3:])
    print(local_res)


if __name__ == "__main__":
    main()
