from whitenoise.storage import CompressedManifestStaticFilesStorage, StaticFilesStorage


# For tests should inherit StaticFilesStorage, otherwise CompressedManifestStaticFilesStorage
class WhiteNoiseStaticFilesStorage(StaticFilesStorage):
    manifest_strict = False
