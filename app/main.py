import os
import shutil
import subprocess
import sys
import tempfile
import ctypes


libc = ctypes.CDLL(None)
UNSHARE_SYSCALL = 272
CLONE_NEWPID = 0x20000000


def subprocess_run(argv: list[str]):
    return subprocess.run(argv, capture_output=True)
    

def main():
    libc.syscall(UNSHARE_SYSCALL, CLONE_NEWPID)

    bin_path = sys.argv[3]
    with tempfile.TemporaryDirectory() as dir:
        shutil.copy(bin_path, dir)
        os.chroot(dir)
        completed = subprocess_run([f'/{os.path.basename(bin_path)}'] + sys.argv[4:])
        sys.stdout.buffer.write(completed.stdout)
        sys.stderr.buffer.write(completed.stderr)
        sys.exit(completed.returncode)


if __name__ == "__main__":
    main()
