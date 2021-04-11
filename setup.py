from setuptools import setup

App=["GUI.py"]
OPTIONS = {
    "argv_emulation": True,

}

setup(
    app=App,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"]
)