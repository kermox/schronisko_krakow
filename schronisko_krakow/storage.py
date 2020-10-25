from whitenoise.storage import (CompressedManifestStaticFilesStorage,
                                StaticFilesStorage)

from .settings import DEBUG

# For tests use StaticFilesStorage parent class otherwise CompressedManifestStaticFilesStorage


class WhiteNoiseStaticFilesStorage(StaticFilesStorage):
    manifest_strict = False
