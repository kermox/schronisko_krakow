from whitenoise.storage import CompressedManifestStaticFilesStorage, StaticFilesStorage
from .settings import DEBUG

# For tests should inherit StaticFilesStorage otherwise CompressedManifestStaticFilesStorage
if DEBUG:
    class WhiteNoiseStaticFilesStorage(StaticFilesStorage):
        manifest_strict = False
else:
    class WhiteNoiseStaticFilesStorage(CompressedManifestStaticFilesStorage):
        manifest_strict = False
