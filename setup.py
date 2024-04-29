from setuptools import find_packages, setup

setup(
    name="MCQ Generator",
    version="0.0.1",
    author="Rohith B",
    author_email="rohithb.ai21@bmsce.ac.in",
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
    )