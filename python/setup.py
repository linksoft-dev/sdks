import os

from setuptools import find_packages, setup

with open("README.md", encoding="utf-8") as leia:
    descricao = leia.read()

setup(
    name="linksoft-sdk",
    version=os.environ.get("SDK_VERSION", "0.0.0"),
    description="Cliente gRPC da API do sistema",
    long_description=descricao,
    long_description_content_type="text/markdown",
    url="https://github.com/linksoft-dev/sdks",
    license="MIT",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    package_data={"": ["*.pyi"]},
    python_requires=">=3.9",
    install_requires=[
        "grpcio>=1.84.0",
        "protobuf>=7.36.2",
        "googleapis-common-protos>=1.75.0",
    ],
)
