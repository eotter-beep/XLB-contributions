from setuptools import setup, find_packages

setup(
    name="xlb",
    version="0.2.1",
    description="XLB: Accelerated Lattice Boltzmann (XLB) for Physics-based ML.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Mehdi Ataei",
    url="https://github.com/Autodesk/XLB",
    license="Apache License 2.0",
    packages=find_packages(),
    install_requires=[
        "matplotlib>=3.10.7",
        "numpy>=2.3.4",
        "pyvista>=0.46.3",
        "trimesh>=4.8.3",
        "warp-lang>=1.10.0.dev20251018",
        "numpy-stl>=3.2.0",
        "pydantic>=2.12.3",
        "ruff>=0.14.1",
        "jax>=0.8.0",  # Base JAX CPU-only requirement
    ],
    extras_require={
        "cuda": ["jax[cuda12]>=0.4.34"],  # For CUDA installations
        "tpu": ["jax[tpu]>=0.4.34"],  # For TPU installations
    },
    python_requires=">=3.10",
    dependency_links=["https://storage.googleapis.com/jax-releases/libtpu_releases.html"],
)
