import uvicorn


if __name__ == "__main__":
    uvicorn.run(
        "app.backend.app:app",
        # host='192.168.0.101',
        # port=8000,
        reload=True)
