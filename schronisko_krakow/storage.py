from whitenoise.storage import StaticFilesStorage


class WhiteNoiseStaticFilesStorage(StaticFilesStorage):
    # do no throw an error when static file is not found
    manifest_strict = False
