from datetime import datetime, timedelta


import jwt

secret_key = "secret_key"


print(int(datetime.strptime(str(datetime.now() + timedelta(days=1)),
      "%Y-%m-%d %H:%M:%S.%f").timestamp()))


# def issue_jwt(expiration, user_id, role):

#     header = {
#         "alg": "HS256",
#         "typ": "JWT"
#     }
#     payload = {
#         "user_role": role,
#         "user_id": user_id,
#         "exp": int(datetime.strptime("2024-06-30", "%Y-%m-%d").timestamp())
#     }

#     token = jwt.encode(payload, secret_key,
#                        algorithm=header["alg"], headers=header)
#     return token


# def verify_jwt(token):
#     try:
#         decoded = jwt.decode(token, secret_key, algorithms=["HS256"])
#         return decoded
#     except jwt.ExpiredSignatureError:
#         return "Token expired"
#     except jwt.InvalidTokenError:
#         return "Invalid token"


# print(issue_jwt())
# print(verify_jwt(issue_jwt()))
