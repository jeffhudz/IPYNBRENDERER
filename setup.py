import setuptools

with open("README.md","r",encoding ="utf-8") as f:
    long_description = f.read()
    
__version__ = "0.0.1"

REPO_NAME = "IPYNBRENDERER"

AUTHOR_USER_NAME ="jeffhudz"

SRC_REPO = "IPYNBRENDERER"
AUTHOR_EMAIL = "godfrenam@yahoo.com"

setuptools.setup(
    name = SRC_REPO,
    version= __version__,
    author_email = "godfrenam@yahoo.com",
    description = "small python project",
    long_description= long_description,
    long_description_content = "text/markdown",
    url =f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls= {
        "Bug Trucker":f"https://github.com/{AUTHOR_EMAIL}/{REPO_NAME}/issues",
        },
    package_dir={"":"src"},
    packages= setuptools.find_packages(where ="src")
    ,
 )
    
