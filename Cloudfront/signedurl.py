import datetime

import os
### pip3 install cryptography boto3

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from botocore.signers import CloudFrontSigner

path='/Users/wyc/Desktop'
os.chdir(path)

### Please replace with your information

key_id = "KHG1OKQ6CZ4G8"
##url = "https://s3.wyc.world/test.png"
url = "https://dvp52oefp1ku8.cloudfront.net/test.png"
##url = "https://d2oli2squmf00i.cloudfront.net/index.html"
private_key_filename = "CloudFront-Workshop-Private-Key.pem"
expire_date = datetime.datetime(2025, 6, 20)
message='test'

def rsasigner(message):
    with open(private_key_filename, 'rb') as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )
    return private_key.sign(message, padding.PKCS1v15(), hashes.SHA1())


cloudfront_signer = CloudFrontSigner(key_id, rsasigner)

# Create a signed url that will be valid until the specific expiry date
# provided using a canned policy.
signed_url = cloudfront_signer.generate_presigned_url(
    url, date_less_than=expire_date)
print(signed_url)

'''
https://s3.wyc.world/test.png?Expires=1750377600&Signature=uq16Kn8GdaOslA99JFmEg76UAfCUhAXaLkSICI5XYhsURPAR52407Pk6Jn7WTfPMXmpvN4qDGERs2N4RWQMWrHtev9fRhb9BFosm4US86-TTEPrCDDCMyVpOCa5dsBX65Al84~UpW~sgJBeGoj8ZBw7F4PVA4FZtdJetzRHMQ~URq~FjZPpfseS~ClsIPmDszy0FBA9U6XqBcckV-RgrjdAD-b9SUBauTCYtahm438yAf2UW2fIRMNR-FfT9kiun146t32iR~uthDAi1CipoYWpd31fGTJcHfzvn0VHwveOqRMUylGvxAVYtmjzFzkljhNUBHF8LQjZHMoYnypeJtw__&Key-Pair-Id=KHG1OKQ6CZ4G8
'''
