from setuptools import find_packages, setup

with open("requirements.txt", "r", encoding="utf-8") as f:
    requires = []
    for line in f:
        req = line.split("#", 1)[0].strip()
        if req and not req.startswith("--"):
            requires.append(req)

with open("project/__init__.py") as f:
    version = f.readlines()[-1].split()[-1].strip("\"'")

setup(
    name="project",
    version=version,
    packages=find_packages(exclude=["tests"]),
    install_requires=requires,
)
