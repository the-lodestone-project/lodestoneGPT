from setuptools import setup, find_packages
import os

package_name = "lodestonegpt"


all_requires = [
    "openai",
    "bs4",
    "selenium",
    "numpy",
    "tiktoken>=0.3.3",
    "requests",
    "colorama",
    "duckduckgo_search>=2.9.4",
    "google-api-python-client",
    "webdriver_manager",
    "simpleeval",
    "transformers[hf]",
    "sentence_transformers[hf]",
    "accelerate[hf]",
    "bitsandbytes[hf]",
    "torch[hf]",
    "python-dotenv",

]

install_requires = []
extras_require = {}

for req in all_requires:
    req = req.strip()
    if not req:
        continue
    if req.endswith("]"):
        sp = req.rsplit("[", 1)
        profile = sp[1][:-1]
        package = sp[0]
        if profile not in extras_require:
            extras_require[profile] = []
        extras_require[profile].append(package)
    else:
        install_requires.append(req)


if __name__ == "__main__":
    setup(
        install_requires=install_requires,
        extras_require=extras_require,
        packages=find_packages(),
        name=package_name,
        version="0.1.0",
        description="Modular Auto-GPT Framework Build For Project Lodestone",
        entry_points={"console_scripts": ["lodestonegpt = lodestonegpt.loops.cli:main"]},
    )
