from distutils.core import setup

import sys
import shutil

if sys.version_info < (2, 7):
    sys.exit("Python 2.7+ is required.")

shutil.copyfile("generate_circuit_id/generate_circuit_id.py", "generate-circuit-id")

setup(
    name="Generate Circuit ID",
    version="0.0.1",
    python_requires=">=2.7.0",
    packages=["generate_circuit_id"],
    install_requires=["click>=6.7"],
    license="Do What The F*ck You Want To Public License",
    long_description=open("README.md").read(),
    scripts=["generate-circuit-id"],
)
