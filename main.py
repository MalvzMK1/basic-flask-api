from os import environ
from dotenv import load_dotenv
from app import create_app

def main() -> None:
  app = create_app()

  app.run(debug=True)

if __name__ == '__main__':
  main()