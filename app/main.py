import os
import shutil
import subprocess
import sys
import tempfile


def subprocess_run(argv: list[str]):
    return subprocess.run(argv, capture_output=True)
    

def main():
    bin_path = sys.argv[2]
    with tempfile.TemporaryDirectory() as dir:
        shutil.move(bin_path, os.path.join(dir, bin_path))
        os.chroot(dir)
        completed = subprocess_run(sys.argv[3:])
        sys.stdout.buffer.write(completed.stdout)
        sys.stderr.buffer.write(completed.stderr)
        sys.exit(completed.returncode)


if __name__ == "__main__":
    main()
