from service import create_app

if (__name__ == "__main__"):
    app = create_app()
    app.run( port=5500, debug=True)

    