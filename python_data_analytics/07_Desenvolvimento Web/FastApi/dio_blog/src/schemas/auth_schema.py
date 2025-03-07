from pydantic import BaseModel


class AccessToken(BaseModel):
    iss: str
    sub: int
    aud: str
    exp: float
    iat: float
    nbf: float
    jti: str


class JwtToken(BaseModel):
    access_token: AccessToken


class LoginIn(BaseModel):
    user_id: str
