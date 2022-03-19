import pyupbit
import os
import jwt
import uuid
import requests
import json
import hashlib
import time
import logging
from urllib.parse import urlencode
from decimal import Decimal

access_key = f"8B7Xz5qSJmyZ3hLNXKpezCIeSH2HEA23dQyiykKS"
secret_key = f"q0aXScp67AYGG4hUT8iJQRNoZthFIVivRNpDGPCU"
server_url = f"https://api.upbit.com"