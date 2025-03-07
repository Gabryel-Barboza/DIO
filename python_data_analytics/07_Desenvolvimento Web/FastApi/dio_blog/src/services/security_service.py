from time import time
from typing import Annotated
from uuid import uuid4

import jwt
from fastapi import Depends, HTTPException, Request, status
from fastapi.security import HTTPBearer

from src.schemas.auth_schema import JwtToken

SECRET = 'my-secret'
ALGORITHM = 'HS256'

# TODO: Entender mais sobre JWT e autenticação
# TODO: Alterar rota de login para username e password, procurar no db


def sign_jwt(user_id: int) -> JwtToken:
    now = time()
    payload = {
        'iss': 'curso-fastapi.com.br',
        'sub': user_id,
        'aud': 'curso-fastapi',
        'exp': now + (60 * 30),
        'iat': now,
        'nbf': now,
        'jti': uuid4().hex,
    }
    token = jwt.encode(payload, SECRET, algorithm=ALGORITHM)

    return {'access_token': token}


async def decode_jwt(token: str) -> JwtToken | None:
    try:
        decoded_token = jwt.decode(
            token, SECRET, audience='curso-fastapi', algorithms=[ALGORITHM]
        )
        _token = JwtToken.model_validate({'access_token': decoded_token})
        return _token if _token.access_token.exp >= time() else None

    except Exception:
        return None


class JwtBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JwtBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request) -> JwtToken:
        authorization = request.headers.get('Authorization', '')
        scheme, _, credentials = authorization.partition(' ')

        if credentials:
            if not scheme == 'Bearer':
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail='Not a Bearer scheme',
                )
            payload = await decode_jwt(credentials)

            if not payload:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail='Invalid or expired authentication token',
                )

            return payload
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Invalid authorization code',
            )


async def get_current_user(
    token: Annotated[JwtToken, Depends(JwtBearer())],
) -> dict[str, int]:
    return {'user_id': token.access_token.sub}


def login_required(current_user: Annotated[dict[str, int], Depends(get_current_user)]):
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail='Acesso Negado!'
        )

    return current_user
