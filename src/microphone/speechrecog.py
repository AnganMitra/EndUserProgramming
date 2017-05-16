#!/usr/bin/env python3

import speech_recognition as sr

# obtain path to "english.wav" in the same folder as this script
from os import path
AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "output.wav")
#AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "french.aiff")
#AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "chinese.flac")

# use the audio file as the audio source
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source) # read the entire audio file

# recognize speech using Sphinx
try:
    print("Sphinx thinks you said " + r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))

# # recognize speech using Google Speech Recognition
# try:
#     # for testing purposes, we're just using the default API key
#     # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
#     # instead of `r.recognize_google(audio)`
#     # print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
#     print("Google Speech Recognition thinks you said " + r.recognize_google(audio, key="AIzaSyAvsddrMAv7uJS8URI8-vA7Wmaxfq9Ar3o"))
# except sr.UnknownValueError:
#     print("Google Speech Recognition could not understand audio")
# except sr.RequestError as e:
#     print("Could not request results from Google Speech Recognition service; {0}".format(e))

# recognize speech using Google Cloud Speech
GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"""{
  "type": "service_account",
  "project_id": "microphonetest-159523",
  "private_key_id": "4af07f0f158281b944bf545dfa68ecc8071dd82e",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC6whIaMyUPoV8R\nOw+6zGSrQqvGIKpmavEayrHJD6bYFlZUmxV8BBBGOnmU8TQxeDAMvU1l+I+6/by+\nfz2wirKMJxZ84WIesVm/fM9uGaNvfoAkJtCaxgrbWF+6CFloE4Hi0BfIzhAOQlcf\nOvSSfBkdSL/k++AV8pP85PuzSkDoCGkWv5BS+5p8sbIHUU43oGiW21N1eikJnbJS\n2VdE22OTw33brOlAEbFguuLWYMTqxmzU8R3TIRrkZPTcIXSXfxeuBE248P6G256y\nxfPpZfwJwucU8jUQQacZyuPiSvCWWyyDTGNSk13t3LVjsn9aVZkR+dV+4EsGnsGS\nOxS1AR3NAgMBAAECggEAH+y68XWauUBJowVom/MCpnAAMx80YcuYKY9KsucVC01O\nNqpIEuoS6h5m2DofRPGZrSPTDkJeN4XWdO4FWp9rBCBObMyOXFbO07f/MX/6ez2x\no/xqnnqKMpK50nBI8EydYGtYFYB8KCPZBsKqOjwygtoDy53u4XGVMJ7oE+72h3NV\nyXxry5IUfYbuSFM7JiZGavlyIBHqhAjmKV8yFsy90V+rZwm1UIatNo+4PxVPJhtV\n7R7FPu2DayofCV3mZgCuTqbvTtizHX7uai0reWiikf66EE+XCeeP8nJ6VQkO+sWl\nKk4LaHfUCdtlxOUkmldsgsBJAAlqJv4tqusL6tUt1QKBgQDj9B2lep9OObp+kbJv\nKsHmHOYDgvq4QMJavxxbUdQypVnHrU5hA/6zRchBwqo4pDr0wsvdRnEcw5QJXgxf\n8xIhXkdYKLgSAGU87pdXNYS7X9HmMvH3KmCXTF3m7wc8aEfzhc9RpcI497nrfThW\n5Uynb6Zf2W2pS/htWt5aKwvzswKBgQDRvGpEyXbq/mcnC6YO+6cVPikFmeFvaicW\nuD75HawGOFkDPdBkCIXBotJMpaCDpraz0N34sKM74QbMSiqQ4rFe/AGmeyF08P4q\nKtae7cgpo3Hnm9VXqaFPjnv7wBG6ce2oLzUj/Wg5SID9N437OVMZTKmFriraNR+n\nHhh0HWPofwKBgGwJpgdo35n+qFIWkaA4fp+mcKmXaWbsYnEKBNGPLeg3EB8gF3bJ\nouyqlSf9sBmaVMrujBq6qR993mq2JV1QYfZorZ2t5te5UkIXvqi5l8gKuPvGh4Gi\nlxb+Pb8W6LILppZXhBPpYO0JFBf1SD9++96bfxoMffnwJLUHjTzlDAwbAoGANeIH\nFzb/Ay5qx+A5QF4stctrdJHtFdeaxT5+hze1Sz/MtoV59UkvO+kdyC1BCLGa/KVr\ncYnH1glg2rkvKFvlH7b0oZW+qbGESscIrnn+U5w3Fj6117ivxaWgerQEmfbNDMlc\nCKwAy76xzNwp8OHwVG6amsp9HeRKBoA33hTy5vcCgYEA1jNbV1A7PMN8CA5skgvV\nGAshzUgel+ctOFUXumJ1mAQrrwtA81yJDtDqzrLTHSUSvIZR4nwWTYHehp7RErWN\n6BsyOOHS/E16bZCnwJhSS3ZRYCimu7QEymNUMXE+pddIFLteRs+aQ8BJ5gZEppQu\nps4vpdPhxqNxxnq1wf8sNr4=\n-----END PRIVATE KEY-----\n",
  "client_email": "angan-527@microphonetest-159523.iam.gserviceaccount.com",
  "client_id": "101145818475366190401",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://accounts.google.com/o/oauth2/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/angan-527%40microphonetest-159523.iam.gserviceaccount.com"
}
"""
try:
    print("Google Cloud Speech thinks you said " + r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS))
except sr.UnknownValueError:
    print("Google Cloud Speech could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Cloud Speech service; {0}".format(e))

# # recognize speech using Wit.ai
# WIT_AI_KEY = "INSERT WIT.AI API KEY HERE" # Wit.ai keys are 32-character uppercase alphanumeric strings
# try:
#     print("Wit.ai thinks you said " + r.recognize_wit(audio, key=WIT_AI_KEY))
# except sr.UnknownValueError:
#     print("Wit.ai could not understand audio")
# except sr.RequestError as e:
#     print("Could not request results from Wit.ai service; {0}".format(e))

# # recognize speech using Microsoft Bing Voice Recognition
# BING_KEY = "INSERT BING API KEY HERE" # Microsoft Bing Voice Recognition API keys 32-character lowercase hexadecimal strings
# try:
#     print("Microsoft Bing Voice Recognition thinks you said " + r.recognize_bing(audio, key=BING_KEY))
# except sr.UnknownValueError:
#     print("Microsoft Bing Voice Recognition could not understand audio")
# except sr.RequestError as e:
#     print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))



