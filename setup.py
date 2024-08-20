from setuptools import setup, find_packages

setup(
    name='chainlit',
    version='1.1.202',
    description="Build Conversational AI.",
    author="Chainlit",
    license="Apache-2.0 license",
    keywords=['LLM', 'Agents', 'gen ai', 'chat ui', 'chatbot ui', 'openai', 'copilot', 'langchain', 'conversational ai'],
    url="https://github.com/Chainlit/chainlit",
    packages=find_packages(exclude=["frontend", "copilot"]),
    include_package_data=True,
    install_requires=[
        "httpx>=0.23.0",
        "literalai==0.0.601",
        "dataclasses_json>=0.5.7",
        "fastapi>=0.110.1",
        "starlette>=0.37.2",
        "uvicorn>=0.25.0",
        "fastapi-socketio>=0.0.10",
        "aiofiles>=23.1.0",
        "syncer>=2.0.3",
        "asyncer>=0.0.2",
        "nest-asyncio>=1.5.6",
        "click>=8.1.3",
        "tomli>=2.0.1",
        "pydantic>=1,<3",
        "python-dotenv>=1.0.0",
        "uptrace>=1.22.0",
        "watchfiles>=0.20.0",
        "filetype>=1.2.0",
        "lazify>=0.4.0",
        "packaging>=23.1",
        "python-multipart>=0.0.9",
        "pyjwt>=2.8.0"
    ],
    extras_require={
        "tests": [
            "openai>=1.11.1",
            "langchain>=0.1.5",
            "llama-index>=0.10.15",
            "transformers>=4.30.1",
            "matplotlib>=3.7.1",
            "farm-haystack>=1.18.0",
            "plotly>=5.18.0"
        ],
        "mypy": [
            "mypy>=1.7.1",
            "types-requests>=2.31.0.2",
            "types-aiofiles>=23.1.0.5"
        ],
        "custom-data": [
            "asyncpg>=0.29.0",
            "SQLAlchemy>=2.0.28",
            "boto3>=1.34.73",
            "azure-identity>=1.14.1",
            "azure-storage-file-datalake>=12.14.0"
        ],
        "slack": [
            "slack_bolt>=1.18.1"
        ],
        "discord": [
            "discord>=2.3.2"
        ]
    },
    entry_points={
        'console_scripts': [
            'chainlit=chainlit.cli:cli',
        ],
    },
    python_requires=">=3.8.1,<4.0.0",
)