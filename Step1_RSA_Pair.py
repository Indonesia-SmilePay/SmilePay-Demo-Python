from Crypto import Random
from Crypto.PublicKey import RSA

encoding_utf8 = 'utf-8'
PRIVATE_KEY_BEGIN = '-----BEGIN PRIVATE KEY-----'
PRIVATE_KEY_END = '-----END PRIVATE KEY-----'
PUBLIC_KEY_BEGIN = '-----BEGIN PUBLIC KEY-----'
PUBLIC_KEY_END = '-----END PUBLIC KEY-----'


def rsa_create_key(bits):
    print("=====> step1 : Create RSA Key")
    random_generator = Random.new().read
    rsa = RSA.generate(bits, random_generator)

    pkcs8_private_key = rsa.exportKey(format='PEM', passphrase=None, pkcs=8, protection=None)
    private_key_with_title_and_bottom = pkcs8_private_key.decode("utf-8")
    private_key_string = private_key_with_title_and_bottom.removeprefix(PRIVATE_KEY_BEGIN) \
        .removesuffix(PRIVATE_KEY_END).replace('\n', "")

    public_pem = rsa.publickey().exportKey()
    public_key_with_begin_and_end = public_pem.decode(encoding_utf8)
    public_key_string = public_key_with_begin_and_end.removeprefix(PUBLIC_KEY_BEGIN) \
        .removesuffix(PUBLIC_KEY_END).replace("\n", "")

    print("private_key_string=", private_key_string)
    print("public_key_string=", public_key_string)
    print("Please note this set of [RSA Key Pair] and send the [public key] to SmilePay." +
          "so that SmilePay can verify the request")
    return public_key_string, private_key_string


# run this. Then get rsa pair, keep PrivateKey yourself, put publicKey to smilePay
rsa_create_key(2048)

# privateKeyStr = MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDGWPgn9MHGpINP55SCJnBIoti5GU4/50ijdvna6ErZLpwLb0CYIlUaXS6YYv2GMW8SXyT2CaVb53tlS7Y6tSzgVNvGB07wJJkkq66ZLlXEkpsXu4lXOgz1D+jxubrdofbVNj5RK3PC/JQjL4brueuBuXyGSWBfSviCy2DximOPh/yCwslK6Fa8JPwehoBFHzECSOmZkPxg1F7VMxKH6EF/qSt5/KAe9fFwe1Nu6ro5pciFK6gEBTuO+p6fnvUEDepW83Ca0hsTqil7Uy1Ule1soQuQH0RWab6MBRqcfeuk82qDnmCaEAZ+PMdX51vxKMvJgtk7un2vBA4yt7hfJ1PbAgMBAAECggEAEnjjt5joWQ8mOZFYN9zLlUAxTd/I9VOdZLfmYhhDLEHWf4wfaGu+IEPwXHnPoalF7mCVCSLx1wLSb6ci9Am+ga/1fdZdaCkIaC1jB9oUW8fJkObCzjBWV5ZhO+3vtMdqPQYdvKJ+1/h89V/uQVLh14WGTt1Tj9xkE45MW4JnbkzyS3CNrzSIlBl0w1PEyPHoqv4wOZjSinedMsKE0IAXhgOu4hClebkeX+0eBvkVNi17+KHK+Aizf2DwJ6+RUUCeGr7yKdOOBxZxkEEEKwHNRkjG0MH69s3Vs80w2NSM89xYqX8No5dwMC0Hhp/i87k2o/qM+J0BuLI9uee9KpXqUQKBgQDS6VbTXF4O2g88OKvH//4CSsG6N8ySAHmJJfNha4u7kmCQz9iLNblRI4Aoei4KIVdY/kHorSijMSa025ki8ebQLw7G5Me5nqBOiuRqlIbXfTaCxjWggzm434mPs/2998GGPEIm1g+qBML2gv42XqG391hrOFpx0EaozmR6JBT+8QKBgQDwwAlo+JOPLlCvfHiMEu+/bMU7F9HKJDOsgG5fFxScUfBBVhXslpV6h23iXp4v/VmF+5EeCIE4gInXEyj9Yn9gpaL72Gdf8PXyZel9WrRfL3CyH0vnR1DM60FHAFmEFUkFvCmzDyOqZmyt2DpYcd4y9Kfs/Ts/iRfvAFAtoO1XiwKBgE59IZ+0nxg91C+gE2VxgdDOizvGqi2nWZNNeT5G7JBYT/F0N+zOiHGGmZn2pg2FDOGEdXimgBoDH5lso5eamD/fU0t3NlCAlL3F+G0lauzknxWZt7lNPHztS18cJ5C7k9xlrmSPgvLNpNRiOUJ4gwxYUyJLrXTvgmwtqry9ksaxAoGAFkiQFmk7rzsIONX6imyOSFeXAds4jc9AAS16Cc8nFzj2VfXT3awqdcbnQtajKan3iVE5o2ACJeqv13pshteBFr7+EPV8zAKPoToRnIqyu0S216XR7rxJHE6CIkJEBte5hJBgA7TZBkKouIaVD+6qNGk0ydi+jSjxUCvlP/PvQ/UCgYBa/ANDflVEvas7txSmqJJ4mDyExs3lcQ2dEBVj6cbfEGDJH0QiOJwbnTAKnub7nNJEWIzIjmNBLoZBUQ1Ox8rRYqvLs0Edl99Y3CFx4boRuBB690kFABl3XzAwpWX266vZfRCg8BcGqpH/BTuAvSW4gHKCGhyqGlDes8w9OUq+4A==
# publicKeyStr  = MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxlj4J/TBxqSDT+eUgiZwSKLYuRlOP+dIo3b52uhK2S6cC29AmCJVGl0umGL9hjFvEl8k9gmlW+d7ZUu2OrUs4FTbxgdO8CSZJKuumS5VxJKbF7uJVzoM9Q/o8bm63aH21TY+UStzwvyUIy+G67nrgbl8hklgX0r4gstg8Ypjj4f8gsLJSuhWvCT8HoaARR8xAkjpmZD8YNRe1TMSh+hBf6krefygHvXxcHtTbuq6OaXIhSuoBAU7jvqen571BA3qVvNwmtIbE6ope1MtVJXtbKELkB9EVmm+jAUanH3rpPNqg55gmhAGfjzHV+db8SjLyYLZO7p9rwQOMre4XydT2wIDAQAB
