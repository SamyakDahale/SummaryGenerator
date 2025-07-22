import ssl
import nltk

# Workaround for SSL errors on Linux
ssl._create_default_https_context = ssl._create_unverified_context

# Download punkt cleanly to the right path
nltk.download('punkt', download_dir='/home/samyak-dahalelinux/nltk_data')
