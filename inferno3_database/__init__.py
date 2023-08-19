import uvicorn

# with open("config.yaml") as file:
# config = yaml.load(file, Loader=yaml.FullLoader)
# print("Successfully loaded the configuration")


def start_web_server() -> None:
    uvicorn.run(
        "inferno3_database.main:app",
        reload=True,
    )
