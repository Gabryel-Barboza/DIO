from fastapi import FastAPI

from .controllers import post_controller

# Possui similaridades com o Flask
app = FastAPI()
app.include_router(post_controller.router)


# Execute o servidor com uvicorn caminho:instância_app --reload (recarrega servidor se alteração)
# uvicorn src.main:app --reload
