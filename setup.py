"""
setup.py: Configurations for install and setup BRKGA-MP-IPR.

(c) Copyright 2019, Carlos Eduardo de Andrade. All Rights Reserved.

This code is released under LICENSE.md.

Created on:  Nov 15, 2019 by ceandrade
Last update: Nov 15, 2019 by ceandrade

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="BRKGA-MP-IPR", # Replace with your own username
    version="0.9",
    author="Carlos Eduardo de Andrade",
    author_email="ce.andrade@gmail.com",
    description="The Multi-Parent Biased Random-Key Genetic Algorithm "
                "with Implict Path Relink",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ceandrade/brkga_mp_ipr_python",
    packages=setuptools.find_packages(),
    # classifiers=[
    #     "Programming Language :: Python :: 3",
    #     "License :: OSI Approved :: MIT License",
    #     "Operating System :: OS Independent",
    # ],
    python_requires='>=3.7',
)

print(setuptools.find_packages())